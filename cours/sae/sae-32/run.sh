#! /bin/bash

### First, we're installing the mongoDB server
docker run --user=mongodb -p 127.0.0.1:27017:27017 -d mongodb/mongodb-community-server:latest

### Then we're installing the backend
cd livre-mon-colis-backend/pyserver
uvicorn server:app &
cd ../../

### and we end by installing the web client
cd livre-mon-colis
yarn dev