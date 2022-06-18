from flask import Flask
app = Flask(__name__)
from flask import request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# from learn_simple import generate_sentence

DEFAULT_ERROR_MSG = "Sever Error"

@app.route("/test/", methods=["GET"])
def test():
    return "Welcome to test!!!"

@app.route("/generate_text/", methods=['POST'])
def generate_text():
    if "text" not in request.POST: return DEFAULT_ERROR_MSG
    minchar = 10 if "min_char" not in request.POST else request.POST["min_char"]
    maxchar = 75 if "max_char" not in request.POST else request.POST["max_char"]
#     return generate_sentence(request.POST["text"], format, maxchar, minchar)

if __name__ == "__main__":
    app.run(debug=True)