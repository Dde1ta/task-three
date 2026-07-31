FROM python:3.12-alpine

RUN mkdir "app"

WORKDIR "/app"

COPY requirements.txt "/app"

RUN pip install -r requirements.txt

COPY . "/app"

CMD ["uvicorn", "--host", "0.0.0.0", "main:app"]