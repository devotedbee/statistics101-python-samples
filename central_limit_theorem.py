import numpy as np
from scipy.stats import norm

# --- SCENARIO CONTEXT ---
# This code determines the sample mean (x̄) for a bonus goal such that
# there is only a 10% chance (P=0.10) of the average oil change time for a 
# sample of n=35 falling AT or BELOW that goal time.

# --- GIVEN POPULATION & SAMPLE PARAMETERS ---
mu = 16.5 # Population mean (μ): The average time for ALL oil changes (in minutes).
sigma = 4.5 # Population standard deviation (σ): The variability of individual oil change times.
n = 35 # Sample size (n): The number of oil changes performed in the 2-hour Saturday window.
target_prob = 0.10 # Target probability: P(X̄ <= x̄_goal) = 0.10 (The 10th percentile).

# 1. Calculate the Standard Error (Standard Deviation of the Sample Mean)
# This is the expected variability of sample means, central to the Central Limit Theorem.
# Standard Error (sigma_x_bar) = sigma / sqrt(n)
standard_error = sigma / np.sqrt(n)

# 2. Find the Z-score corresponding to the 10th percentile
# This Z-score is the standardized distance below the mean that corresponds to a cumulative
# area (probability) of 0.10 under the standard normal curve.
z_score = norm.ppf(target_prob) # norm.ppf() is the inverse of the cumulative distribution function (CDF).

# 3. Solve for the Sample Mean (x_bar) using the Z-score formula:
# We convert the standardized Z-score back into the original time units (minutes).
# Z = (x_bar - mu) / standard_error => x_bar = mu + Z * standard_error
x_bar = mu + z_score * standard_error

# --- PRINT RESULTS ---
print("--- Oil-Change Facility Bonus Goal Calculation ---")
print(f"Population Mean Time (μ): {mu} minutes")
print(f"Population Std. Dev. (σ): {sigma} minutes")
print(f"Sample Size (n) for Goal: {n} changes")
print(f"Goal Probability: {target_prob} (10th Percentile)")
print("-" * 50)
print(f"Standard Error (σₓ): {standard_error:.4f} minutes")
print(f"Z-score for 10% Goal: {z_score:.4f}")
print("-" * 50)
print(f"The Goal Time (Required Sample Mean x̄): {x_bar:.2f} minutes")