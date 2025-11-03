from scipy.stats import nbinom

# Parameters
r = 3     # number of successes
p = 0.2   # probability of success
x = 5     # number of trials

# Calculate the negative binomial probability
nbinom_prob = nbinom.pmf(x, r, p)
print(f"Negative Binomial distribution probability for x={x}: {nbinom_prob:.4f}")
