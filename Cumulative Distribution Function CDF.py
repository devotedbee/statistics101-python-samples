from scipy.stats import binom

# --- CONTEXT & PARAMETERS ---
# Imagine a scenario where a politician has a 60% approval rating (p).
# We survey n=15 people and want to know the probability that x=10 or fewer approve.

# Parameters for the Binomial Distribution B(n, p):
n = 15   # Total number of independent trials (e.g., sample size)
p = 0.6  # Probability of success on a single trial (e.g., approval rating)
x = 10   # Maximum number of successes we are interested in (i.e., x or fewer)

# --- CALCULATION ---
# binom.cdf(x, n, p) calculates P(X <= x).
# This is the sum of all individual PMF probabilities from 0 up to x:
# P(X <= x) = P(X=0) + P(X=1) + ... + P(X=x)
binom_cdf = binom.cdf(x, n, p)

# --- OUTPUT ---
print(f"Binomial CDF for x={x} (P(X <= {x})): {binom_cdf:.4f}")
# In context: The probability that 10 or fewer people approve out of 15 is 0.9095.