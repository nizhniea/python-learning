import numpy as np
from scipy import stats

ages_group_2 = np.array([25, 24, 26, 24, 25, 25, 24, 26, 27, 24, 26])
mean_2 = np.mean(ages_group_2)
median_2 = np.median(ages_group_2)
# TODO: Compute the mean of the ages group.
# TODO: Compute the median of the ages group.
mode_2 = stats.mode(ages_group_2)
range_2 = np.ptp(ages_group_2)
print("For the second age group:")
print("Mean: ", mean_2) 
print("Median: ", median_2)
print("Range: ", range_2)
print("Mode: ", mode_2.mode)