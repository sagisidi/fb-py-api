FROM python:3.7-alpine 
MAINTAINER Sagi CD 

ENV PYTHONUNBUFFERED 1

COPY ./Requirements.txt /Requirements.txt
RUN pip install -r /Requirements.txt 

RUN mkdir /api
WORKDIR /api
COPY ./api /api

RUN adduser -D user
USER user