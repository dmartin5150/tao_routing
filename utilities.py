
import pandas as pd
# Data for practice routing is incomplete so will not process for now
practice_routing = 5533

def fill_na_with_all(df):
    values = {'Provider ID': 'All', 'Order Type ID':'All', 'Order Type':'All','Order Genus':'All'}
    return df.fillna(value=values)

def update_dictionary_values(row, name_column, value_column,value_dict):
    if(row[value_column] == 'All'):
        value_dict[row[value_column]] = 'All'
        return value_dict
    else:
        names = row[name_column].split(',')
        ids = row[value_column].split(',')
    for x, y in zip(ids, names):
        value_dict[x.strip()] = y.strip()
    return value_dict





# keeping as an example for apply for now
# def add_departments(df):
#     df['depts'] = df.apply(lambda row: create_value_pairs(row, 'Department', 'Department ID'), axis=1)
#     return df

def process_routing_column(value):
    if value == 'All':
        return ['All']
    return value.split(',') 


def process_department_and_provider_row(row, depts, providers):
    depts = update_dictionary_values(row, 'Department', 'Department ID',depts)
    providers = update_dictionary_values(row, 'Provider', 'Provider ID',providers)
    return depts, providers

def add_departments_and_providers(df, depts, providers):
    for index, row in df.iterrows():
        if(row['TAO ID'] != practice_routing):
            depts, providers = process_department_and_provider_row(row, depts, providers)
    return depts, providers



def update_column_values(row, value_column):
    if (row[value_column] == 'All'):
        return ['All']
    value_list = row[value_column].split(',')
    value_strip_list = [j.strip() for j in value_list]
    return value_strip_list


def update_routing_rows(df):
    for index, row in df.iterrows():
        if(row['TAO ID'] != practice_routing):
            df['Dept_ID_List'] = df.apply(lambda row: update_column_values(row, 'Department ID'), axis=1)
            df['Provider_ID_List'] = df.apply(lambda row: update_column_values(row, 'Provider ID'), axis=1)
            df['Genus_List'] = df.apply(lambda row: update_column_values(row, 'Order Genus'), axis=1)
    return df



def process_routing_row(row,depts, providers,df):
    cur_depts = process_routing_column(row['Department ID'])
    cur_providers = process_routing_column(row['Provider ID'])
    for dept in cur_depts:
        for provider in cur_providers:
            if row['TAO ID'] == 5533:
                continue
            new_row = row.copy()
            new_row['Provider ID'] = provider
            new_row['Provider'] = providers[provider.strip()]
            new_row['Department ID'] = dept
            new_row['Department'] = depts[dept.strip()] 
            df = pd.concat([pd.DataFrame([new_row]), df], ignore_index=True) 
    return df


def get_genus(df):
    genus_list = []
    for index, row in df.iterrows():
        cur_row = row['Order Genus'].split(',')
        genus_list = set([*genus_list,*cur_row])
    genus_stripped_list = [j.strip() for j in genus_list]
    return genus_stripped_list



def create_routing_table (df, depts, providers,routing_df):
    for index, row in df.iterrows():
        if(row['TAO ID'] != practice_routing):
            routing_df = process_routing_row(row,depts, providers,routing_df)
    return routing_df

        


