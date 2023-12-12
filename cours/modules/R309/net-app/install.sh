#! /usr/bin/sh

mkdir -p ./net-app/src/icons/alternatives/
curl -O --output-dir ./net-app/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/net-app.py
curl -O --output-dir ./net-app/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/network_equipment.py
curl -O --output-dir ./net-app/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/network_link.py
curl -O --output-dir ./net-app/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/utils.py
curl -O --output-dir ./net-app/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/coords.py
curl -O --output-dir ./net-app/src/icons/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/src/icons/mobile.png
curl -O --output-dir ./net-app/src/icons/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/src/icons/pc.png
curl -O --output-dir ./net-app/src/icons/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/src/icons/router.png
curl -O --output-dir ./net-app/src/icons/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/src/icons/switch.png
curl -O --output-dir ./net-app/src/icons/alternatives/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/src/icons/alternatives/mobile.drawio.png
curl -O --output-dir ./net-app/src/icons/alternatives/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/src/icons/alternatives/pc.drawio.png
curl -O --output-dir ./net-app/src/icons/alternatives/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/src/icons/alternatives/router.drawio.png
curl -O --output-dir ./net-app/src/icons/alternatives/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/src/icons/alternatives/router.png
curl -O --output-dir ./net-app/src/icons/alternatives/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/src/icons/alternatives/switch.drawio.png
curl -O --output-dir ./net-app/src/icons/alternatives/ https://raw.githubusercontent.com/alexis-opolka/import-cours-but-rt/master/cours/modules/R309/net-app/src/icons/alternatives/switch.png

cd ./net-app/