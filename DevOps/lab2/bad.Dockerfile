FROM python:latest
RUN apt upgrade
WORKDIR ./DevOps/lab2
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./main.py .
EXPOSE 80
USER root
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]