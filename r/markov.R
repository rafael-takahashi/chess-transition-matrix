library(markovchain)

states <- scan("output/states.txt", what = "", quiet = TRUE)

mc_fit <- markovchainFit(data = states)
mc <- mc_fit$estimate

print(mc)

cat("Is irreducible? ", is.irreducible(mc), "\n")

cat("Is regular? ", is.regular(mc), "\n")

cat("Stationary distribution:\n")
print(steadyStates(mc))

dir.create("output/plots", recursive = TRUE, showWarnings = FALSE)

png("output/plots/markov_chain.png", width = 800, height = 600)

plot(mc, edge.arrow.size = 0.5)

dev.off()