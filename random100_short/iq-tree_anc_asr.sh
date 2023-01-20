#!/usr/bin/

nice -n 5 iqtree -s run_alignment_no_resis_no_clus.fas \
            -te iq_tree.contree -T AUTO --threads-max 3 \
            --prefix iq_tree_anc_asr -asr -m GTR