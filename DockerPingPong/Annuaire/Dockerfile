# Set the base image to Ubuntu
FROM ubuntu:18.04

RUN apt update && apt upgrade -y

RUN apt install python3 -y 

COPY  Annuaire.py .

CMD python3 Annuaire.py

# Expose the default port
EXPOSE 8090
EXPOSE 8888
EXPOSE 8889