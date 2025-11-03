import numpy as np
from scipy.stats import norm

# --- BINOMIAL PARAMETERS ---
n = 46
p = 0.6

# 1. Calculate the Mean (mu) and Standard Deviation (sigma)
mu = n * p
sigma = np.sqrt(n * p * (1 - p))

# --- NORMAL DISTRIBUTION CALCULATION (for approximation) ---
# Note: The parameters mu and sigma are now calculated above.
# x will be used with continuity correction for a proper approximation
# For demonstration, we'll use a single point x=12.5 (the upper bound for P(X=12))

# FIX APPLIED: Retyped this line to remove the invalid characters.
x_approx = 36  # Using the upper continuity correction bound for the previous problem (X=12 -> 11.5 to 12.5)

# Calculate the normal probability (PDF value at x_approx)
# For approximating P(X=12), you'd typically use the CDF (as shown in the previous calculation),
# but this script calculates the PDF, which is the height of the curve at a point.
norm_prob = norm.pdf(x_approx, mu, sigma)

print(f"Binomial Mean (mu): {mu:.4f}")
print(f"Binomial Standard Deviation (sigma): {sigma:.4f}")
print("-" * 35)
print(f"Normal distribution PDF value at x={x_approx}: {norm_prob:.4f}")