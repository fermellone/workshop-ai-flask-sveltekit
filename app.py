import os
os.environ["OPENAI_API_KEY"] = "acá va tu api key..."


from flask import Flask, jsonify, request
from flask_cors import CORS

from langchain.llms import OpenAI

llm = OpenAI()

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    args = request.args
    message = llm(args['prompt'])
    response = jsonify(message=message)
    return response

@app.route("/about")
def about():
    response = jsonify(message="Hola about")
    return response