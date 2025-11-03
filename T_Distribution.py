from scipy.stats import t

# Parameters
df = 10             # degrees of freedom
x = 1.5             # t-value

# Calculate the t-distribution probability
t_prob = t.pdf(x, df)
print(f"T-distribution probability for x={x}: {t_prob:.4f}")
