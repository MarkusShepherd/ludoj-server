FROM python:3.6-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV MAILTO=''
ENV PYTHONPATH=.

RUN mkdir -p /app
WORKDIR /app

RUN apt-get -y update && \
    apt-get -y install --no-install-recommends git && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install --upgrade pip pipenv
COPY Pipfile* ./
RUN pipenv install --deploy --system --verbose

COPY db.sqlite3 ./
RUN chmod 0444 db.sqlite3
COPY games games
COPY ludoj ludoj
COPY static static

RUN useradd -m ludoj
USER ludoj

CMD gunicorn --bind 0.0.0.0:$PORT ludoj.wsgi
