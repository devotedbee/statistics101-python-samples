from scipy.stats import norm

# --- 1. Define Binomial Parameters (Replace with your problem values) ---
# Total number of trials (n): Must be large (n*p >= 10 and n*(1-p) >= 10 for approximation to be valid)
sample_size_n = 169
# Probability of success on a single trial (p):
prob_success_p = 0.8

# --- 2. Calculate Normal Approximation Parameters ---
# The normal distribution requires a mean (mu) and standard deviation (sigma).

# Calculate the mean (mu) of the approximating normal distribution: mu = n * p
# This represents the expected number of successes.
mu = sample_size_n * prob_success_p

# Calculate the standard deviation (sigma) of the approximating normal distribution: sigma = sqrt(n * p * (1 - p))
# This measures the spread of the distribution.
sigma = (sample_size_n * prob_success_p * (1 - prob_success_p)) ** 0.5

# --- 3. Define the specific event counts (k) for the questions ---
# These variables define the discrete values we are looking for in the binomial distribution.
k_a = 127
k_b_min = 127
k_c_max = 143
k_d_min = 143
k_d_max = 150

# --- 4. Calculate Probabilities using Normal Approximation and CCF ---
# We use the Continuity Correction Factor (CCF) because we are using a continuous
# normal distribution to approximate a discrete binomial distribution.

# (a) Probability for X = k_a (Exactly k_a successes)
# Logic: P(k_a - 0.5 < X_Normal < k_a + 0.5)
# This uses the area under the normal curve from 0.5 below to 0.5 above the target integer.
p_exact = norm.cdf(k_a + 0.5, mu, sigma) - norm.cdf(k_a - 0.5, mu, sigma)

print(f"(a) P(X = {k_a}) [Exact Probability]: {p_exact:.4f}")

# (b) Probability for X >= k_b_min (At least k_b_min successes)
# Logic: P(X_Normal > k_b_min - 0.5)
# Since we include k_b_min, we start the normal calculation 0.5 below it.
# We calculate 1 - P(X_Normal <= k_b_min - 0.5) because norm.cdf gives P(X <= x).
p_at_least = 1 - norm.cdf(k_b_min - 0.5, mu, sigma)

print(f"(b) P(X >= {k_b_min}) [At Least]: {p_at_least:.4f}")

# (c) Probability for X < k_c_max (Fewer than k_c_max successes)
# This is equivalent to P(X <= k_c_max - 1).
# Logic: P(X_Normal < k_c_max - 0.5)
# Since we exclude k_c_max, the upper boundary of the continuous range is k_c_max - 0.5.
p_fewer_than = norm.cdf(k_c_max - 0.5, mu, sigma)

print(f"(c) P(X < {k_c_max}) [Fewer Than]: {p_fewer_than:.4f}")

# (d) Probability for k_d_min <= X <= k_d_max (Between two values, inclusive)
# Logic: P(k_d_min - 0.5 < X_Normal < k_d_max + 0.5)
# The probability is the difference between the CDF at the upper boundary (k_d_max + 0.5)
# and the CDF at the lower boundary (k_d_min - 0.5).
p_between = norm.cdf(k_d_max + 0.5, mu, sigma) - norm.cdf(k_d_min - 0.5, mu, sigma)

print(f"(d) P({k_d_min} <= X <= {k_d_max}) [Between]: {p_between:.4f}")