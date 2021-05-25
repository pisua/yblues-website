FROM python:3.10-rc-buster

COPY app /opt/yblues/

COPY run.sh /opt/yblues/run.sh
RUn pip3 install jwt pymongo
RUN chmod a+x /opt/yblues/run.sh

CMD ["/opt/yblues/run.sh"]