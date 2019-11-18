import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

csv_path = ('interrupcion-legal-del-embarazo2.csv')
df = pd.read_csv(csv_path, sep=",")

df = df.drop(['p_consent'], axis=1)

transformers = [('impute_edocivil_descripcion', SimpleImputer(strategy="most_frequent"), ['edocivil_descripcion']),
                ('desc_derechohab', SimpleImputer(strategy="most_frequent"), ['desc_derechohab']),
                ('nivel_edu', SimpleImputer(strategy="constant", fill_value="otra"), ['nivel_edu']),
                ('ocupacion', SimpleImputer(strategy="constant", fill_value="otra"), ['ocupacion']),
                ('religion', SimpleImputer(strategy="constant", fill_value="otra"), ['religion']),
                ('alcomunicipio', SimpleImputer(strategy="most_frequent"), ['alcomunicipio']),
                ('menarca', SimpleImputer(strategy="mean"), ['menarca']),
                ('fsexual', SimpleImputer(strategy="mean"), ['fsexual']),
                ('sememb', SimpleImputer(strategy="mean"), ['sememb']),
                ('nhijos', SimpleImputer(strategy="mean"), ['nhijos']),
                ('naborto', SimpleImputer(strategy="mean"), ['naborto']),
                ('npartos', SimpleImputer(strategy="mean"), ['npartos']),
                ('ncesarea', SimpleImputer(strategy="mean"), ['ncesarea']),
                ('nile', SimpleImputer(strategy="mean"), ['nile']),
                ('desc_servicio', SimpleImputer(strategy="most_frequent"), ['desc_servicio']),
                ('p_semgest', SimpleImputer(strategy="mean"), ['p_semgest']),
                ('procile', SimpleImputer(strategy="most_frequent"), ['procile'])]

col_trans = ColumnTransformer(transformers, remainder="passthrough", n_jobs=-1, verbose=True)
col_trans.fit(df)
df1=col_trans(df)

export_csv = df.to_csv (r'C:\\Users\\marco\\OneDrive\\Documentos\\ITAM\\Minería de Datos\\Proyecto 1\\interrupcion-legal-del-embarazo3.csv', index = None, header=True)