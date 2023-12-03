FROM python:3.12

WORKDIR /app

COPY DevOps/lab3/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "main.py"]
