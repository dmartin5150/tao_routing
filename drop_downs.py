
from providers import get_providers
from genus import get_genus, get_genus_orderIds
from departments import get_departments



def get_dropdowns(df_orders, df_rules):
    get_genus_orderIds(df_orders)
    providers= {'name': 'Provider', 'options': get_providers('fljac_providers.json')}
    genus =  get_genus(df_orders)
    genus_orders = get_genus_orderIds(df_orders)
    departments = get_departments(df_rules)
    return [providers, {'name':'Genus', 'options': genus}, {'name': 'OrderType', 'options': genus_orders},{'name':'Department', 'options': departments}]

