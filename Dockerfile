FROM python:3.7.4-alpine
WORKDIR /flaskdemo
ADD . /flaskdemo
RUN pip3 install -r requirement.txt
CMD ["python","app.py"]