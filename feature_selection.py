import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer


csv_path = ('interrupcion-legal-del-embarazo.csv')
df = pd.read_csv(csv_path, sep=";")

clean_data(df)

df = df.drop(['fingreso','panticoncep','autoref','p_diasgesta','entidad','consejeria','motiles','s_complica','gesta','c_num','fmenstrua','año','mes','h_fingreso'], axis=1)
print(df.dtypes)

#desc_derechohab
df.loc[(df["desc_derechohab"] != 'ninguna') & (df["desc_derechohab"].notnull()) & (df["desc_derechohab"]!='n/e'), ['desc_derechohab']] = 'si'
df.loc[(df["desc_derechohab"] != 'si') & (df["desc_derechohab"].notnull()), ['desc_derechohab']] = 'no'

#nivel_edu
df.loc[(df["nivel_edu"] != 'preparatoria completa') & 
       (df["nivel_edu"].notnull()) & 
       (df["nivel_edu"]!='secundaria completa') &
       (df["nivel_edu"]!='licenciatura completa') &
       (df["nivel_edu"]!='primaria completa') &
       (df["nivel_edu"]!='preparatoria incompleta'), 
       ['nivel_edu']] = 'otra'

#ocupacion
df.loc[(df["ocupacion"] != 'estudiante') & 
       (df["ocupacion"].notnull()) & 
       (df["ocupacion"]!='empleada') &
       (df["ocupacion"]!='ama de casa') &
       (df["ocupacion"]!='trabajadora del sector público') &
       (df["ocupacion"]!='comerciante') &
       (df["ocupacion"]!='trabajadora del sector mesera') &
       (df["ocupacion"]!='desempleada'), 
       ['ocupacion']] = 'otra'

#religion
df.loc[(df["religion"] != 'católica') & 
       (df["religion"].notnull()) & 
       (df["religion"]!='ninguna') &
       (df["religion"]!='creyente'), 
       ['religion']] = 'otra'

#parentesco
df.loc[(df["parentesco"].notnull()),
       ['parentesco']] = 'acompañada'
df.loc[(df["parentesco"].isnull()),
       ['parentesco']] = 'sola'

#anticonceptivo
df.loc[(df["anticonceptivo"] != 'ninguno') & 
       (df["anticonceptivo"].notnull()) & 
       (df["anticonceptivo"]!='condón'), 
       ['anticonceptivo']] = 'otro'
df.loc[(df["anticonceptivo"].isnull()),
       ['anticonceptivo']] = 'ninguno'

clean_data2(df)
eda_generator(df)

export_csv = df.to_csv (r'C:\\Users\\marco\\OneDrive\\Documentos\\ITAM\\Minería de Datos\\Proyecto 1\\interrupcion-legal-del-embarazo2.csv', index = None, header=True)