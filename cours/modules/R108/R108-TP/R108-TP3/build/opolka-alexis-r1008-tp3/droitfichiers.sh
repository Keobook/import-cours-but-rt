# !/bin/sh

if [ $# -le 1 ];
then
  echo "Sans argument";
  exit 1;
else
  str=$2
  for file in *:
  do
  if (! test -d "$file");
  then
    ## cfile -> Correct File
    for cfile in *"$2";
    do
      echo $cfile;
      chmod g$1 $cfile;
    done
  fi;
  done;
fi
