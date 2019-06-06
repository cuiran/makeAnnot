#!/bin/bash

python make_annot.py \
    --bed-file $1 \
    --bfile-chr $2 \
    --chrom $3 \
    --prefix $4
