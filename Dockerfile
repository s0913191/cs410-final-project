#dockerイメージを指定。
FROM python:3.11-slim
RUN apt-get -y update && apt-get -y upgrade
#コンテナ内での作業ディレクトリを指定。
WORKDIR root


RUN mkdir app
#main.pyを/root/appに以下にコピー。
COPY search_api.py app/
COPY consolidated_docs.json app/
COPY app.js app/
#requirements.txtをコンテナ内のroot配下にコピー。
COPY requirements.txt requirements.txt
# コンテナ起動時にモジュールをインストール。
RUN pip install -r requirements.txt
#コンテナ起動時に実行するコマンドを指定。
ENTRYPOINT ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]