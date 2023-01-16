#!/bin/sh

echo "Entrez un nombre à rechercher"
read x
clear
if [ $x -le 100 ] && [ $x -ge 1 ];
then
  y=0;
  while [ $y -ne $x ]
  do
    echo "Entrez un nombre:";
    read y;
    if [ $y -lt $x ];
    then
      echo "Le nombre recherché est plus grand";
    else if [ $y -gt $x ];
    then
      echo "Le nombre recherché est plus petit"
    fi
    fi
  done
  echo "Le nombre recherché est bien $y";
else
echo "Mauvaise entrée ! Donner un nombre 1-100"
fi

