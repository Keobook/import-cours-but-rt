#!/bin/sh

file=var-folders.log


echo "/var/ directories (including symbolic-links)" > $file
echo "" >> $file
ls -l --format=commas /var/ >> $file
echo "" >> $file
echo "/var/spool/ files" >> $file
echo "" >> $file
ls -l --format=verbose /var/spool/ >> $file
