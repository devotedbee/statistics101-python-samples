import numpy as np # Imported but not used in this specific example
from scipy.stats import norm

# --- CONTEXT & PARAMETERS ---
# Imagine a cookie company finds that the number of chocolate chips per bag is normally distributed.
# The average number of chips (mean) is 1252.
# The variability (standard deviation) is 129 chips.

# Parameters for the Normal Distribution N(mu, sigma):
mean = 1252    # mu (μ): The center of the distribution (average number of chips)
std_dev = 129  # sigma (σ): The spread or variability of the distribution

# --- CALCULATION OF PROBABILITIES (Areas Under the Curve) ---

# 1. Probability of a bag containing between 1100 and 1500 chocolate chips
# Logic: P(1100 < X < 1500) = CDF(1500) - CDF(1100)
# We calculate the area from the mean up to 1500, and subtract the area from the mean up to 1100.
prob_between = norm.cdf(1500, mean, std_dev) - norm.cdf(1100, mean, std_dev)
print(f"Probability of having between 1100 and 1500 chips: {prob_between:.4f}")

# 2. Probability of a bag containing fewer than 1050 chocolate chips
# Logic: P(X < 1050) = CDF(1050)
# The Cumulative Distribution Function (CDF) always returns the area to the LEFT of the given x-value.
prob_less_than_1050 = norm.cdf(1050, mean, std_dev)
print(f"Probability of having less than 1050 chips: {prob_less_than_1050:.4f}")

# 3. Proportion of bags containing more than 1175 chocolate chips
# Logic: P(X > 1175) = 1 - CDF(1175)
# Since the total area under the curve is 1, we subtract the area to the left of 1175 from 1.
prob_more_than_1175 = 1 - norm.cdf(1175, mean, std_dev)
print(f"Proportion of bags with more than 1175 chips: {prob_more_than_1175:.4f}")

# 4. Percentile rank of a bag containing 1000 chocolate chips
# Logic: Percentile = CDF(x) * 100
# The percentile rank is the percentage of data points that fall below the given score (x).
percentile_rank = norm.cdf(1000, mean, std_dev) * 100
print(f"Percentile rank of 1000 chips: {percentile_rank:.2f}%")