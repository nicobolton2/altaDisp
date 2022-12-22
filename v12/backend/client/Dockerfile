FROM python:3.7-alpine

WORKDIR /client

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]