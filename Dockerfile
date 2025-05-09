FROM python:3.10-slim

WORKDIR /app

COPY calculadora.py .
COPY test_calculator.py .

RUN pip install --no-cache-dir --upgrade pip

CMD ["python3", "-m", "unittest", "test_calculator.py"]
