FROM python:3.10.0
ENV PYTHONUNBUFFERED 1
WORKDIR /web
COPY . . 
RUN chmod +x scripts/*.sh
RUN pip install --upgrade pip && pip install poetry
RUN poetry config virtualenvs.create false
CMD ["/bin/bash", "scripts/run-server.sh"]