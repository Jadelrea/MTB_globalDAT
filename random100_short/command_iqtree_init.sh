#!/usr/bin/

nice -n 5 iqtree -s run_alignment_no_resis.fas \
    -T AUTO --threads-max 3 -m GTR -B 1000 --prefix iq_tree \
    -fconst 756053,1443410,1438006,755885 
