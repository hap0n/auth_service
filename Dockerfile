FROM python:3.10

COPY poetry.lock pyproject.toml /app/
RUN apt-get update

COPY . app/
WORKDIR app

RUN pip install -e .

EXPOSE 8080
