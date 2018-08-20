# Classification Tree with rpart
library(ggplot2)
library(ggpubr)

df <- read.csv("iris.data", 
                 header = TRUE,
                 sep = ",")

sds <- read.csv("iris_syn.data", 
                header = TRUE,
                sep = ",")

df$set = rep("observed", nrow(df))
sds$set = rep("synthetised", nrow(sds))
all = rbind(df, sds)

p1 <- ggplot(all, aes(x=sepal_length, colour=set)) +
  geom_density()
p2 <- ggplot(all, aes(x=sepal_width, colour=set)) +
  geom_density()
p3 <- ggplot(all, aes(x=petal_length, colour=set)) +
  geom_density()
p4 <- ggplot(all, aes(x=petal_width, colour=set)) +
  geom_density()
p5 <- ggplot(all, aes(x=class, fill=set)) +
  geom_histogram(binwidth=.5, position="dodge", stat="count")
ggarrange(p1, p2, p3, p4, p5)

readline("Press <return to continue")

p1 <- ggplot(all, aes(x=sepal_length, colour=set)) +
  geom_density() + 
  facet_wrap(~class)
p2 <- ggplot(all, aes(x=sepal_width, colour=set)) +
  geom_density() + 
  facet_wrap(~class)
p3 <- ggplot(all, aes(x=petal_length, colour=set)) +
  geom_density() + 
  facet_wrap(~class)
p4 <- ggplot(all, aes(x=petal_width, colour=set)) +
  geom_density() + 
  facet_wrap(~class)
ggarrange(p1, p2, p3, p4)



