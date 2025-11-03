from scipy.stats import norm

# Parameters
mu = 0       # mean
sigma = 1    # standard deviation
x = .0028      # value to evaluate

# Calculate the normal probability
norm_prob = norm.pdf(x, mu, sigma)
print(f"Normal distribution probability for x={x}: {norm_prob:.4f}")
