from scipy.stats import norm

# Parameters
n = 169
p = 0.8
mu = n * p
sigma = (n * p * (1 - p)) ** 0.5

# (a) Exact probability for X = 127
p_exact_127 = norm.cdf(127.5, mu, sigma) - norm.cdf(126.5, mu, sigma)

print(f"Probability of exactly 127 flights on time: {p_exact_127:.4f}")

# (b) Probability for X >= 127
p_at_least_127 = 1 - norm.cdf(126.5, mu, sigma)

print(f"Probability of at least 127 flights on time: {p_at_least_127:.4f}")

# (c) Probability for X < 143
p_fewer_than_143 = norm.cdf(142.5, mu, sigma)

print(f"Probability of fewer than 143 flights on time: {p_fewer_than_143:.4f}")

# (d) Probability for 143 <= X <= 150
p_between_143_and_150 = norm.cdf(150.5, mu, sigma) - norm.cdf(142.5, mu, sigma)

print(f"Probability of between 143 and 150 flights on time: {p_between_143_and_150:.4f}")