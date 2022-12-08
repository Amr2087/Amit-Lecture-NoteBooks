import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

dataset = pd.read_csv("data/diabetes.csv")

print(sns.pairplot(dataset))


print(1)
