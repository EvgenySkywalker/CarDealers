FROM python:3.9

ADD backend /backend
ADD service_scripts /service_scripts

WORKDIR /backend

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install