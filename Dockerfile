FROM ubuntu:latest
MAINTAINER Fagani Hajizada "hacizade.faqani@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential cron
ADD . /DevOpstalks
WORKDIR /DevOpstalks
RUN pip install -r requirements.txt
RUN touch /var/log/cron.log
COPY root /var/spool/cron/crontabs
RUN chmod 0600 /var/spool/cron/crontabs/root
CMD cron && tail -f /var/log/cron.log
ENV MESSAGE "DevOPS Talks"
