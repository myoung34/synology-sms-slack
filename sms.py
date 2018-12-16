import logging
import boto3
from slacker import Slacker
from flask import Flask, request

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

slack_channel = os.environ.get('SLACK_CHANNEL', '#ops')
slack = Slacker(os.environ['SLACK_TOKEN'])

@app.route('/', methods=['GET', 'POST'])
def send_message():
    message_body = request.args.get('message', '')
    message = 'Synology'
    fields = [{
        "title": None,
        "value": message_body,
        "short": False
    }]
    attachments = [{
        'fallback': '',
        'message': '',
        'color': 'good',
        "fields": fields
    }]
    slack.chat.post_message(slack_channel, message, attachments=attachments)
    return ''
