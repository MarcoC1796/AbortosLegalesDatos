
def imputate(df):
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
    u=col_trans.transform(df)
    df1= pd.DataFrame(u, columns=df.columns)
    return df1
