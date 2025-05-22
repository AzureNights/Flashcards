from flask import Flask
from dotenv import load_dotenv
import os


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route("/questions")
def questions():
    return {"questions":
            ["nani desu ka? = whats that", "yes"]}


# main driver func
if __name__ == '__main__':
    app.run(debug=True)

