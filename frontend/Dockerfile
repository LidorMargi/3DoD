FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip \
    pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["streamlit", "run", "app.py"]