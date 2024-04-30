import pandas as pd


order_columns = ['_id', 'practiceId', 'departmentId', 'deptName', 'dateOrdered',
       'dateOrderedFormatted',  'orderName','clinicalOrderTypeId', 'documentId', 
       'orderingProvider', 'orderType', 'orderGenus', 'orderPriority', 'ministry',
        'taoBucket', 'usedTAO', 'performDate','assignedUser']

order_dtypes = {'_id':'string', 'practiceId': int, 'departmentId':"string", 'deptName':'string', 'dateOrdered':'string',
        'orderName':'string','clinicalOrderTypeId':'string', 'documentId':'string', 'orderingProvider':'string', 
         'orderType':'string', 'orderGenus':'string', 'orderPriority':'string', 'ministry':'string',
        'taoBucket':'string', 'usedTAO':'string', 'performDate':'string','assignedUser':'string'}

def fill_orders_na_with_all(df):
    values = {'orderGenus':'All'}
    return df.fillna(value=values)



def remove_comments(df):
    df['orderName'] = df.apply(lambda row: row['orderName'].split('-')[0], axis=1)
    return df


def get_unique_list(df, columnName):
    orderCount = df.value_counts(columnName)
    counts = [{'name': idx} for idx, val in orderCount.items()]
    return counts


def get_unique_providers(df):
    orderCount = df.value_counts('orderingProvider')
    counts = [{'name': idx, 'value': idx + ' STAFF'} for idx, val in orderCount.items()]
    return counts

def get_order_providers(df):
    provider_list = []
    provider_list = get_unique_providers(df)
    return provider_list

def get_order_genus(df):
    genus_list = []
    genus_list = get_unique_list(df, 'orderGenus')
    return genus_list


def get_genus_orderIds(df):

    genus_df = df[['orderGenus','clinicalOrderTypeId','orderName']]
    genus_group = genus_df.groupby(by=['orderGenus','clinicalOrderTypeId','orderName'])
    genus_order =[]
    for name_of_group,contents_of_group  in genus_group:
        cur_group = {'genus': name_of_group[0],'name': name_of_group[2], 'value': name_of_group[1], }
        genus_order.append(cur_group)
    return genus_order


