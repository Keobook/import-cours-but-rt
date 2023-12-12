#! /usr/bin/sh

mkdir -p ./net-app/src/icons/alternatives/
curl -O --output-dir ./net-app/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/net-app.py
curl -O --output-dir ./net-app/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/network_equipment.py
curl -O --output-dir ./net-app/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/network_link.py
curl -O --output-dir ./net-app/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/utils.py
curl -O --output-dir ./net-app/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/coords.py

cd ./net-app/src/icons

wget https://github.com/alexis-opolka/import-cours-but-rt/raw/master/cours/modules/R309/net-app/src/icons/mobile.png?download= -O mobile.png
wget https://github.com/alexis-opolka/import-cours-but-rt/raw/master/cours/modules/R309/net-app/src/icons/pc.png?download= -O pc.png
wget https://github.com/alexis-opolka/import-cours-but-rt/raw/master/cours/modules/R309/net-app/src/icons/router.png?download= -O router.png
wget https://github.com/alexis-opolka/import-cours-but-rt/raw/master/cours/modules/R309/net-app/src/icons/switch.png?download= -O switch.png

cd ./alternatives/

wget https://github.com/alexis-opolka/import-cours-but-rt/raw/master/cours/modules/R309/net-app/src/icons/alternatives/mobile.drawio.png?download= -O mobile.drawio.png
wget https://github.com/alexis-opolka/import-cours-but-rt/raw/master/cours/modules/R309/net-app/src/icons/alternatives/pc.drawio.png?download= -O pc.drawio.png
wget https://github.com/alexis-opolka/import-cours-but-rt/raw/master/cours/modules/R309/net-app/src/icons/alternatives/router.drawio.png?download= -O router.drawio.png
wget https://github.com/alexis-opolka/import-cours-but-rt/raw/master/cours/modules/R309/net-app/src/icons/alternatives/router?download= -O router.png
wget https://github.com/alexis-opolka/import-cours-but-rt/raw/master/cours/modules/R309/net-app/src/icons/alternatives/switch.drawio.png?download= -O switch.drawio.png
wget https://github.com/alexis-opolka/import-cours-but-rt/raw/master/cours/modules/R309/net-app/src/icons/alternatives/switch.png?download= -O switch.png

cd ../../