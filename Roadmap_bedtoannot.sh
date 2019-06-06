#!/bin/bash

python make_annot_batch.py \
    --input-folder $1 \
    --output-folder $2 \
    --file-type bed \
    --bfile $3
