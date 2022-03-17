from flask import Flask, jsonify
from speech_to_text import automatic_speech_recognition

app = Flask(__name__)

@app.route("/")
def homepage():
    return "HELLO"

@app.route("/speechtotext/<fileId>", methods=['GET'])
def speechToText(fileId):
    # speechTranscript = automatic_speech_recognition(fileId)
    return jsonify("Helllo")

if __name__ == "__main__":
    app.run()