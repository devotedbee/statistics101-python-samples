from scipy.stats import poisson

# Parameters
lam = 5      # average rate (lambda)
x = 3        # number of events

# Calculate the Poisson probability
poisson_prob = poisson.pmf(x, lam)
print(f"Poisson distribution probability for x={x}: {poisson_prob:.4f}")
