#!/bin/bash

CHR=$1
S=$2
E=$3
NAME=$4
DIR=$5
OUT=$6

command=paste
for i in ${DIR}Roadmap.{$S..$E}.$CHR.annot.gz; do
    command="$command <(gzip -cd $i | cut -f5)"
done
eval $command > ${OUT}${NAME}.concatenated.$CHR.annot
echo ${OUT}${NAME}.concatenated.$CHR.annot
