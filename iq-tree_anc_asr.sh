#!/usr/bin/

nice -n 5 iqtree -s ../randomseqs_treemm.fasta \
            -te iq_tree.contree -T AUTO --threads-max 3 \
            --prefix iq_tree_anc_asr -asr -m GTR