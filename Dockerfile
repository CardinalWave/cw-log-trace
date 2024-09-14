# Imagem base do Python na versao 3.11
FROM python:3.11-alpine

COPY requirements.txt .


# Instala as propriedades necessarias
RUN apk add --no-cache git build-base

# Atualiza as dependencias
RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
RUN python3 -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

WORKDIR /app

ENV CW_LOG_TRACE=http://0.0.0.0:5050
ENV CW_LOG_TRACE_IP=0.0.0.0
ENV CW_LOG_TRACE_PORT=5050

CMD [ "python", "./src/main.py"  ]