from scipy.stats import binom

# --- CONTEXT & PARAMETERS (Using n=57, p=0.4 from a previous context) ---
# Example: A drug has a 40% success rate (p=0.4). In a trial of n=57 patients,
# we want to find the probability that MORE THAN 22 patients successfully respond.

n = 57     # Total number of trials
p = 0.4    # Probability of success
x = 22     # The specific number of successes to exceed

# --- CALCULATION ---
# binom.sf(x, n, p) calculates P(X > x).
# Logic: P(X > x) = 1 - P(X <= x) = 1 - binom.cdf(x, n, p)
binom_sf = binom.sf(x, n, p)

# --- OUTPUT ---
print(f"Binomial SF for x={x} (P(X > {x})): {binom_sf:.4f}")