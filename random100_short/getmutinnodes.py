import subprocess
from Bio import SeqIO
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tipseq',help="multifasta of aligned samples in tree",required=True)
    parser.set_defaults()
    args = parser.parse_args()

    print(args)

    #nodeparent.csv is an R output from getnodeparent.R. It is further modified by removing colnames manually.
    with open('nodeparent.csv','r') as fnd:
        for line in fnd:
            Rnode = line.split(',')[1]
            tnode = line.split(',')[2]
            tparent = line.split(',')[3]
            with open('ids.txt','w') as id:
                id.write(tnode + "\n" + tparent)
            fparlign = open("paralign.fa","w")
            subprocess.call(["seqtk","subseq",args.tipseq,"ids.txt"], stdout=fparlign)
            fparlign.close()
            fparlign = open("paralign.fa","a")
            subprocess.call(["seqtk","subseq","nodeseqs.fasta","ids.txt"], stdout=fparlign)
            fparlign.close()
            fin = open('paralign.fa','r')
            seq_records = SeqIO.parse(fin, 'fasta')
            refseq_record = next(seq_records)
            mymut = []
            for record in seq_records:
                mutnr = 0
                for i in range(0, len(record)):
                    pos1 = refseq_record[i]
                    pos2 = record[i]
                    if pos1 != pos2:
                        mymut.append(pos2+str(i)+pos1)
                        mutnr = mutnr + 1
            fin.close()
            with open('node_mut.csv','a') as fout:
                fout.write(Rnode + ";" + str(mutnr) + ";" + str(mymut) + "\n")
        
        subprocess.call(["rm", "paralign.fa"])
        subprocess.call(["rm", "ids.txt"])

if __name__ == "__main__":
    main()
