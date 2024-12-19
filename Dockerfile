FROM python:3.11

WORKDIR /app

COPY src/ .

COPY requirements.txt .

RUN pip3 install -r requirements.txt

USER root

ENTRYPOINT [ "" ]

CMD [ "python3.11", "app.py" ]