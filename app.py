from flask import Flask, jsonify, Response
from speech_to_text import automatic_speech_recognition
from celery import Celery
from time import sleep

app = Flask(__name__)

app.config['CELERY_BROKER_URL'] = 'amqps://rzlgmprn:scZ9iVo_d6pZj7hzPEWvjrXjiMtA7W1F@puffin.rmq2.cloudamqp.com/rzlgmprn'

celery = Celery(app.name,  backend='rpc://', broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route("/")
def homepage():
    return "HELLO"

@celery.task
def computeTranscript(fileId):
    sleep(10)
    print(2)
    # return automatic_speech_recognition(fileId)

@app.route("/speechtotext/<fileId>", methods=['GET'])
def speechToText(fileId):
    result = computeTranscript.delay(fileId)

    def stream():
        while not result.ready():
            sleep(1)
            yield f"data: Processing\n\n"

        yield f"data: {result.get()}\n\n"

    return Response(stream(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run()