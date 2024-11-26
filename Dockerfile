FROM python:3.13.0-alpine3.20 

RUN apk upgrade --no-cache

WORKDIR /home
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

ENTRYPOINT [ "/bin/sh" ]