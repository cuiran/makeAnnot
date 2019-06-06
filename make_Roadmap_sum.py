import pandas as pd
import argparse

# make Roadmap.DNase.sum.bed
def DNase(args):
    print('making DNase sum annotations')
    annot_folder = args.annot_folder
    chrom = args.chrom
    # DNase: Roadmap.1 - Roadmap.34
    # assuming they are thin annotations
    dfs = [pd.read_csv(annot_folder+'Roadmap.'+str(i)+'.'+chrom+'.annot.gz',delim_whitespace=True) for i in range(1,35)]
    df = pd.concat(dfs,axis=1)
    col_sum = df.sum(axis=1)
    sum_df = pd.DataFrame(col_sum,columns=['ANNOT'])
    sum_df.to_csv(annot_folder+'Roadmap.DNase.sum.'+chrom+'.annot.gz',sep='\t',index=False,compression='gzip')
    return

def H3K27ac(args):
    print('making H3K27ac sum annotations')
    annot_folder = args.annot_folder
    chrom = args.chrom
    # H3K27ac: Roadmap.35 - Roadmap.102
    dfs = [pd.read_csv(annot_folder+'Roadmap.'+str(i)+'.'+chrom+'.annot.gz',delim_whitespace=True) for i in range(35,103)]
    df = pd.concat(dfs,axis=1)
    col_sum = df.sum(axis=1)
    sum_df = pd.DataFrame(col_sum,columns=['ANNOT'])
    sum_df.to_csv(annot_folder+'Roadmap.H3K27ac.sum.'+chrom+'.annot.gz',sep='\t',index=False,compression='gzip')
    return

def H3K36me3(args):
    print('making H3K36me3 sum annotations')
    annot_folder = args.annot_folder
    chrom = args.chrom
    # H3K36me3: Roadmap.103 - Roadmap.190
    dfs = [pd.read_csv(annot_folder+'Roadmap.'+str(i)+'.'+chrom+'.annot.gz',delim_whitespace=True) for i in range(103,191)]
    df = pd.concat(dfs,axis=1)
    col_sum = df.sum(axis=1)
    sum_df = pd.DataFrame(col_sum,columns=['ANNOT'])
    sum_df.to_csv(annot_folder+'Roadmap.H3K36me3.sum.'+chrom+'.annot.gz',sep='\t',index=False,compression='gzip')
    return

def H3K4me1(args):
    print('making H3K4me1 sum annotations')
    annot_folder = args.annot_folder
    chrom = args.chrom
    # H3K4me1: Roadmap.191 - Roadmap.278
    dfs = [pd.read_csv(annot_folder+'Roadmap.'+str(i)+'.'+chrom+'.annot.gz',delim_whitespace=True) for i in range(191,279)]
    df = pd.concat(dfs,axis=1)
    col_sum = df.sum(axis=1)
    sum_df = pd.DataFrame(col_sum,columns=['ANNOT'])
    sum_df.to_csv(annot_folder+'Roadmap.H3K4me1.sum.'+chrom+'.annot.gz',sep='\t',index=False,compression='gzip')
    return

def H3K4me3(args):
    print('making H3K4me3 sum annotations')
    annot_folder = args.annot_folder
    chrom = args.chrom
    # H3K4me3: Roadmap.279 - Roadmap.366
    dfs = [pd.read_csv(annot_folder+'Roadmap.'+str(i)+'.'+chrom+'.annot.gz',delim_whitespace=True) for i in range(279,367)]
    df = pd.concat(dfs,axis=1)
    col_sum = df.sum(axis=1)
    sum_df = pd.DataFrame(col_sum,columns=['ANNOT'])
    sum_df.to_csv(annot_folder+'Roadmap.H3K4me3.sum.'+chrom+'.annot.gz',sep='\t',index=False,compression='gzip')
    return

def H3K9ac(args):
    print('making H3K9ac sum annotations')
    annot_folder = args.annot_folder
    chrom = args.chrom
    # H3K9ac: Roadmap.367 - Roadmap.396
    dfs = [pd.read_csv(annot_folder+'Roadmap.'+str(i)+'.'+chrom+'.annot.gz',delim_whitespace=True) for i in range(367,397)]
    df = pd.concat(dfs,axis=1)
    col_sum = df.sum(axis=1)
    sum_df = pd.DataFrame(col_sum,columns=['ANNOT'])
    sum_df.to_csv(annot_folder+'Roadmap.H3K9ac.sum.'+chrom+'.annot.gz',sep='\t',index=False,compression='gzip')
    return


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--annot-folder',help='folder containing all relevant annotations')
    parser.add_argument('--chrom',help='which chromosome')
    args = parser.parse_args()
 
    DNase(args)
    H3K27ac(args)
    H3K36me3(args)
    H3K4me1(args)
    H3K4me3(args)
    H3K9ac(args)
