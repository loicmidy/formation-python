# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn import datasets


iris = datasets.load_iris()
irisdataframe=pd.DataFrame(iris['data'],columns=iris['feature_names'])
irisdataframe['target'] = iris['target'].astype(str)

print(irisdataframe.info())

print(irisdataframe.describe())
print(irisdataframe['target'].describe())

print(irisdataframe.cov())
print(irisdataframe.corr())
