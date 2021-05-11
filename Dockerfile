FROM python:latest
MAINTAINER Rodrigo Magalhães
WORKDIR /codes/
COPY ./codes/ .
COPY requirements.txt .
RUN pip install -r requirements.txt
