import os
from flask import Flask, jsonify, render_template, flash, request, redirect, url_for
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader
from io import BytesIO

# TODO 
# Get PDF file 
# Get text extracted from file

# File
# file = request.files



# Get Info from PDF Uploads
def get_pdf_info(file):
    pdf_reader = PdfReader(BytesIO(file.read()))
    text = ""




# Gemini API 
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


# main driver func
if __name__ == '__main__':
    app.run(debug=True)

