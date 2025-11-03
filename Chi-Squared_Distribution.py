from scipy.stats import chi2

# Parameters
degrees_of_freedom = 5
x = 10              # x value

# Calculate the chi-squared probability
chi2_prob = chi2.pdf(x, degrees_of_freedom)
print(f"Chi-squared distribution probability for x={x}: {chi2_prob:.4f}")
