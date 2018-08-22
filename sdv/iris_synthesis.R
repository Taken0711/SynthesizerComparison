library(synthpop)

ods <- read.csv("iris.data", 
                 header = TRUE,
                 sep = ",")
synthesis <- syn(ods)
sds = synthesis$syn

write.csv(sds, file = "iris_syn.data", row.names=FALSE, quote = FALSE)

