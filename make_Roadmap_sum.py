import pandas as pd
import argparse
import subprocess
import os
import pdb

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
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for mark in dic:
        print('making '+mark+' sum annotations')
        # this is for annotations that are not thinannots
        print('concatenating...')
        subprocess.call([dir_path+'/concat_annots.sh',str(chrom),str(dic[mark][0]),
            str(dic[mark][-1]),
            mark,annot_folder,out_folder])
        df = pd.read_csv(mark+'.annot',delim_whitespace=True)
        print('shape of the concatenated dataframe',df.shape)
        print('summing up columns')
        col_sum = df.sum(axis=1)
        sampledf = pd.read_csv(annot_folder+'Roadmap.1.'+chrom+'.annot.gz',delim_whitespace=True)
        print('shape of sample dataframe',sampledf.shape)
        sumdf = pd.DataFrame(col_sum,columns=['ANNOT'])
        sumdf[['CHR','SNP','CM','BP']] = sampledf[['CHR','SNP','CM','BP']]
        sumdf = sumdf[['CHR','SNP','CM','BP','ANNOT']]
        sumdf.to_csv(out_folder+'Roadmap.'+mark+'.sum.'+chrom+'.annot.gz',sep='\t',index=False,compression='gzip')
    return
        

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--annot-folder',help='folder containing all relevant annotations')
    parser.add_argument('--chrom',help='which chromosome')
    parser.add_argument('--out-folder')
    args = parser.parse_args()
    
    make_sum(args)
