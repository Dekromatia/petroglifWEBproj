FROM ubuntu:focal
# FROM python:3.7

RUN apt update
RUN apt install -y python3-pip
#RUN pip3 install flask requests перешло requirements-web.txt

RUN mkdir -p /app
WORKDIR  /app 


COPY requirements-web.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

#COPY  /app/  - копируем все содержимое дирриктории но можно копировать только отдельные файлы внутрь нашего образа как ниже
COPY web.py /app/web.py 
COPY templates /app/templates
COPY static /app/static

CMD ["python3", "web.py"]

EXPOSE 5000
