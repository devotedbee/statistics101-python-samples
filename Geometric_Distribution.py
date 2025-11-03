from scipy.stats import geom

# Parameters
p = 0.3      # success probability
x = 2        # number of trials until the first success

# Calculate the geometric probability
geom_prob = geom.pmf(x, p)
print(f"Geometric distribution probability for x={x}: {geom_prob:.4f}")
