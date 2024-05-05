import pandas as pd
from utilities import fill_na_with_all, update_dictionary_values, update_column_values,get_unique_column_values

# Data for practice routing is incomplete so will not process for now
practice_routing = 5533

columns = ['CONTEXT_ID', 'CONTEXT_NAME', 'TAO ID', 'Last Modified Date',
       'Document Class/Subclass', 'Document Class/Subclass ID', 'Ordering',
       'Action', 'Next Status', 'Department', 'Department ID', 'Provider',
       'Provider ID', 'Order Type', 'Order Type ID', 'Order Genus',
       'Assigned To']





def process_department_and_provider_row(row, depts, providers):
    depts = update_dictionary_values(row, 'Department', 'Department ID',depts)
    providers = update_dictionary_values(row, 'Provider', 'Provider ID',providers)
    return depts, providers

def add_departments_and_providers(df, depts, providers):
    for index, row in df.iterrows():
        if(row['TAO ID'] != practice_routing):
            depts, providers = process_department_and_provider_row(row, depts, providers)
    return depts, providers


def update_routing_rows(df):
    for index, row in df.iterrows():
        if(row['TAO ID'] != practice_routing):
            df['Dept_ID_List'] = df.apply(lambda row: update_column_values(row, 'Department ID'), axis=1)
            df['Provider_ID_List'] = df.apply(lambda row: update_column_values(row, 'Provider ID'), axis=1)
            df['Genus_List'] = df.apply(lambda row: update_column_values(row, 'Order Genus'), axis=1)
    return df


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

def get_tao_rules(filename,ministry):
    providers = {}
    departments = {}
    athena_data_frame = pd.DataFrame(columns=columns)
    taos_raw_data = pd.read_csv(filename)
    tao_min = taos_raw_data[taos_raw_data['CONTEXT_NAME'] == ministry]
    tao_min = fill_na_with_all(tao_min)
    tao_min = update_routing_rows(tao_min)
    # departments, providers = add_departments_and_providers(tao_min,departments,providers)
    return tao_min