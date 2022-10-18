# !/bin/sh

if [ $# -le 1 ];
then
  echo "Sans argument";
  exit 1;
else
  while [ $# -ne 0 ];
  do
    echo $1
    shift
  done
fi
