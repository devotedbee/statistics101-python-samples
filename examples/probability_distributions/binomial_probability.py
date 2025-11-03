"""
# Moved from Binomial_Probability.py
from scipy.stats import binom

# Parameters
n = 30
p = 0.35
x = 20

# Calculate the binomial probability
probability = binom.pmf(x, n, p)

print(f"The probability of observing {x} successes in {n} trials is: {probability:.4f}")
"""