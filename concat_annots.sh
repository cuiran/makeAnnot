#!/bin/bash

CHR=$1
S=$2
E=$3
NAME=$4
DIR=$5

command=paste
for i in ${DIR}Roadmap.{$S..$E}.$CHR.annot.gz; do
    command="$command <(gzip -cd $i | cut -f5)"
done
eval $command > $NAME.annot
