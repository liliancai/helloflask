FROM python:3.6-slim

RUN echo 'we are running some # of cool things'
WORKDIR /app
COPY . /app

RUN pip3 install pipenv
EXPOSE 80

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# Really important to add --system cause docker image don't need virtualenv
# Otherwise would get path error or flask import error
RUN pipenv install --deploy --system --ignore-pipfile

ENV FLASK_APP=flasky.py

CMD ["flask","run","--host=0.0.0.0","--port=80"]


ENV http_proxy 0.0.0.0:80
ENV https_proxy host:port
