#!/bin/bash

CHR=$1
S=$2
E=$3
NAME=$4
DIR=$5
OUT=$6


for ((i=$S;i<=$E;i++)); do
    gunzip ${DIR}Roadmap.$i.$CHR.annot.gz
    cut -f5 ${DIR}Roadmap.$i.$CHR.annot > ${DIR}Roadmap.$i.$CHR.thin.annot
done

paste ${DIR}Roadmap.*.$CHR.thin.annot > ${OUT}${NAME}.concatenated.$CHR.annot
rm ${DIR}Roadmap.*.$CHR.thin.annot
echo ${OUT}${NAME}.concatenated.$CHR.annot


