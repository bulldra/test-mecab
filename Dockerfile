FROM python:3.9.4-slim-buster

ENV TZ JST-9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=on
ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN apt-get update -y && apt-get install -y \
        git curl make xz-utils file sudo \
        mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
WORKDIR /tmp/mecab-ipadic-neologd
RUN ./bin/install-mecab-ipadic-neologd -n -y \
    && rm -r /tmp/mecab-ipadic-neologd

WORKDIR /tmp
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade pip \
    && pip3 install -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

RUN ln -s /etc/mecabrc /usr/local/etc/
RUN ln -s /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd /usr/local/etc/

RUN mkdir /data
