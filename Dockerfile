FROM python:3.10-rc-buster

COPY pelix /opt/yblues/pelix
COPY ycappuccino /opt/yblues/ycappuccino
COPY yblues /opt/yblues/yblues

COPY run.sh /opt/yblues/run.sh

RUN chmod a+x /opt/yblues/run.sh

CMD ["/opt/yblues/run.sh"]