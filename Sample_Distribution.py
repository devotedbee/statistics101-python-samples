import numpy as np  # Import the NumPy library for numerical operations

# Given parameters
mu = 68  # Population mean 'μ' 
sigma = 4  # Population standard deviation 'σ'
n = 52  # Sample size 'n'

# Mean of the sample distribution is the same as the population mean
mu_x = mu  

# Standard deviation of the sample distribution (standard error)
# It is calculated as the population standard deviation divided by the square root of the sample size
sigma_x = sigma / np.sqrt(n)  

# Calculate n times the square root of σ
result = n * np.sqrt(sigma)  # n * sqrt(σ)

# Display the results
print(f"Mean of the sample distribution (μₓ): {mu_x}")  # Print the mean
print(f"Standard deviation of the sample distribution (σₓ): {sigma_x}")  # Print the standard deviation
print(f"{n} times the square root of σ: {result}")  # Print the result of n * sqrt(σ)
