#!/usr/bin/sh

if [ $1 ];
  then
  echo "Reference to get: $1.json"
  echo "File to write: ../../temp/$1.json"
  if [ -e ../../temp/$1.json ];
    then
    echo "Let's curl our $1.json file!"
    curl https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_$1.json
  else
    echo "That's a problem, the folder doesn't exist..."
    mkdir ../../temp/
    curl https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_$1.json
  fi
else
  echo "No arguments given: $*"
fi
