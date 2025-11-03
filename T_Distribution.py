from scipy.stats import t

# --- CONTEXT & PARAMETERS ---
# Imagine performing a hypothesis test on a small sample of data (e.g., n=11).
# We calculate the t-statistic (x) from our sample data.

# 1. Degrees of Freedom (df):
# This defines the shape of the t-distribution. It is typically calculated as df = n - 1.
df = 10             # (e.g., sample size n = 11, so df = 11 - 1 = 10)

# 2. T-Value (x):
# This is the point on the horizontal axis (the calculated t-statistic) where we want to find the density.
x = 1.5             # The calculated t-statistic value

# --- CALCULATION ---
# t.pdf(x, df) calculates the height of the t-distribution curve at the point x.
# This density is higher than the Standard Normal distribution for the same x-value due to the t-distribution's heavier tails.
t_prob = t.pdf(x, df)

# --- OUTPUT ---
print(f"T-distribution PDF value (density) for t={x} and df={df}: {t_prob:.4f}")