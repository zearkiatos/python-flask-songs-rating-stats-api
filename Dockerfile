FROM python:alpine3.11

COPY . /app/

WORKDIR /app

RUN apk update && apk upgrade
RUN apk add --no-cache build-base
RUN apk add --no-cache g++ jpeg-dev zlib-dev libjpeg make gcc
RUN apk add --no-cache libffi-dev postgresql-dev
RUN apk add --no-cache python3-dev  py-pip
RUN apk add --no-cache py-pip py-virtualenv
RUN pip install --upgrade pip setuptools
RUN pip install --upgrade pip
RUN pip install wheel
RUN export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/
RUN make install

EXPOSE 6000

ENTRYPOINT ["sh", "./docker/entrypoint.sh"]