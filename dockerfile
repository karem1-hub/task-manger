FROM python:3.10-slim

WORKDIR /app

COPY . .
#it is solved by adding the line below 
ENV PYTHONUNBUFFERED=1 

CMD ["python3", "main.py"]
