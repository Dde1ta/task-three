FROM python:3.12-alpine

RUN mkdir "app"

WORKDIR "/app"

COPY requirements.txt "/app"

RUN pip install -r requirements.txt

COPY . "/app"

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]