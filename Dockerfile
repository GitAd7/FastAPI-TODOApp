FROM python:3.12-slim

WORKDIR /app

COPY requirments.txt requirments.txt
RUN pip install -r requirments.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]