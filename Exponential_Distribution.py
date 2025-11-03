from scipy.stats import expon

# Parameters
lambda_rate = 0.5  # rate parameter
x = 4               # time value

# Calculate the exponential probability
expon_prob = expon.pdf(x, scale=1/lambda_rate)
print(f"Exponential distribution probability for x={x}: {expon_prob:.4f}")
