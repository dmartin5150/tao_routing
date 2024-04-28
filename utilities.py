
import pandas as pd



def fill_na_with_all(df):
    values = {"Provider ID": "All", "Order Type ID":"All", "Order Type":"All",}
    return df.fillna(value=values)

def update_dictionary_values(row, name_column, value_column,value_dict):
    if(row[value_column] == 'All'):
        value_dict[row[value_column]] = 'All'
        return value_dict
    else:
        names = row[name_column].split(',')
        ids = row[value_column].split(',')
        for x, y in zip(ids, names):
            value_dict[x] = y
    return value_dict


# def create_orders(row, name_column, value_column):
#     # print('row ', row)
#     depts = {}
#     if(row[name_column] == 'All'):
#         depts[value_column] = 'All'
#         return depts
#     else:
#         depts[row[value_column]] = row[name_column]
#     return depts


# def add_departments(df):
#     df['depts'] = df.apply(lambda row: create_value_pairs(row, 'Department', 'Department ID'), axis=1)
#     return df




def process_department_and_provider_row(row, depts, providers):
    depts = update_dictionary_values(row, 'Department', 'Department ID',depts)
    providers = update_dictionary_values(row, 'Provider', 'Provider ID',providers)
    return depts, providers

def add_departments_and_providers(df, depts, providers):
    for index, row in df.iterrows():
        depts, providers = process_department_and_provider_row(row, depts, providers)
    return depts, providers

# def process_routing_row(row):
#     departments = process_routing_column(row['Department ID'])
#     providers = process_routing_column(row['Provider ID'])
    # for dept in departments:
    #     for provider in providers:
    #         new_row = row.copy()
    #             print(new_row)
    # return row


    



def create_routing_table (df):
    # for index, row in df.iterrows():
    #     process_routing_row(row)
    return df

        


