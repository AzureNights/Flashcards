from flask import Flask
from dotenv import load_dotenv
import os
from google import genai


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain some kanji"
)
# print(response.text)

app = Flask(__name__)

@app.route('/')
def test_apikey():
    if GEMINI_API_KEY:
        api_key_status = "API Key Works! YAY!"
    else:
        api_key_status = "Not found. Oops."


    if client:
        client_status = "Yay. Client was initialized too!"
    else:
        client_status = "Not initialized :("


    return f"Yay! App is running. API Key Status: {api_key_status} AI Status: {client_status}"

@app.route("/questions")
def questions():
    return {"questions":
            ["nani desu ka? = whats that", "yes"]}


# main driver func
if __name__ == '__main__':
    app.run(debug=True)

