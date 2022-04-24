from re import A
import statistics
import pandas as pd

sr = pd.Series([10, 25, 3, 25, 24, 6])

mean = sr.mean()
median = sr.median()
mode = sr.mode()
range1 = sr.max() - sr.min();
stdeviation = sr.std(axis=0, skipna=True)

print("Mean:",mean)
print("Median:",median)
print("Mode:",mode)
print("Range:",range1)
print("Standard Deviation:",stdeviation)
print("Variance of sample set is % s:"
      % (statistics.variance(sr)))
