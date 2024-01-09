#! /bin/bash

mkdir livre-mon-colis
cd livre-mon-colis

### First, we're installing the mongoDB server
docker pull mongodb/mongodb-community-server:latest
docker run --user=mongodb -p 127.0.0.1:27017:27017 -d mongodb/mongodb-community-server:latest

### Then we're installing the backend
git clone https://github.com/alexis-opolka/livre-mon-colis-backend.git
cd livre-mon-colis-backend/pyserver
pip3 install -r ./requirements.txt
uvicorn server:app &
cd ../../

### and we end by installing the web client
git clone https://github.com/alexis-opolka/livre-mon-colis.git
cd livre-mon-colis
sudo npm i -g yarn
yarn
yarn dev