
import pandas as pd
from utilities import update_dictionary_values
# Data for practice routing is incomplete so will not process for now
practice_routing = 5533


columns = ['CONTEXT_ID', 'CONTEXT_NAME', 'TAO ID', 'Last Modified Date',
       'Document Class/Subclass', 'Document Class/Subclass ID', 'Ordering',
       'Action', 'Next Status', 'Department', 'Department ID', 'Provider',
       'Provider ID', 'Order Type', 'Order Type ID', 'Order Genus',
       'Assigned To']


def process_routing_column(value):
    if value == 'All':
        return ['All']
    return value.split(',') 

def process_routing_row(row,depts, providers,df):
    cur_depts = process_routing_column(row['Department ID'])
    cur_providers = process_routing_column(row['Provider ID'])
    for dept in cur_depts:
        for provider in cur_providers:
            if row['TAO ID'] == practice_routing:
                continue
            new_row = row.copy()
            new_row['Provider ID'] = provider
            new_row['Provider'] = providers[provider.strip()]
            new_row['Department ID'] = dept
            new_row['Department'] = depts[dept.strip()] 
            df = pd.concat([pd.DataFrame([new_row]), df], ignore_index=True) 
    return df


def create_routing_table (df, depts, providers,routing_df):
    for index, row in df.iterrows():
        if(row['TAO ID'] != practice_routing):
            routing_df = process_routing_row(row,depts, providers,routing_df)
    return routing_df


def process_department_and_provider_row(row, depts, providers):
    depts = update_dictionary_values(row, 'Department', 'Department ID',depts)
    providers = update_dictionary_values(row, 'Provider', 'Provider ID',providers)
    return depts, providers

def add_departments_and_providers(df, depts, providers):
    for index, row in df.iterrows():
        if(row['TAO ID'] != practice_routing):
            depts, providers = process_department_and_provider_row(row, depts, providers)
    return depts, providers


def get_departments(df):
    providers = {}
    departments = {}
    departments, providers = add_departments_and_providers(df,departments,providers)
    routing_df = pd.DataFrame(columns=columns)
    routing_df = create_routing_table (df, departments, providers,routing_df)
    routing_df = routing_df[['Department ID', 'Department']]
    routing_df = routing_df.drop_duplicates(subset='Department ID')
    department_group = routing_df.groupby(by=[ 'Department','Department ID',])
    depts =[{'label':'All', 'value': '0'}]
    for name_of_group,contents_of_group  in department_group:
        if (name_of_group[0] == 'All'):
            continue
        cur_group = {'label': name_of_group[0], 'value': name_of_group[1] }
        depts.append(cur_group)
    seen = {}
    for obj in depts:
        if obj["label"] in seen.keys():
            depts.remove(obj)
        else:
            seen[obj["label"]] = 1
    return depts