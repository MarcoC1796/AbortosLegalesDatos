
def eda_generator(df):
    null_values = df.isnull().sum()
    print(null_values)
    
    #Categorical data
    
    cat_var=df.loc[:,df.dtypes=='category'].columns
    print('\nVariables categóricas:')
    print(cat_var)
    
    print(df.describe(include='category'))
       
    for column in cat_var:
       if column not in ['h_fingreso', 'fingreso','mes']:
           columnSeriesObj = df[column]
           print('\nColunm Name : ', column)
           print('Column Contents : ', columnSeriesObj.unique())
           
    #Numerical data
    print(df.describe())

    #Geda categorical data
    for column in cat_var:
           if column not in ['h_fingreso', 'fingreso','mes','index','alcomunicipio','panticoncep']:
               df[column].value_counts().plot(kind='bar',title=column)
               plt.show()
    #Geda for numerical data
      
    cat_num=df.loc[:,df.dtypes=='float64'].columns
    for column in cat_num:
           df.hist(column)