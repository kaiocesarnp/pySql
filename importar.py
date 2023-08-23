#Por meio do Pandas, podemos realizar a importação de dados externos

import pandas as pd

cali_houses = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data')
print(cali_houses.head())

print(cali_houses.describe())
