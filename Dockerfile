FROM python:3.9

ADD . /backend

WORKDIR /backend

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install