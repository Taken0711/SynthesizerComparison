# Classification Tree with rpart
library(ggplot2)
library(ggpubr)

df <- read.csv("categorized_abalone.data", 
               header = TRUE,
               sep = ",")

sds <- read.csv("categorized_abalone_syn.data", 
                header = TRUE,
                sep = ",")

df$set = rep("observed", nrow(df))
sds$set = rep("synthetised", nrow(sds))
all = rbind(df, sds)

p1 <- ggplot(all, aes(x=Sex, fill=set)) +
  geom_histogram(binwidth=.5, position="dodge", stat="count")
p2 <- ggplot(all, aes(x=Length, colour=set)) +
  geom_density()
p3 <- ggplot(all, aes(x=Diameter, colour=set)) +
  geom_density()
p4 <- ggplot(all, aes(x=Height, colour=set)) +
  geom_density()
p5 <- ggplot(all, aes(x=Whole.weight, colour=set)) +
  geom_density()
p6 <- ggplot(all, aes(x=Shucked.weight, colour=set)) +
  geom_density()
p7 <- ggplot(all, aes(x=Viscera.weight, colour=set)) +
  geom_density()
p8 <- ggplot(all, aes(x=Shell.weight, colour=set)) +
  geom_density()
p9 <- ggplot(all, aes(x=Rings, fill=set)) +
  geom_histogram(binwidth=.5, position="dodge", stat="count")
ggarrange(p1, p2, p3, p4, p5, p6, p7, p8, p9)

readline("Press <return to continue")

p1 <- ggplot(all, aes(x=Sex, fill=set)) +
  geom_histogram(binwidth=.5, position="dodge", stat="count") + 
  facet_wrap(~Rings)
p2 <- ggplot(all, aes(x=Length, colour=set)) +
  geom_density() + 
  facet_wrap(~Rings)
p3 <- ggplot(all, aes(x=Diameter, colour=set)) +
  geom_density() + 
  facet_wrap(~Rings)
p4 <- ggplot(all, aes(x=Height, colour=set)) +
  geom_density() + 
  facet_wrap(~Rings)
p5 <- ggplot(all, aes(x=Whole.weight, colour=set)) +
  geom_density() + 
  facet_wrap(~Rings)
p6 <- ggplot(all, aes(x=Shucked.weight, colour=set)) +
  geom_density() + 
  facet_wrap(~Rings)
p7 <- ggplot(all, aes(x=Viscera.weight, colour=set)) +
  geom_density() + 
  facet_wrap(~Rings)
p8 <- ggplot(all, aes(x=Shell.weight, colour=set)) +
  geom_density() + 
  facet_wrap(~Rings)
ggarrange(p1, p2, p3, p4, p5, p6, p7, p8, ncol = 2, nrow = 4)




