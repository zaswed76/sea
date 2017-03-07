
import pandas as pd
my_series = pd.Series([1, 2,3, 4, 5, 6, 7, 8, 9, 10])
print(my_series.index)
print(my_series[my_series > 3].values)