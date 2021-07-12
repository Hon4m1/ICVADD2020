# Set the base image to Ubuntu
FROM ubuntu:18.04

RUN apt update && apt upgrade -y

RUN apt install python3 -y 

COPY  WebServerPing.py .
COPY  clientsUtils.py .

CMD python3 WebServerPing.py

# Expose the default port
EXPOSE 8888
EXPOSE 8090