FROM python:3.12-alpine

RUN mkdir "app"

WORKDIR "/app"

COPY requirments.txt "/app"

RUN pip install -r requirments.txt

COPY . "/app"

CMD ["uvicorn", "--host", "0.0.0.0", "main:app"]