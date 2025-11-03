import numpy as np
from scipy.stats import norm

# --- BINOMIAL PARAMETERS ---
# Context: We have 46 independent trials (n) where the probability of success (p) is 0.6.
# Example: A quality control check on 46 items, each having a 60% chance of passing.
n = 46  # Total number of trials
p = 0.6 # Probability of success

# 1. Calculate the Mean (mu) and Standard Deviation (sigma)
# These are the *expected* values for the underlying Binomial distribution.
# Mean (mu): Expected number of successes (E[X] = n * p)
mu = n * p
# Standard Deviation (sigma): Measure of spread (SD[X] = sqrt(n * p * (1 - p)))
sigma = np.sqrt(n * p * (1 - p))

# --- NORMAL DISTRIBUTION CALCULATION (for approximation demonstration) ---
# Check Condition: For the approximation to be valid, n*p and n*(1-p) must both be >= 10.
# Here, n*p = 27.6 and n*(1-p) = 18.4. Both are >= 10, so the approximation is appropriate.

# x_approx represents a value on the continuous Normal curve.
x_approx = 36  # This point (36) is for demonstration only. In practice, you use the Continuity Correction Factor (CCF) here.

# Calculate the normal probability density function (PDF) value at x_approx
# PDF is the HEIGHT of the bell curve at this point, NOT the probability P(X=x).
# We use the calculated Binomial mu and sigma as the parameters for the Normal curve.
norm_prob = norm.pdf(x_approx, mu, sigma)

# --- OUTPUT ---
print(f"Binomial Sample Size (n): {n}")
print(f"Success Probability (p): {p}")
print("-" * 35)
print(f"Binomial Mean (mu): {mu:.4f} (Expected number of successes)")
print(f"Binomial Standard Deviation (sigma): {sigma:.4f} (Spread of the outcomes)")
print("-" * 35)
print(f"Normal distribution PDF value (Density) at x={x_approx}: {norm_prob:.4f}")