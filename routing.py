import pandas as pd


def route(df, dept_id, provider_id, genus, order_id):
    
    if (dept_id != '0'):
        depts = df[(df['Department ID'].str.contains(dept_id)) | (df['Department ID'] == 'All')]
        print('depts with id', depts)
    else:
        depts = df[df['Department ID'] == 'All']
    if (provider_id != '0'):
        depts = depts[(depts['Provider ID'].str.contains(provider_id)) | (depts['Provider ID'] == 'All')]
    else:
        depts = depts[depts['Provider ID'] == 'All']
    print('depts with id 2', depts)
    if (genus != '0'):
        depts = depts[(depts['Genus_List'].str.contains(genus, regex=False)) |  (depts['Genus_List'].str.contains('All', regex=False))]
    print('depts with id 3', depts)
    if (order_id != '0'):
        depts = depts[(depts['Order Type ID'].str.contains(order_id,regex=False)) | (depts['Order Type ID'] == 'All')]
    else:
        depts = depts[depts['Order Type ID'].str.strip() == 'All']
    print('depts with id 3', depts)
    return depts
    # print(depts)