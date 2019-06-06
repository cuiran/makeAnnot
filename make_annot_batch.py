import argparse
import os
from subprocess import Popen,PIPE,call

def batch_convert(args):
    in_folder = args.input_folder
    out_folder = args.output_folder
    ftype = args.file_type
    bfile = args.bfile

    files = list_files(ftype,in_folder)
    for f in files:
        in_file = in_folder+f
        if args.chr_sep:
            chrom = f.split('.')[-2]
            out_prefix = out_folder+'.'.join(f.split('.')[:-2])
            make_annot_single(ftype,in_file,bfile,chrom,out_prefix,args.replace)
        else:
            for i in range(1,23):
                chrom = str(i)
                out_prefix = out_folder+'.'.join(f.split('.')[:-1])
                make_annot_single(ftype,in_file,bfile,chrom,out_prefix,args.replace)
    return

def make_annot_single(ftype,in_file,bfile,chrom,out_prefix,replace):
    if annot_exists(out_prefix,chrom) and not replace:
        print('annotation file '+out_prefix+'.'+chrom+'.annot.gz exists')
    else:
        if ftype == 'bed':
            print('converting bed file '+in_file+' to annotation file')
            cmd = ['sbatch -p short -t 0-12:00 --mem=240000 -o '+out_prefix+'.%N_%j.out -e '+out_prefix+'.%N_%j.err',
            'bed_to_annot.sh',in_file,bfile,chrom,out_prefix]
            call(' '.join(cmd),shell=True)
        elif ftype == 'GeneSet':
            print('converting GeneSet file '+in_file+' to annotation file')
            cmd = ['sbatch -p short -t 0-12:00 --mem=10000 -o '+out_prefix+'.%N_%j.out -e '+out_prefix+'.%N_%j.err',
            'geneset_to_annot.sh',in_file,bfile,chrom,out_prefix]
            call(' '.join(cmd),shell=True)
        elif ftype == 'snp-list':
            print('has not been implemented yet')
    return

def annot_exists(out_prefix,chrom):
    fname = out_prefix+'.'+chrom+'.annot.gz'
    return os.path.isfile(fname)

def list_files(ftype,folder):
    # list all files in folder with suffix ftype
    f = []
    for (dirpath, dirnames, filenames) in os.walk(folder):
        f.extend(filenames)
        break
    files = [s for s in f if s.endswith(ftype)]
    return files

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file-type', help='three choices for input: bed, GeneSet, snp-list')
    parser.add_argument('--input-folder', help='folder directory that contains all the preprocessed files')
    parser.add_argument('--output-folder', help='folder directory where you want the output annot.gz files')
    parser.add_argument('--bfile', help='plink file prefix')
    parser.add_argument('--chr-sep', action='store_true', help='indicate if input files are chromosome separated')
    parser.add_argument('--replace', action='store_true', help='skip checking if the annotation file already exists, re-compute everything')
    args = parser.parse_args()

    batch_convert(args)
