#Hay que ejeutar Rscript --vanilla DIRECTORIO ÁRBOL
#Para cargar los nombres de los nodos que se corresponden con la salida
#de iqtree2 asr (state), hay que leer el archivo treefile (es el árbol 
#definitivo de iqtree -asr, y el nombre aparece en el campo label)

library(ape)
library(dplyr)
library(treeio)

args = commandArgs(trailingOnly = TRUE)

MYPATH <- args[1]
setwd(MYPATH)

MYTREE <- args[2]
random100_ANC <- ape::read.tree(MYTREE)
#random100_ANC <- ape::read.tree("~/comp/DatasetGlobalMTB/random100_short/iq_tree_anc_asr.treefile")
random100_ANC_t <- as_tibble(random100_ANC)
#load sampletest (subset4) for testing getmutinnodes.py
#random100_ANC <- ape::read.tree("iqtree_anc/sampletest/subset4contree_asr.treefile")
#random100_ANC_t <- as_tibble(random100_ANC)
##

mut_table <- random100_ANC_t[,c(1,2,4)]
mut_table$labparent <- random100_ANC_t[random100_ANC_t$node[random100_ANC_t$parent],4]
colnames(mut_table) <- c("parent","node","labnode","labparent")
write.csv(as.matrix(mut_table),paste0(MYPATH,"nodeparent.csv"), quote = FALSE,row.names = FALSE)
# write.csv(as.matrix(mut_table),"iqtree_anc/sampletest/nodeparent.csv", quote = FALSE,
#          row.names = FALSE)