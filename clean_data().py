def clean_data(df):   
    print(df.shape)
    
    #Adding index column
    total_rows = df.shape[0]
    index = [str(i) for i in range(total_rows)]
    df['index']=index
    
    #Cleaning column names
    for col in df.columns: 
        df.rename(columns={col: col.lower()}, inplace=True)
        
    for col in df.columns: 
        df.rename(columns={col: col.replace(" ","")}, inplace=True)
        
    #Cleaning data
    cat_var=df.loc[:,df.dtypes==np.object].columns
    cat_var=cat_var.tolist()
    for column in cat_var:
       df[column]=df[column].str.lower()
       
def clean_data2(df):
    cat_var=df.loc[:,df.dtypes==np.object].columns
    cat_var=cat_var.tolist()
    df[cat_var] = df[cat_var].apply(lambda x: x.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))

    cat_var.append('cve_hospital')
    for column in cat_var:
        if column not in ['h_fingreso', 'fingreso','fmenstrua','mes','index']:
            df[column] = pd.Categorical(df[column])