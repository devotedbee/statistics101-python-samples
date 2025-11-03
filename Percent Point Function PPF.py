# Calculate percent point (inverse CDF)
quantile = 0.95  # 95%
binom_ppf = binom.ppf(quantile, n, p)
print(f"95th percentile for Binomial: {binom_ppf:.4f}")
