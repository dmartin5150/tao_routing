import pandas as pd
from utilities import fill_na_with_all, update_dictionary_values, update_column_values,get_unique_column_values
import array as arr
# Data for practice routing is incomplete so will not process for now
practice_routing = 5533



def add_new_route(df, tao_id, depts,dept_ids, providers, provider_ids,priority, genus, order_type, order_type_ids):
    new_row = df.iloc[0].copy()
    new_row['TAO ID'] = tao_id
    new_row['Department']= depts
    new_row['Department ID'] = dept_ids
    new_row['Dept_ID_List'] = dept_ids
    new_row['Provider'] = providers
    new_row['Provider ID'] = provider_ids
    new_row['Ordering'] = priority
    new_row['Order Genus'] = genus
    new_row['Genus_List'] = genus
    new_row['Order Type'] = order_type
    new_row['Order Type ID'] = order_type_ids
    df = pd.concat([pd.DataFrame([new_row]), df], ignore_index=True) 
    return df


def update_routing_rows(df):
    for index, row in df.iterrows():
        if(row['TAO ID'] != practice_routing):
            df['Dept_ID_List'] = df.apply(lambda row: update_column_values(row, 'Department ID'), axis=1)
            df['Provider_ID_List'] = df.apply(lambda row: update_column_values(row, 'Provider ID'), axis=1)
            df['Genus_List'] = df.apply(lambda row: update_column_values(row, 'Order Genus'), axis=1)
    return df




def get_tao_rules(filename,ministry):
    taos_raw_data = pd.read_csv(filename)
    tao_min = taos_raw_data[taos_raw_data['CONTEXT_NAME'] == ministry]
    tao_min = fill_na_with_all(tao_min)
    tao_min['Department ID'] = tao_min['Department ID'].astype(str)
    tao_min['Order Type ID'] = tao_min['Order Type ID'].astype(str)
    tao_min['Provider ID'] = tao_min['Provider ID'].astype(str)
    tao_min['Order Genus'] = tao_min['Order Genus'].astype(str)
    tao_min = update_routing_rows(tao_min)
    return tao_min

