FROM python:3.10-slim-buster
WORKDIR /bot
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN apt-get update
CMD ["python3", "bot.py"]
