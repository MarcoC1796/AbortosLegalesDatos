print(df.isnull().sum())
df['dia'] = df['fingreso'].astype(str).str[0:1]
