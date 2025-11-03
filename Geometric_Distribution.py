from scipy.stats import geom

# --- CONTEXT & PARAMETERS ---
# Imagine a basketball player has a 30% chance of making a free throw (success).
# We want to find the probability that their very first successful free throw occurs on their 2nd attempt.

# 1. Success Probability (p):
# The probability of 'success' on any single, independent trial.
p = 0.3      # (e.g., 30% chance of making the shot)

# 2. Number of Trials (x):
# The specific trial number on which the *first* success is observed.
x = 2        # (e.g., the first success occurs on the 2nd attempt)

# --- CALCULATION ---
# geom.pmf(x, p) calculates P(X = x).
# The Geometric PMF formula is: P(X=x) = (1 - p)^(x-1) * p
# This represents (Failures on first x-1 trials) * (Success on the x-th trial).
geom_prob = geom.pmf(x, p)

# --- OUTPUT ---
print(f"Geometric distribution PMF for x={x} (P(X={x})): {geom_prob:.4f}")