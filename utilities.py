

def fill_na_with_all(df):
    values = {"Provider ID": "All", "Order Type ID":"All", "Order Type":"All",}
    return df.fillna(value=values)

def create_value_pairs(row, name_column, value_column):
    depts = {}
    print('row ', row)
    if(row[name_column] == 'All'):
        depts[name_column] = 'All'
        return depts
    else:
        department_names = row[name_column].split(',')
        department_ids = row[value_column].split(',')
        # print('department names ', department_names)
        for x, y in zip(department_names, department_ids):
            # print('dept', x)
            depts[x] = y
            # print(depts)
    return depts


def create_orders(row, name_column, value_column):
    print('row ', row)
    depts = {}
    if(row[name_column] == 'All'):
        depts[name_column] = 'All'
        return depts
    else:
        depts[row[name_column]] = row[value_column]
    return depts


def add_departments(df):
    df['depts'] = df.apply(lambda row: create_value_pairs(row, 'Department', 'Department ID'), axis=1)
    return df

def add_providers(df):
    df['providers'] = df.apply(lambda row: create_value_pairs(row, 'Provider', 'Provider ID'), axis=1 )
    return df

def add_orders(df):
    print('df', df['Order Type'])
    df['orders'] = df.apply(lambda row: create_orders(row, 'Order Type', 'Order Type ID'), axis=1 )
    return df