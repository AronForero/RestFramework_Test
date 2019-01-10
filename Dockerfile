FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code/ 
COPY . /code

RUN apt-get update
RUN pip install pipenv
RUN pipenv --python 3.6
RUN pipenv install --system
