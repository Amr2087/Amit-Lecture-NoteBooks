import pandas as pd
import numpy as np
dataframe = pd.DataFrame(data=np.random.randn(10000).reshape(1000, 10), columns=['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10'])

st = dataframe.loc[50, 'col1':'col7'].values

nd = dataframe.loc[70:201, 'col5']

rd1 = dataframe.loc[:, 'col3'].values
rd2 = dataframe.loc[:, 'col5'].values

cov1 = np.cov(rd1, rd2)
cor1 = np.corrcoef(rd1, rd2)

th = dataframe.tail(1).values
mean1 = np.mean(th)
std = np.std(th)
var = np.var(th)

