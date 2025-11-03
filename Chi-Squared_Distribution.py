from scipy.stats import chi2

# --- CONTEXT & PARAMETERS ---
# The Chi-Squared distribution is primarily used in hypothesis testing (e.g., goodness-of-fit, independence)
# and for constructing confidence intervals for population variance.

# 1. Degrees of Freedom (df):
# This parameter defines the shape of the Chi-Squared distribution. It's typically
# determined by the sample size or the number of categories in the statistical test.
degrees_of_freedom = 5 # df = 5 (e.g., analyzing 6 categories in a goodness-of-fit test, df = 6 - 1)

# 2. X Value:
# This is the point on the horizontal axis where we want to find the height of the curve (the density).
x = 10              # x value (e.g., a calculated test statistic value like X^2 = 10)

# --- CALCULATION ---
# chi2.pdf(x, df) calculates the height of the probability curve at the point x.
# This value itself is NOT the probability of x, but the DENSITY at x.
chi2_prob = chi2.pdf(x, degrees_of_freedom)

# --- OUTPUT ---
print(f"Chi-squared distribution PDF value (density) for x={x} and df={degrees_of_freedom}: {chi2_prob:.4f}")