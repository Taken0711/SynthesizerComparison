library(synthpop)

ods <- read.csv("categorized_abalone.data", 
                 header = TRUE,
                 sep = ",")
synthesis <- syn(ods)
sds = synthesis$syn

write.csv(sds, file = "categorized_abalone_syn.data", row.names=FALSE, quote = FALSE)


