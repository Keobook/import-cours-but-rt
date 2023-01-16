#!/bin/sh

if [ $# -le 0 ];
then
  echo "Sans argument";
  exit 1;
else
  mkdir $1 &> err.log;
  if [ $? == 0 ];
  then
    echo "Tout s'est bien passé, exit-code: $?";
  else
    echo "Tout s'est mal passé, exit-code: $?, see err.log for more information";
  fi
fi
