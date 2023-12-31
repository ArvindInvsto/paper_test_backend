FROM python:3.11

WORKDIR /paper_test_backend

COPY requirements.txt .

RUN apt-get update && apt-get install -y git && RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8002

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
