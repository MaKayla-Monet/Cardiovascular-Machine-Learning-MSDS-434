FROM python:3.10

WORKDIR /app

COPY requirments.txt .
RUN pip install -r requirments.txt

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]
