import pandas as pd
from sklearn.datasets import fetch_california_housing

df = fetch_california_housing(as_frame=True).frame

print(list(df.columns))