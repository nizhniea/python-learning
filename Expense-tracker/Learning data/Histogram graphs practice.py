from scipy.stats import skew, kurtosis
#importing skew and kurtosis functions from scipy.stats module to calculate skewness and kurtosis of data distribution
import numpy as np
import matplotlib.pyplot as plt

card_game_scores = np.random.uniform(low=0, high=100, size=1000)
#Generating 1000 data points from a uniform distribution between 0 and 100

plt.hist(card_game_scores, bins=100, color = "b")
#plotting a histogram of the data with 100 bins and blue color
#visualising data distribution
print(skew(card_game_scores), kurtosis(card_game_scores))
#tells us skewness and kurtosis of the data distribution
plt.show()