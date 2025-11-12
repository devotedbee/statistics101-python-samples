import numpy as np
from scipy.stats import norm # Import the norm object for Z-score and probability functions

# --- POPULATION & SAMPLING CONTEXT ---
# Context: We are assuming a large population with a known mean and standard deviation.
# We are examining the distribution of means (the sampling distribution) that would result
# from drawing repeated samples of size n=36 from this population.

# --- POPULATION PARAMETERS ---
mu = 89 # Population mean 'μ' (The center of the population distribution)
sigma = 18 # Population standard deviation 'σ' (The variability of individuals in the population)
n = 36 # Sample size 'n' (The number of observations in each sample)

# --- CENTRAL LIMIT THEOREM CALCULATIONS ---
# The CLT states that the sampling distribution of the mean will be approximately normal
# since n=36 is > 30.

# 1. Mean of the Sample Distribution (μₓ)
# According to the CLT, the mean of the sample means is always equal to the population mean.
mu_x = mu

# 2. Standard Error (σₓ)
# This measures the variability of the sample means around the population mean.
# It is calculated as: σₓ = σ / sqrt(n)
sigma_x = sigma / np.sqrt(n)

# --- HYPOTHETICAL TARGET SAMPLE MEANS ---
# These are the specific sample means (x̄) we are testing probabilities against.
x_bar_1 = 85 # Target 1: A value below the population mean (μ=89).
x_bar_2 = 91 # Target 2: A value above the population mean.
x_bar_3 = 93 # Target 3: A second, higher value above the mean, used for the 'between' probability.

# --- PROBABILITY CALCULATIONS ---
# We calculate the probability (P) of obtaining a sample mean (X̄) in the specified range.

# P-Value 1: P(X̄ < 85) - Probability of getting a sample mean less than 85.
z_score_1 = (x_bar_1 - mu_x) / sigma_x # Z-score tells us how many standard errors 85 is from the mean.
prob_1_less_than = norm.cdf(z_score_1) # norm.cdf() returns the area to the left (P < x̄).

# P-Value 2: P(X̄ > 91) - Probability of getting a sample mean greater than 91.
z_score_2 = (x_bar_2 - mu_x) / sigma_x
# P(X̄ > x̄) is the area to the right, calculated as 1 minus the area to the left (1 - CDF).
prob_2_greater_than = 1 - norm.cdf(z_score_2)

# P-Value 3: P(91 < X̄ < 93) - Probability of getting a sample mean between 91 and 93.
z_score_3 = (x_bar_3 - mu_x) / sigma_x
# P(lower < X̄ < upper) = P(X̄ < upper) - P(X̄ < lower)
prob_3_between = norm.cdf(z_score_3) - norm.cdf(z_score_2)


# --- DISPLAY RESULTS ---
print("--- Central Limit Theorem Results ---")
print(f"Population Mean (μ): {mu}")
print(f"Sample Size (n): {n}")
print(f"Standard Error (σₓ): {sigma_x:.4f}") # The standard deviation of the sample means
print("-" * 35)

print(f"Calculation 1: P(X̄ < {x_bar_1})")
print(f"Calculated Z-score 1 (for x̄ = {x_bar_1}): {z_score_1:.4f}")
print(f"Probability P(X̄ < {x_bar_1}): {prob_1_less_than:.4f}")

print(f"Calculation 2: P(X̄ > {x_bar_2})")
print(f"Calculated Z-score 2 (for x̄ = {x_bar_2}): {z_score_2:.4f}")
print(f"Probability P(X̄ > {x_bar_2}): {prob_2_greater_than:.4f}")

print(f"Calculation 3: P({x_bar_2} < X̄ < {x_bar_3})")
print(f"Calculated Z-score 3 (for x̄ = {x_bar_3}): {z_score_3:.4f}")
print(f"Probability P({x_bar_2} < X̄ < {x_bar_3}): {prob_3_between:.4f}")