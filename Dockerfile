FROM python:3.8-alpine3.13 as BUILD

RUN apk add --update \
    && apk add --no-cache build-base curl-dev linux-headers bash git musl-dev\
    && rm -rf /var/cache/apk/*

COPY requirements.txt /root/minimal/requirements.txt
COPY README.md /root/minimal/README.md
COPY setup.py /root/minimal/setup.py
COPY minimalpy /root/minimal/minimalpy

RUN pip install --upgrade pip && \
    pip install -r /root/minimal/requirements.txt && \
    pip install /root/minimal

FROM python:3.8-alpine3.13

RUN apk add --no-cache --update bash

LABEL maintainer "blankdots"
LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.vcs-url="https://github.com/blankdots/minimalpy"

COPY --from=BUILD usr/local/lib/python3.8/ usr/local/lib/python3.8/

COPY --from=BUILD /usr/local/bin/gunicorn /usr/local/bin/

COPY --from=BUILD /usr/local/bin/minimal /usr/local/bin/

RUN mkdir -p /app

WORKDIR /app

COPY ./deploy/app.sh /app/app.sh

RUN chmod +x /app/app.sh

ENTRYPOINT ["/bin/sh", "-c", "/app/app.sh"]
