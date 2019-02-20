import logging
import boto3
import os
import json
from slacker import Slacker
from flask import Flask, request

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

slack_webhook_url = os.environ.get('SLACK_WEBHOOK')
slack = Slacker('', incoming_webhook_url=slack_webhook_url)

@app.route('/', methods=['GET', 'POST'])
def send_message():
    message_body = request.args.get('message', '')
    body = {
        "text": message_body,
        "title": "foo"
    }
    slack.incomingwebhook.post(body)
    return ''
