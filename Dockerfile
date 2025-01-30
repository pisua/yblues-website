FROM python:slim-buster

COPY app /opt/yblues/

COPY run.sh /opt/yblues/run.sh
RUn pip install PyJWT pymongo ipopo
RUN chmod a+x /opt/yblues/run.sh

CMD ["/opt/yblues/run.sh"]
