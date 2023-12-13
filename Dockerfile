#dockerイメージを指定。
FROM python:3.11-slim
RUN apt-get -y update && apt-get -y upgrade
#コンテナ内での作業ディレクトリを指定。
WORKDIR root

RUN mkdir src
ENV PYTHONPATH "${PYTHONPATH}:/root/src"

COPY src src/
COPY data data/
COPY app.js app.js
COPY index.html index.html
COPY requirements.txt requirements.txt

# コンテナ起動時にモジュールをインストール。
RUN pip install -r requirements.txt
#コンテナ起動時に実行するコマンドを指定。
ENTRYPOINT ["uvicorn", "src.search_api:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]