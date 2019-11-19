import pandas as pd
import os
import numpy as np
import pandas as pd
import runpy
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

runfile('load_data.py')
runfile('clean_data().py')
runfile('eda.py')
runfile('feature_selection.py')
runfile('transfom_data.py')

#eda1
pd.set_option('display.max_columns', 500)
df=load_data(';')
df=clean_data(df)
df=clean_data2(df)
eda_generator(df)

#feature selection
csv_path = ('interrupcion-legal-del-embarazo.csv')
df1=load_data(";")
clean_data(df1)
df1 = feature_selection(df1)
df1=imputate(df1)

export_csv = df1.to_csv (r'\\Users\\marcochacon\\Documents\\ITAM\\7moSemestre\\MineriaDatos\\interrupcion-legal-del-embarazo2.csv'
                        , index = None, header=True)
