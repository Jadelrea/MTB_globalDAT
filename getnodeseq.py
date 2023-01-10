#!/usr/bin/python

from Bio import SeqIO
import argparse
import numpy as np

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--state', required=True)
    parser.set_defaults()
    args = parser.parse_args()

    print(args)

    tableiqtree = open(args.state,'r')
    node = []
    myseq = []
    new_fasta = []
    codenucl = ["A","C","G","T"]
    for line in tableiqtree:
        if line.split()[0] == node:
            x = np.array(line.split()[3:7])
            prob = x.astype(float)
            myidx = np.argmax(prob)
            myseq.append(codenucl[myidx])
        else:
            myseq=''.join(myseq)
            new_fasta.append('>%s\n%s' % (node, myseq))
            with open('nodeseqs.fasta', 'w') as f:
                f.write('\n'.join(new_fasta))
            node = line.split()[0]
            myseq = []
    myseq=''.join(myseq)
    new_fasta.append('>%s\n%s' % (node, myseq))
    with open('nodeseqs.fasta', 'w') as f:
                f.write('\n'.join(new_fasta))

if __name__ == "__main__":
    main()
