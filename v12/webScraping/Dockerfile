FROM python:3.8.5-alpine

COPY . /cronjob
WORKDIR /cronjob

RUN pip3 install --upgrade pip
RUN pip3 install requests 
RUN pip3 install beautifulsoup4
RUN pip3 install pymongo

RUN crontab cronjob


CMD crond && tail -f /cronjob/out.log 