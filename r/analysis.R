library(markovchain)

transition_matrix <- as.matrix(read.csv("output/transition_matrix.csv", header = FALSE))

states <- c("WIN", "LOSS", "DRAW")
rownames(transition_matrix) <- states
colnames(transition_matrix) <- states

mc <- new("markovchain", states = states, transitionMatrix = transition_matrix, name = "Player Results")

print(mc)

cat("Is irreducible? ", is.irreducible(mc), "\n")

cat("Is regular? ", is.regular(mc), "\n")

cat("Stationary distribution:\n")
print(steadyStates(mc))

dir.create("output/plots", recursive = TRUE, showWarnings = FALSE)

png("output/plots/markov_chain.png", width = 800, height = 600)

plot(mc, edge.arrow.size = 0.5)

dev.off()

