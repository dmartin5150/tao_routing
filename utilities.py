
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









def update_column_values(row, value_column):
    if (row[value_column] == 'All'):
        return ['All']
    value_list = row[value_column].split(',')
    value_strip_list = [j.strip() for j in value_list]
    return value_strip_list



def get_unique_column_values(df, column_name):
    cur_df = df[[column_name]]
    sel_group = cur_df.groupby(by=['Order Genus'])
    cur_values =[]
    for name_of_group,contents_of_group  in sel_group:
        cur_group = {'name': name_of_group[0]}
        cur_values.append(cur_group)
    return cur_values 




# def get_genus(df):
#     genus_df = df[['Order Genus']]
#     genus_group = genus_df.groupby(by=['Order Genus'])
#     genus =[]
#     for name_of_group,contents_of_group  in genus_group:
#         cur_group = {'name': name_of_group[0]}
#         genus.append(cur_group)
#     return genus




def get_departments(df):
    department_df = df[['Department ID', 'Department']]
    department_group = department_df.groupby(by=[ 'Department','Department ID',])
    depts =[]
    for name_of_group,contents_of_group  in department_group:
        cur_group = {'name': name_of_group[0], 'value': name_of_group[1] }
        depts.append(cur_group)
    return depts
        


