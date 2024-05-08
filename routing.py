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
    
    if (dept_id != '0'):
        depts = df[(df['Department ID'].str.contains(dept_id)) | (df['Department ID'] == 'All')]
    else:
        depts = df[df['Department ID'] == 'All']
    if (provider_id != '0'):
        depts = depts[(depts['Provider ID'].str.contains(provider_id)) | (depts['Provider ID'] == 'All')]
    else:
        depts = depts[depts['Provider ID'] == 'All']
    print('dept 1', depts)
    if (genus != '0'):
        depts = depts[(depts['Genus_List'].str.contains(genus, regex=False)) |  (depts['Genus_List'].str.contains('All', regex=False))]
    else:
        depts = depts[depts['Order Genus'] == 'All']
    if (order_id != '0'):
        depts = depts[(depts['Order Type ID'].str.contains(order_id,regex=False)) | (depts['Order Type ID'] == 'All')]
    else:
        depts = depts[depts['Order Type ID'] == 'All']
    print('orderId', order_id)
    print('dept 2', depts['Order Type ID'])
    results = convert_results(depts.sort_values(by='Ordering'))
    return results