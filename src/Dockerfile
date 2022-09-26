# syntax = docker/dockerfile:1.3
FROM python:3.10-alpine
LABEL maintainer="azat715"

# добавляю для wait-for-it.sh
RUN apk add --no-cache bash

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

RUN --mount=type=cache,target=/root/.cache \
    apk add --no-cache --virtual .build-deps build-base gcc musl-dev libffi-dev && \
    apk add  mysql-client mariadb-connector-c-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

COPY . /code/
ENTRYPOINT ["/code/entrypoint.sh"]