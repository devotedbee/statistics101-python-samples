from scipy.stats import binom

# --- CONTEXT & PARAMETERS ---
# Imagine a scenario where a manufacturer's machine has a 35% chance of producing a defective item.
# We take a random sample of 30 items and want to know the probability that exactly 20 are defective.

# Parameters for the Binomial Distribution B(n, p):
n = 30    # Total number of independent trials (e.g., sample size, number of items checked)
p = 0.35  # Probability of success on a single trial (e.g., probability of being defective)
x = 20    # Exact number of successes we are interested in (e.g., exactly 20 defective items)

# --- CALCULATION ---
# binom.pmf(x, n, p) calculates P(X = x).
# This is the formula: P(X=x) = (n choose x) * p^x * (1-p)^(n-x)
probability = binom.pmf(x, n, p)

# --- OUTPUT ---
# The result is formatted to four decimal places for clarity.
print(f"The probability of observing exactly {x} successes (e.g., defective items) ")
print(f"in {n} trials (e.g., sample size) with a success probability of {p} is: {probability:.4f}")