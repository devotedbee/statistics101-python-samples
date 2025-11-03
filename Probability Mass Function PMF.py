from scipy.stats import binom

# Parameters
n = 57  # number of trials
p = 0.4 # probability of success
x = 22  # number of successes

# Calculate the binomial probability (PMF)
binom_prob = binom.pmf(x, n, p)
print(f"Binomial PMF for x={x}: {binom_prob:.4f}")
