import argparse
import pandas as pd
import pdb

def make_control(args):
    cols = ['DNase.union','DNase.sum','H3K4me1.union','H3K4me1.sum','H3K4me3.union','H3K4me3.sum','H3K9ac.union','H3K9ac.sum','H3K27ac.union','H3K27ac.sum','H3K36me3.union','H3K36me3.sum']
    fnames = ['DNase.all','DNase.sum','H3K4me1.all','H3K4me1.sum','H3K4me3.all','H3K4me3.sum','H3K9ac.all','H3K9ac.sum','H3K27ac.all','H3K27ac.sum','H3K36me3.all','H3K36me3.sum']

    chrom = args.chrom
    annot_dir = args.annot_dir
    out_dir = args.out_dir
    print('concatenating chromosome '+chrom)
    dfs = []
    for s in fnames:
        print('reading in file '+s+'.'+chrom+'.annot.gz')
        dfs.append(pd.read_csv(annot_dir+'Roadmap.'+s+'.'+chrom+'.annot.gz', delim_whitespace=True)['ANNOT'])
    sampledf = pd.read_csv(annot_dir+'Roadmap.DNase.all.'+chrom+'.annot.gz',delim_whitespace=True).iloc[:,:4]
    df = pd.concat([sampledf]+dfs,axis=1)
    df.columns=sampledf.columns.tolist()+cols
    df.to_csv(out_dir+'Roadmap.control.'+chrom+'.annot.gz',sep='\t',index=False,compression='gzip')


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--annot-dir')
    parser.add_argument('--chrom',type=str)
    parser.add_argument('--out-dir')
    args = parser.parse_args()

    make_control(args)
