# first stage
FROM python:3.8 AS builder

ENV PYTHONUNBUFFERED=1

WORKDIR /django

COPY django/requirements/base.txt .

# install dependencies to the local user directory (eg. /root/.local)
RUN pip install --user -r base.txt --no-warn-script-location

COPY . django/