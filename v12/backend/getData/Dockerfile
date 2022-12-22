FROM python:3.8.5-alpine

COPY . /cronjob
WORKDIR /cronjob

RUN pip install --upgrade pip
RUN pip install requests 
RUN pip install beautifulsoup4
RUN crontab cronjob
RUN pip install pymongo

CMD crond && tail -f /cronjob/out.log