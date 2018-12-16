#!/bin/sh
export FLASK_APP=sms.py
exec flask run --host 0.0.0.0
