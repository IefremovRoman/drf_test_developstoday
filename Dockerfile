# syntax=docker/dockerfile:1
FROM python:3.9.7
ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8002

CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]