#! /bin/bash

mkdir livre-mon-colis
cd livre-mon-colis

### First, we're installing the mongoDB server
docker pull mongodb/mongodb-community-server:latest

### Then we're installing the backend
git clone https://github.com/alexis-opolka/livre-mon-colis-backend.git
cd livre-mon-colis-backend/pyserver
pip3 install -r ./requirements.txt
cd ../../

### and we end by installing the web client
git clone https://github.com/alexis-opolka/livre-mon-colis.git
cd livre-mon-colis
sudo npm i -g yarn
yarn

cd ../
curl -O https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/sae/sae-32/run.sh
chmod +x run.sh
