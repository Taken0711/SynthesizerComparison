library(synthpop)

ods <- read.csv("abalone.data", 
                 header = TRUE,
                 sep = ",")
synthesis <- syn(ods)
sds = synthesis$syn

write.csv(sds, file = "abalone_syn.data", row.names=FALSE, quote = FALSE)


