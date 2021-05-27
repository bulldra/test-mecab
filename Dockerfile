FROM python:3.9.4-slim-buster

ENV TZ JST-9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=on
ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN apt update -y && apt-get upgrade -y
RUN apt install -y mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8
RUN ln /etc/mecabrc /usr/local/etc/

RUN pip3 install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

RUN mkdir /data
WORKDIR /data/

