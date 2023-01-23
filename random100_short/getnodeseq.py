#!/usr/bin/python

import argparse
import sys
#import numpy as np

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--state',help=".state file from iqtree_anc containing"
                        "internal nodes sequences, WITHOUT header and columnames" ,required=True)
    parser.set_defaults()
    args = parser.parse_args()

    print(args)

    tableiqtree = open(args.state,'r')
    node = []
    myseq = []
    new_fasta = []
    #codenucl = ["A","C","G","T"] #what if parent should be -?
    for line in tableiqtree:
        if '#' in line:
            continue
        elif 'Node\t' in line:
            continue
        elif line.split()[0] == node:
            #x = np.array(line.split()[3:7])
            #prob = x.astype(float)
            #myidx = np.argmax(prob)
            x = line.split("\t")[2]
            if x == "-":
                myseq.append("N")
            else:
                myseq.append(x)
            #myseq.append(codenucl[myidx])
        else:
            myseq=''.join(myseq)
            new_fasta.append('>%s\n%s' % (node, myseq))
            with open('nodeseqs.fasta', 'w') as f:
                f.write('\n'.join(new_fasta))
            node = line.split()[0]
            myseq = []
            myseq.append(line.split('\t')[2])
    
    myseq=''.join(myseq)
    new_fasta.append('>%s\n%s' % (node, myseq))
    with open('nodeseqs.fasta', 'w') as f:
                f.write('\n'.join(new_fasta))


if __name__ == "__main__":
    main()
