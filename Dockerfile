FROM python:3.6-slim

RUN echo 'we are running some # of cool things'
WORKDIR /app
COPY . /app

RUN pip3 install pipenv
EXPOSE 80

# ENV NAME hello

# ENV FLASK_APP=demos/hello/app.py

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock


RUN pipenv install --deploy --system --ignore-pipfile
# ONBUILD RUN set -ex && pipenv install --deploy --system
ENV FLASK_APP=/app/app.py

# CMD ["pipenv","shell"]
CMD ["flask","run","--host=0.0.0.0"]
# CMD ["python3","-m","flask","run"]


ENV http_proxy 0.0.0.0:80
ENV https_proxy host:port
