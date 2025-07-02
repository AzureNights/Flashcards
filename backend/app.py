import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from google import genai
import fitz # PyMuPDF import 
from langchain_text_splitters import RecursiveCharacterTextSplitter


# ------------------------------------------------------------------------------------------------------------
# Gemini API SetUp 
# ------------------------------------------------------------------------------------------------------------

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY: 
        client = genai.Client(api_key=GEMINI_API_KEY)
        print("Global Gemini Client initialized. YAY!")

else: print("Gemini API Key not found. Global client not initialized.")

# ------------------------------------------------------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------------------------------------------------------

# Get Info from PDF Uploads in text form using PyMuPDF
def get_pdf_info(file):
    text = ""
    file_in_bytes = file.read()
    with fitz.open(stream=file_in_bytes, filetype="pdf") as doc:
        for page in doc:
            page_text = page.get_text()
            if page_text:
                text += page_text
    return text


# Split the text into chunks using langchain's text splitter 
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,   
        # Shows that its counting characters rather than token length. but default is char count - so line can be removed 
        length_function = len 
    )
    chunks = text_splitter.split_text(text)
    return chunks


# Embed the chunks with google AI 
def embed_the_chunks(chunks):
    
    result = client.models.embed_content(
        #for Japanese support - text-embedding-004 very good for eng 
        model = "models/text-embedding-004",
        contents = chunks,
        # check which one 
        config = {"task_type": "retrieval_document"}
    )

    embedding_values = [embedding.values for embedding in result.embeddings]

    return embedding_values

# ------------------------------------------------------------------------------------------------------------
# Flask App Routes 
# ------------------------------------------------------------------------------------------------------------

app = Flask(__name__)
#Configure Flask to handle UTF-8 Characters correctly 
app.config['JSON_AS_ASCII'] = False

@app.route("/api/process-file", methods = ["POST"])
def process_file():
    if 'file' not in request.files:
        return jsonify({"error": "No 'file' found"}), 400
    
    file = request.files['file']
    
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    
    if not file.filename.endswith('.pdf'):
        return jsonify({"error": "Invalid file type. Please uplaod a .pdf file"}), 400
    
    try:
        extracted_text = get_pdf_info(file)
        if not extracted_text:
            return jsonify({"error": "Could not extract the text from the PDF"}), 400

        chunked_text = get_text_chunks(extracted_text)
        if not chunked_text:
            return jsonify({"error": "Could not split text into chunks"}), 400
        
        embedded_chunks = embed_the_chunks(chunked_text)

        return jsonify({
            "message": "File was processed successfully! Yay!",
            "filename": file.filename,
            "text_length": len(extracted_text),
            "number_of_chunks": len(chunked_text),
            "number_of_embeddings": len(embedded_chunks),
            "text_preview": extracted_text[:250] + "...",
            "chunk_preview": chunked_text[0][:100] 
            if chunked_text else "No chunks generated. Sorry!",
            "embeddings_preview": embedded_chunks[0][:5] 
            if embedded_chunks else []
        }), 200
    
    except Exception as e: 
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# ------------------------------------------------------------------------------------------------------------
# Main Driver Func
# ------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)

