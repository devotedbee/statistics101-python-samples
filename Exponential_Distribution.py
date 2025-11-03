from scipy.stats import expon

# --- CONTEXT & PARAMETERS ---
# Imagine a customer service line where customers arrive at an average rate (lambda) of 0.5 customers per minute.
# We want to know the density of the probability distribution at exactly the 4-minute mark.

# 1. Rate Parameter (lambda_rate):
# This is the average number of events per unit of time (e.g., 0.5 arrivals/minute).
lambda_rate = 0.5  

# 2. Scale Parameter (1/lambda_rate):
# The Exponential distribution in scipy.stats uses 'scale', where scale = 1 / lambda.
# The scale parameter (often denoted as beta, or mu) is the mean time *between* events.
# Mean Time Between Events (MTBE) = 1 / 0.5 = 2 minutes.

# 3. X Value:
# This is the specific time (or distance, etc.) at which we want to find the density.
x = 4               # Time value (e.g., 4 minutes)

# --- CALCULATION ---
# expon.pdf(x, scale=1/lambda) calculates the height of the probability curve at the point x.
# The PDF formula is: f(x) = lambda * e^(-lambda * x)
expon_prob = expon.pdf(x, scale=1/lambda_rate)

# --- OUTPUT ---
print(f"Exponential distribution PDF value (density) for x={x} and rate={lambda_rate}: {expon_prob:.4f}")