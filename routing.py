import pandas as pd


def route(df, dept_id, provider_id, genus, order_id):
    
    if (dept_id != 'All'):
        depts = df[(df['Department ID'] == dept_id) | (df['Department ID'] == 'All')]
        print('depts with id', depts)
    else:
        depts = df[df['Department ID'] == 'All']
    if (provider_id != 'All'):
        depts = depts[(depts['Provider ID'] == provider_id) | (depts['Provider ID'] == 'All')]
    else:
        depts = depts[depts['Provider ID'] == 'All']

    if (genus != 'All'):
        depts = depts[(depts['Genus_List'].str.contains(genus, regex=False)) |  (depts['Genus_List'].str.contains('All', regex=False))]

    if (order_id != 'All'):
        depts = depts[(depts['Order Type ID'] == order_id) | (depts['Order Type ID'] == 'All')]
    else:
        depts = depts[depts['Order Type ID'].str.strip() == 'All']
    return depts
    # print(depts)