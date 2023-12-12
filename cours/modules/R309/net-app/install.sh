#! /usr/bin/sh

mkdir -p ./net-app/src/icons/alternatives/
curl -O --output-dir ./net-app/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/[net-app,network_equipment,network_link,utils,coords].py
curl -O --output-dir ./net-app/src/icons/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/src/icons/[mobile,pc,router,switch].png
curl -O --output-dir ./net-app/src/icons/alternatives/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/src/icons/alternatives/[mobile.drawio,pc.drawio,router.drawio,router,switch.drawio,switch].png

cd ./net-app/