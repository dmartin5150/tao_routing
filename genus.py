def get_genus(df):
    genus_df = df[['orderGenus']]
    genus_group = genus_df.groupby(by=['orderGenus'])
    genus =[]
    for name_of_group,contents_of_group  in genus_group:
        cur_group = {'name': name_of_group[0]}
        genus.append(cur_group)
    return genus

def get_genus_orderIds(df):

    genus_df = df[['orderGenus','clinicalOrderTypeId','orderName']]
    genus_group = genus_df.groupby(by=['orderGenus','clinicalOrderTypeId','orderName'])
    genus_order =[]
    for name_of_group,contents_of_group  in genus_group:
        cur_group = {'genus': name_of_group[0],'name': name_of_group[2], 'value': name_of_group[1], }
        genus_order.append(cur_group)
    return genus_order
