from scipy.stats import poisson

# --- CONTEXT & PARAMETERS ---
# Imagine a customer support call center that receives an average of lam=5 calls per hour.
# We want to find the probability of receiving exactly x=3 calls in the next hour.

# 1. Average Rate (lam):
lam = 5      # The average number of events in the specified interval (lambda, λ).

# 2. Number of Events (x):
x = 3        # The exact number of events we are interested in observing.

# --- CALCULATION ---
# poisson.pmf(x, lam) calculates P(X = x).
# The Poisson PMF formula is: P(X=x) = (e^(-λ) * λ^x) / x!
poisson_prob = poisson.pmf(x, lam)

# --- OUTPUT ---
print(f"Poisson distribution PMF for x={x} (P(X={x})): {poisson_prob:.4f}")