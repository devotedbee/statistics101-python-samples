import numpy as np  # Import the NumPy library for numerical operations

# --- POPULATION PARAMETERS ---
# Context: Imagine a population where the average height is 68 inches, with a standard deviation of 4 inches.
mu = 68    # Population mean 'μ' (The average height of all individuals)
sigma = 4  # Population standard deviation 'σ' (The variability of individual heights)
n = 52     # Sample size 'n' (The number of individuals measured in each sample)

# --- CENTRAL LIMIT THEOREM CALCULATIONS ---

# 1. Mean of the Sample Distribution (Mean of means)
# According to the CLT, the mean of the sampling distribution (μₓ) is always equal to the population mean (μ).
mu_x = mu  

# 2. Standard Deviation of the Sample Distribution (Standard Error)
# This measures the variability of the sample means around the population mean.
# It is calculated as the population standard deviation divided by the square root of the sample size.
sigma_x = sigma / np.sqrt(n)  

# --- EXTRANEOUS CALCULATION (for demonstration only) ---
# This calculation is not directly related to the Central Limit Theorem or sampling distribution properties.
result_demonstration = n * np.sqrt(sigma)  # n * sqrt(σ)

# --- DISPLAY RESULTS ---
print("--- Central Limit Theorem Results ---")
print(f"Mean of the sampling distribution (μₓ): {mu_x:.2f}")
print(f"Standard Error (σₓ) of the mean: {sigma_x:.4f}")
print(f"Demonstration value (n * sqrt(σ)): {result_demonstration:.4f}")