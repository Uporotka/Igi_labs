FROM python:latest
ADD main.py /
COPY . /python
WORKDIR /python
CMD [ "python", "./main.py" ]