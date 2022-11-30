library(igraph)
library(arcdiagram)

data(package = "networkdata")

library("networkdata")
arc<-networkdata::movie_576
arc
m <- madmen[1:nrow(madmen) %% 2 == 1, ]
g <- graph.data.frame(m, directed=FALSE)

typeof(arc)
length(arc)
plot.igraph(arc)
arcplot(arc)
??arcplot
g <- graph.data.frame(arc, directed=FALSE)
arcplot(as_edgelist(arc), show.nodes = TRUE, show.labels = TRUE,
        lwd.arcs=4*runif(10,.5,2), col.arcs=hsv(runif(9,0.5,0.9),alpha=0.4),
        col.nodes = "red", main = "Relationships in Reservoir Dogs",
        col.main = "navy")
