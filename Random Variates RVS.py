from scipy.stats import binom

# --- CONTEXT & PARAMETERS (Using n=57, p=0.4 from a previous context) ---
# Example: Simulating the outcome of 10 independent clinical trials, where each trial has
# n=57 patients and a drug success rate of p=0.4.

n = 57      # Total number of trials (number of patients in one clinical trial)
p = 0.4     # Probability of success (drug success rate)
size = 10   # The number of random outcomes (simulations) to generate

# --- CALCULATION ---
# binom.rvs(n, p, size=k) generates 'k' random numbers, where each number represents
# the total number of successes observed in a single set of 'n' trials.
samples = binom.rvs(n, p, size=size)

# --- OUTPUT ---
print(f"Number of simulations generated: {size}")
print(f"Random samples from Binomial distribution (n={n}, p={p}):")
print(samples)