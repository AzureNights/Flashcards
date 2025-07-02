import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from google import genai
import fitz # PyMuPDF import 
from langchain_text_splitters import RecursiveCharacterTextSplitter

# TODO 
# Get PDF file DONE
# Get text extracted from file DONE
# Use langchain - to chunk, vectorize and store my data 

# Get Info from PDF Uploads in text form PyPDF
def get_pdf_info(file):
    text = ""
    file = file.read()

    with fitz.open(stream=file, filetype="pdf") as doc:
        for page in doc:
            page_text = page.get_text()
            if page_text:
                text += page_text
    return text



# Split the text into chunks using langchain's text splitter 
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,   
        # Shows that its counting characters rather than token length. but default is char count - so line can be removed 
        length_function=len 
    )
    chunks = text_splitter.split_text(text)
    return chunks

# # Embed the chunks with google 
# def embed_the_chunks(chunks):
#     #for Japanese support - text-embedding-004 very good for eng 
#     embedding_model = "models/text-multilingual-embedding-002"

#     response = genai.embed_content(
#         model=embedding_model,
#         content=chunks,
#         #Optional + Only for models/embedding-001
#         # task_type
#     )
#     content = chunks




# Gemini API SetUp 
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

gemini_client = None
if GEMINI_API_KEY: 
    try:
        gemini_client = genai.Client(api_key=GEMINI_API_KEY)
        print("Global Gemini Client initialized. YAY!")

    except Exception as e:
        print(f"Error when initializing Gemini client: {e}")
        gemini_client = None

else: print("Gemini API Key not found. Global client not initialized.")


app = Flask(__name__)

#Configure Flask to handle UTF-8 Characters correctly 
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def test_apikey():
    if GEMINI_API_KEY:
        api_key_status = "API Key Works! YAY!"
    else:
        api_key_status = "Not found. Oops."


    if gemini_client:
        client_status = "Yay. Client was initialized too!"
    else:
        client_status = "Not initialized :("

    return f"Yay! App is running. <br> API Key Status: {api_key_status} <br> AI Status: {client_status}"


@app.route("/api/simple-prompt", methods = ["POST"])
def simple_prompt():

    gemini_client = genai.Client(api_key=GEMINI_API_KEY)
    response = gemini_client.models.generate_content(
        model="gemini-1.0-flash"
    )

    if gemini_client:
        return jsonify({
            "Success!": "Gemini AI at your service!"
        })
    
    else:
        return jsonify({
            "message": "This endpointworks YAY!"
        })



@app.route("/api/upload-file", methods = ["POST"])
def upload_file():
    file = request.files['file']

    if 'file' not in request.files:
        return jsonify({"error": "No 'file' found"}), 400
    
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    
    if not file.filename.endswith('.pdf'):
        return jsonify({"error": "Invalid file type. Please uplaod a .pdf file"}), 400
    

    try:
        extracted_text = get_pdf_info(file)

        chunked_text = get_text_chunks(extracted_text)

        return jsonify({
            "message": "File was processed successfully! Yay!",
            "filename": file.filename,
            "text_length": len(extracted_text),
            "text_preview": extracted_text[:250] + "...",
            "number_of_chunks": len(chunked_text),
            "chunk_preview": chunked_text[0] 
            if chunked_text else "No chunks generatet. Sorry!"
        }), 200
    
    except Exception as e: 
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# main driver func
if __name__ == '__main__':
    app.run(debug=True)

