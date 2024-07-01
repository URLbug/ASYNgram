FROM python:3.12

WORKDIR .
COPY . .

RUN python3 -m pip install -r requirements.txt