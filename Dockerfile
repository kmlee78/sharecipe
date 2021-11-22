FROM python:3.10.0
ENV PYTHONUNBUFFERED 1
WORKDIR /web
COPY . . 
RUN pip install -r requirements.txt