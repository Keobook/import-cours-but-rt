#!/usr/bin/sh

if [ $1 ];
  then
  echo "Reference to get: $1.json"
  echo "File to write: ../../temp/$1.json"
  if [ -e ../../temp/$1.json ];
    then
    curl -o ../../temp/$1.json https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_$1.json
  else
    mkdir ../../temp/
    curl -o ../../temp/$1.json https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_$1.json
  fi
else
  echo "No arguments given: $*"
fi
