import pandas as pd


def convert_results(df):
    results = []
    for index, row in df.iterrows():
        cur_results = {'taoID': row['TAO ID'], 'dept': row['Department'], 'provider':row['Provider'], 
                       'genus': row['Order Genus'],'orderType':row['Order Type'],'priority':row['Ordering'],
                        'bucket': row['Assigned To'] }
        results.append(cur_results)
    return results



def route(df, dept_id, provider_id, genus, order_id):
    
    depts = df

    if (dept_id != '0'):
        depts = df[(df['Department ID'].str.contains(dept_id)) | (df['Department ID'] == 'All')]
    if (provider_id != '0'):
        depts = depts[(depts['Provider ID'].str.contains(provider_id)) | (depts['Provider ID'] == 'All')]
    print('dept 1', depts)
    if (genus != '0'):
        depts = depts[(depts['Genus_List'].str.contains(genus, regex=False)) |  (depts['Genus_List'].str.contains('All', regex=False))]
    if (order_id != '0'):
        depts = depts[(depts['Order Type ID'].str.contains(order_id,regex=False)) | (depts['Order Type ID'] == 'All')]
    print('dept 4', depts)
    results = convert_results(depts.sort_values(by='Ordering'))
    return results