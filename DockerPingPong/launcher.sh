#!/bin/sh


cd Ping
docker build -t ping .
cd..

cd Pong
docker build -t pong .
cd..

cd Annuaire
docker build -t annuaire .
cd ..

docker run --rm -it --network host ping

docker run --rm -it --network host pong

docker run --rm -it --network host annuaire