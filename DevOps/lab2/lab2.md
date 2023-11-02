## Лаборатоная работа №2

### Основное задание

#### Текст задачи

Написать два Dockerfile – плохой и хороший. Плохой должен запускаться и работать корректно, но в нём должно быть не
менее 3 “bad practices”. В хорошем Dockerfile они должны быть исправлены. Также привести 2 плохие практики по
использованию хорошего контейнера.

#### Плохие практики

- Использование `apt-upgrade`, `apt-get update`. Это может увеличить размер образа, что в свою очередь ожидает и
  контейнер.
- Использование тега `:latest` в продакшне может повлечь за собой конфликты между версиями.
- Использование пользователя с привелигированным доступом может представлять угрозы безопасности.

#### Ход работы

1. Сначала создал базовый код на Python, используя FastAPI.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}
```

2. Далее создал плохой Dockerfile - **bad.Dockerfile**

```dockerfile
FROM python:latest
RUN apt upgrade
WORKDIR ./DevOps/lab2
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./main.py .
EXPOSE 80
USER root
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

В коде видно, что использованы все перечисленные плохие практики. Тем не менее, образ собрался, а контейнер запустился.

3. Собрал образ и контейнер, написав в терминале `docker build -t bad-docker -f bad.Dockerfile .` и запустил
   его `docker run -p 80:80 bad-docker`.
   По адресу localhost:80 выводится мое API:
   ![api.png](static%2Fapi.png)
4. Исправил код в файле **Dockerfile**

```dockerfile
FROM python:3.12
WORKDIR ./DevOps/lab2
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./main.py .
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

5. Собрал образ исправленного файла `docker build -t good-docker -f Dockerfile .`,
   запустил `docker run -p 80:80 good-docker`.
   ![api.png](static%2Fapi.png)
   ![img.png](static%2Fimg.png)

#### Вывод

По результату вышепредставленные Dockerfile'ы не отличаются, однако использование плохих практик может сказаться на
дальнешей работоспособности.