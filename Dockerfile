FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD ping.py /
CMD [ "python", "./ping.py" ]
