FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /backend

COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["cmd", "-c", "python", "backend/manage.py", "runserver"]