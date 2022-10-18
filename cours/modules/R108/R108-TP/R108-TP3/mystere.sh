# !/bin/sh

if [ $# -ne 1 ]; then
  echo "Fournir un nom en parametre";
  exit 1;
fi
if ( test -d "$1" ); then
  echo "Répertoire "$1" existe déja"
  exit 0
else
  echo "Script : "$0" nom de repertoire: "$1" "
  mkdir "$1"
fi
