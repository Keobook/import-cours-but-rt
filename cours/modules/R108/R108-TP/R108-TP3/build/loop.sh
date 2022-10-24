# !/bin/sh

if [ $# -le 1 ];
then
  echo "Sans argument";
  exit 1;
else
  for arg in $*;
  do
    echo $arg
    shift
  done;
fi
