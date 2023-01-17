1. Alignment, SNP_table, SNP_pos and invarseq.sum.txt were copied from salas:/data/dataset_Global_Javi/test_sample

2. Run first ML tree with iqtree with command_iqtree_init.sh

3. Get ancestral sequences with iq-tree_anc_asr.sh

4. I generated conversion.txt with get_conversion.R and SNP_pos.txt

5. Run muttui: MutTui run -a run_alignment_no_resis.fas -t iq_tree_anc_asr.treefile -r MTB_ancestor_reference.fasta -c conversion.txt -o muttui_out
