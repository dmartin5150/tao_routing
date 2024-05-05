
from providers import get_providers
from genus import get_genus, get_genus_orderIds
from departments import get_departments


def get_dropdowns(df_orders, df_rules):
    get_genus_orderIds(df_orders)
    providers= {'providers': get_providers('fljac_providers.json')}
    genus = {'genus': get_genus(df_orders)}
    genus_orders = {'genusOrders':get_genus_orderIds(df_orders)}
    departments = {'departments': get_departments(df_rules)}
    return {'providers': providers, 'genus':genus, 'genus_orders':genus_orders,'departments':departments}

