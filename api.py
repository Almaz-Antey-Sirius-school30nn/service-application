import requests as requests
from flask import request

from app import app
from config import ACCESS_TOKEN, AI_SERVER_IP


@app.route("/api/photo", methods=['POST'])
def photo_analyze():
    data = request.data
    fname = request.headers['fname']
    token = request.headers['token']

    if token != ACCESS_TOKEN:
        return "", 403

    requests.post(AI_SERVER_IP + "/api/photo", data=data, headers={"fname": fname})

    return "OK"
