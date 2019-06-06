#!/bin/bash 

python make_annot.py \
    --geneset-file $1 \
    --bfile-chr $2 \
    --chrom $3 \
    --prefix $4 \
    --gene-coord-file /n/groups/price/ran/high-dim-sldsc/real_pheno_pipeline/ref_files/ENSG_gene_annot.txt \
    --gene-col-name ENSGID
