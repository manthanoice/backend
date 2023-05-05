# Start with a Python 3.10.11 base image
FROM python:3.10.11

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "--bind", "127.0.0.1:8000"]