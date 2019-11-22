FROM python:3.7-alpine3.9

RUN apk add --no-cache -U \
    python3-dev && \
  pip install -U pip pipenv

RUN mkdir /app
COPY Pipfile /app
COPY Pipfile.lock /app

WORKDIR /app
RUN pipenv install --deploy --system

COPY sms.py /app

COPY docker-entrypoint.sh /app
RUN chmod +x /app/docker-entrypoint.sh

ENTRYPOINT /app/docker-entrypoint.sh
