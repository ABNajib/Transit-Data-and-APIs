FROM python:3.11.4-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app/. .

EXPOSE 3000

CMD [ "python", "server.py" ]

