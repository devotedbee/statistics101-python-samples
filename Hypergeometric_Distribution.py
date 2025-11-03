from scipy.stats import hypergeom

# Parameters
M = 30   # total population size
K = 10   # total number of successes in the population
n = 15   # number of draws
x = 5    # number of observed successes

# Calculate the hypergeometric probability
hypergeom_prob = hypergeom.pmf(x, M, K, n)
print(f"Hypergeometric distribution probability for x={x}: {hypergeom_prob:.4f}")
