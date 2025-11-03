from scipy.stats import norm

# --- CONTEXT & PARAMETERS ---
# The Standard Normal distribution (Z-distribution) is a Normal distribution
# that is centered at 0 and has a spread of 1.

# 1. Mean (mu):
mu = 0       # The center of the Standard Normal curve.

# 2. Standard Deviation (sigma):
sigma = 1    # The spread of the Standard Normal curve.

# 3. X Value (or Z-score):
# This is the point on the horizontal axis (the Z-score) at which we want to find the density.
x = 0.0028      # Value to evaluate (e.g., a calculated Z-score)

# --- CALCULATION ---
# norm.pdf(x, mu, sigma) calculates the height of the probability curve at the point x.
# The PDF formula for the Normal distribution is: f(x) = (1 / (sigma * sqrt(2*pi))) * e^(-0.5 * ((x - mu) / sigma)^2)
# Since mu=0 and sigma=1, this is the Z-table formula.
norm_prob = norm.pdf(x, mu, sigma)

# --- OUTPUT ---
print(f"Standard Normal distribution PDF value (density) for z={x}: {norm_prob:.4f}")