FROM python:3.12-alpine3.20
COPY requirements.txt /
RUN pip3 install -r requirements.txt
COPY src /src
EXPOSE 8000
WORKDIR /src
RUN fastapi run
