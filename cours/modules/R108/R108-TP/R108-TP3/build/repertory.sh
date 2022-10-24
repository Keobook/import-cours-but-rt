# !/bin/sh

for rep in *;
do
  if (test -d "$rep");
  then
    echo $rep;
  fi;
done;
