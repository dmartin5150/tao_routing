def get_genus(df):
    genus_df = df[['orderGenus']]
    genus_group = genus_df.groupby(by=['orderGenus'])
    genus =[{'label': 'All', 'value': '0'}]
    i = 1
    for name_of_group,contents_of_group  in genus_group:
        if name_of_group[0] == 'All':
            continue
        cur_group = {'label': name_of_group[0], 'value': i}
        genus.append(cur_group)
        i += 1
    return  genus

def get_genus_orderIds(df):

    genus_df = df[['orderGenus','clinicalOrderTypeId','orderName']]
    print('pre', genus_df.shape[0])
    genus_df = genus_df.drop_duplicates(subset='clinicalOrderTypeId')
    print('post', genus_df.shape[0])
    # print('ordergenus', genus_df)
    genus_group = genus_df.groupby(by=['orderGenus','clinicalOrderTypeId','orderName'])
    genus_order =[{'superset': 'All', 'label':'All', 'value':'0'}]
    for name_of_group,contents_of_group  in genus_group:
        if (name_of_group[0]  == 'All') | (name_of_group[1] == 'All'):
            continue
        cur_group = {'superset': name_of_group[0],'label': name_of_group[2], 'value': name_of_group[1]} 
        # print('superset', cur_group)
        genus_order.append(cur_group)
    
    return genus_order
