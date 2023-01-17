1. Alignment, SNP_table, SNP_pos and invarseq.sum.txt were copied from salas:/data/dataset_Global_Javi/test_sample

2. Run first ML tree with iqtree with command_iqtree_init.sh

3. Get ancestral sequences with iq-tree_anc_asr.sh

4. I generated conversion.txt with get_conversion.R and SNP_pos.txt

5a. Run muttui: MutTui run -a run_alignment_no_resis.fas -t iq_tree_anc_asr.treefile -r MTB_ancestor_reference.fasta -c conversion.txt -o muttui_out
  Res: MutTui uses treetime for ancestral reconstruction (it won't work for my large dataset).
      Also, script error comes out.
 
5b. Alternatively, I made some custom scripts for annotate the trees with mutations and metadata.
    i. Obtain sequences of internal nodes of iq_tree_anc_asr.treetime file from getnodeseq.py, which uses iq_tree_anc_asr.state (modified) file
    ii. Nodes of .treefile is not the same as nodes of .state, but they can be related with the script getnodeparent.R, which outputs table nodeparent.csv
    iii. Mutations of every tip and internal node is obtained with getmutinnodes.py, and saved to node_mut.csv, together with the total number of mutations of each node.
    iv. This can be loaded to annotate_tree.R. There, it can also be combined with metadata such as predicted resistance, lineage or sampling country
