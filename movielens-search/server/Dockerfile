FROM python:3.10

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install dependencies
COPY ./dev-requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r dev-requirements.txt