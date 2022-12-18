FROM alpine:3.14 AS builder
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
WORKDIR /app
EXPOSE 8000
COPY requirements.txt /app
#RUN pip3 install -r requirements.txt --no-cache-dir
ENTRYPOINT ['python3']
CMD ['manage.py', 'runserver', '0.0.0.0:8000']