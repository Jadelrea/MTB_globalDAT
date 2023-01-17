SNP_pos <- read.csv("~/comp/DatasetGlobalMTB/random100_short/SNP_pos.txt",
                    sep="")

alignpos <- seq(1:length(SNP_pos$Position))

conversion <- cbind(alignpos, SNP_pos)


write.table(conversion,"./conversion.txt",sep="\t",col.names = FALSE, row.names = FALSE)
