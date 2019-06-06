import pandas as pd

cols = ['DNase.union','DNase.sum','H3K4me1.union','H3K4me1.sum','H3K4me3.union','H3K4me3.sum','H3K9ac.union','H3K9ac.sum','H3K27ac.union','H3K27ac.sum','H3K36me3.union','H3K36me3.sum']
fnames = ['DNase.all','DNase.sum','H3K4me1.all','H3K4me1.sum','H3K4me3.all','H3K4me3.sum','H3K9ac.all','H3K9ac.sum','H3K27ac.all','H3K27ac.sum','H3K36me3.all','H3K36me3.sum']

for i in range(1,23):
    chrom = str(i)
    print('concatenating chromosome '+chrom)
    dfs = []
    for s in fnames:
        print('reading in file '+s+'.'+chrom+'.annot.gz')
        dfs.append(pd.read_csv('/n/groups/price/ran/high-dim-sldsc/real_pheno_pipeline/annotations/UK10K/Roadmap/Roadmap.'+s+'.'+chrom+'.annot.gz', delim_whitespace=True))
    df = pd.concat(dfs,axis=1)
    df.columns=cols
    df.to_csv('/n/groups/price/ran/high-dim-sldsc/real_pheno_pipeline/annotations/UK10K/Roadmap/Roadmap.control.'+chrom+'.annot.gz',sep='\t',index=False,compression='gzip')
