FROM python:3.11-alpine

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

WORKDIR /app

ENV CW_LOG_TRACE=http://0.0.0.0:5050
ENV CW_LOG_TRACE_IP=0.0.0.0
ENV CW_LOG_TRACE_PORT=5050

CMD [ "python", "./src/main.py"  ]