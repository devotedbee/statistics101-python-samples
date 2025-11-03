from scipy.stats import binom

# --- CONTEXT & PARAMETERS ---
# Imagine a new drug has a 40% success rate (p=0.4).
# A clinical trial enrolls n=57 patients.
# We want to find the probability that exactly x=22 patients successfully respond to the drug.

# Parameters for the Binomial Distribution B(n, p):
n = 57  # Total number of independent trials (e.g., sample size, number of patients)
p = 0.4 # Probability of success on a single trial (e.g., success rate of the drug)
x = 22  # Exact number of successes we are interested in (e.g., exactly 22 patients responding)

# --- CALCULATION ---
# binom.pmf(x, n, p) calculates P(X = x).
# This is the formula: P(X=x) = (n choose x) * p^x * (1-p)^(n-x)
binom_prob = binom.pmf(x, n, p)

# --- OUTPUT ---
print(f"Binomial PMF for x={x} (P(X={x})): {binom_prob:.4f}")