import pandas as pd
import os
import numpy as np
import seaborn as sns


#Poder visualizar varias columnas
pd.set_option('display.max_columns', 500)

#Vemos que hay en el directorio que usamos
print(os.listdir(os.getcwd()))

#Carga de datos
csv_path = ('interrupcion-legal-del-embarazo.csv')
df = pd.read_csv(csv_path, sep=";")

