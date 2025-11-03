from scipy.stats import binom

# --- CONTEXT & PARAMETERS (Using n=46, p=0.6 from a previous context) ---
# Example: A quality control check on n=46 items, each having a 60% chance (p=0.6) of passing.
# We want to find the 95th percentile, X_0.95.

n = 46     # Total number of trials
p = 0.6    # Probability of success
quantile = 0.95  # The target cumulative probability (95th percentile)

# --- CALCULATION ---
# binom.ppf(quantile, n, p) finds the smallest integer x such that P(X <= x) >= quantile.
# This means, "What is the minimum number of successes (x) needed to be in the top 5% (or bottom 95%)?"
binom_ppf = binom.ppf(quantile, n, p)

# --- OUTPUT ---
print(f"95th percentile (X_0.95) for Binomial: {binom_ppf:.0f}")