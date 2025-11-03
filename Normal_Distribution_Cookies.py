import numpy as np
from scipy.stats import norm

# Parameters
mean = 1252
std_dev = 129

# Probability of a bag containing between 1100 and 1400 chocolate chips
prob_between = norm.cdf(1500, mean, std_dev) - norm.cdf(1100, mean, std_dev)
print(f"Probability of having between 1500 and 1100 chips: {prob_between:.4f}")

# Probability of a bag containing fewer than 1050 chocolate chips
prob_less_than_1050 = norm.cdf(1050, mean, std_dev)
print(f"Probability of having less than 1050 chips: {prob_less_than_1050:.4f}")

# Proportion of bags containing more than 1175 chocolate chips
prob_more_than_1175 = 1 - norm.cdf(1175, mean, std_dev)
print(f"Proportion of bags with more than 1175 chips: {prob_more_than_1175:.4f}")

# Percentile rank of a bag containing 1000 chocolate chips
percentile_rank = norm.cdf(1000, mean, std_dev) * 100
print(f"Percentile rank of 1000 chips: {percentile_rank:.2f}%")
