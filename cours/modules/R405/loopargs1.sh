#!/bin/bash

for i in $*; do echo $i; done

echo -e '\n'

for i in $@; do echo $i; done

echo -e '\n'

for i in "$*"; do echo $i; done

echo -e '\n'

for i in "$@"; do echo $i; done