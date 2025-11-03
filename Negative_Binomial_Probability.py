from scipy.stats import nbinom

# --- CONTEXT & PARAMETERS ---
# Imagine a salesperson has a 20% chance (p=0.2) of closing a sale (success).
# We want to find the probability that their 3rd successful sale (r=3) occurs on their 5th client visit (x=5).
# Note: The failures before the r-th success is k = x - r = 5 - 3 = 2.

# 1. Number of Successes (r):
r = 3     # The fixed number of successes required to stop the process.

# 2. Probability of Success (p):
p = 0.2   # The probability of success on a single, independent trial.

# 3. Number of Trials (x):
x = 5     # The specific trial number on which the r-th success occurs.
# Note: scipy's nbinom.pmf requires 'x' to be the total number of trials (x_total).

# --- CALCULATION ---
# nbinom.pmf(x_total - r, r, p) is often the function signature, where the first argument
# is the number of failures (k = x_total - r).
# HOWEVER, the 'scipy.stats' documentation for nbinom.pmf (since version 0.17) uses the
# total number of trials (x_total) as the first argument, which aligns with the common
# definition where X is the total number of trials.
# The formula is: P(X=x) = (x-1 choose r-1) * p^r * (1-p)^(x-r)
nbinom_prob = nbinom.pmf(x, r, p)

# --- OUTPUT ---
print(f"Negative Binomial distribution PMF for x={x} (P(X={x})): {nbinom_prob:.4f}")