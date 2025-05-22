from flask import Flask

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

