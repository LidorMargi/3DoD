FROM python:3.10-slim

WORKDIR /fastapi-backend

COPY . /fastapi-backend

RUN pip install --upgrade pip \
    pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]