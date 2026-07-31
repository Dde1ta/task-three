FROM python:3.12-alpine

RUN mkdir "app"

WORKDIR "/app"

COPY requirments.txt "/app"

RUN pip install -r requirments.txt

COPY . "/app"

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]