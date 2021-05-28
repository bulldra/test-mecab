FROM python:3.9.4-slim-buster

ENV TZ JST-9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=on
ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN apt update -y && apt-get upgrade -y
RUN apt install -y git curl make curl xz-utils file sudo
RUN apt install -y mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8

WORKDIR /opt
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
WORKDIR /opt/mecab-ipadic-neologd
RUN ./bin/install-mecab-ipadic-neologd -n -y

RUN pip3 install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

RUN ln -s /etc/mecabrc /usr/local/etc/
RUN ln -s /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd /usr/local/etc/

RUN mkdir /data
WORKDIR /data/
