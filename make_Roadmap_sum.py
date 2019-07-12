import pandas as pd
import argparse

def make_sum(args):
    dic = {
    'DNase':[i for i in range(1,35)],
    'H3K27ac':[i for i in range(35,103)],
    'H3K36me3':[i for i in range(103,191)],
    'H3K4me1':[i for i in range(191,279)],
    'H3K4me3':[i for i in range(279,367)],
    'H3K9ac':[i for i in range(367,397)]}
    annot_folder = args.annot_folder
    chrom = args.chrom
    out_folder = args.out_folder
    for mark in dic:
        print('making '+mark+' sum annotations')
        dfs = [pd.read_csv(annot_folder+'Roadmap.'+str(i)+'.'+chrom+'.annot.gz',delim_whitespace=True) for i in dic[mark]]
        df = pd.concat(dfs,axis=1)
        col_sum = df.sum(axis=1)
        sum_df = pd.DataFrame(col_sum,columns=['ANNOT'])
        sum_df.to_csv(out_folder+'Roadmap.'+mark+'.sum.'+chrom+'.annot.gz',sep='\t',index=False,compression='gzip')
    return
        

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--annot-folder',help='folder containing all relevant annotations')
    parser.add_argument('--chrom',help='which chromosome')
    parser.add_argument('--out-folder')
    args = parser.parse_args()
    
    make_sum(args)
