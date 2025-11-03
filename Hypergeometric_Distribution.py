from scipy.stats import hypergeom

# --- CONTEXT & PARAMETERS ---
# Imagine a box of M=30 electronic components, where K=10 are known to be defective.
# We randomly select a sample of n=15 components without putting them back.
# We want to find the probability that exactly x=5 of the 15 drawn components are defective.

# 1. Total Population Size (M):
M = 30   # Total number of items in the population (e.g., total components in the box)

# 2. Total Successes in Population (K):
K = 10   # Total number of items in the population that are 'successes' (e.g., defective components)

# 3. Sample Size (n):
n = 15   # Number of items drawn without replacement (e.g., sample size)

# 4. Observed Successes (x):
x = 5    # The specific number of successes we want to observe in the sample (e.g., exactly 5 defective components)

# --- CALCULATION ---
# hypergeom.pmf(x, M, K, n) calculates P(X = x).
# The formula is based on combinations:
# P(X=x) = [ (K choose x) * ((M-K) choose (n-x)) ] / (M choose n)
hypergeom_prob = hypergeom.pmf(x, M, K, n)

# --- OUTPUT ---
print(f"Hypergeometric distribution PMF for x={x} (P(X={x})): {hypergeom_prob:.4f}")