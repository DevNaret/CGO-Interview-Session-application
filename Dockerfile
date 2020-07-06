FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./code/* ./
COPY requirements.txt /
RUN pip install -U pip \
    && pip install -r /requirements.txt
ADD . /code/
EXPOSE 9999
CMD python3 code/Python_Assignment/manage.py runserver 0.0.0.0:9999