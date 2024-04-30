import pandas as pd

from utilities import fill_na_with_all,create_routing_table,get_genus, get_departments,update_routing_rows,add_departments_and_providers
from orders import order_dtypes, fill_orders_na_with_all, remove_comments,get_order_providers, get_order_genus,get_genus_orderIds
from providers import get_providers

columns = ['CONTEXT_ID', 'CONTEXT_NAME', 'TAO ID', 'Last Modified Date',
       'Document Class/Subclass', 'Document Class/Subclass ID', 'Ordering',
       'Action', 'Next Status', 'Department', 'Department ID', 'Provider',
       'Provider ID', 'Order Type', 'Order Type ID', 'Order Genus',
       'Assigned To']


taos_raw_data = pd.read_csv('TAO.csv')
tao_orders = pd.read_csv('TAOOrders.csv', dtype=order_dtypes)


providers = {}
departments = {}
genus = []
order_providers = {}
order_genus = {}
order_buckets = {}


athena_data_frame = pd.DataFrame(columns=columns)

tao_fl = taos_raw_data[taos_raw_data['CONTEXT_NAME'] == 'FL - Ascension - Florida']
tao_fl = fill_na_with_all(tao_fl)
tao_fl = update_routing_rows(tao_fl)
departments, providers = add_departments_and_providers(tao_fl,departments,providers)
genus = get_genus(tao_fl)
athena_data_frame = create_routing_table(tao_fl,departments,providers,athena_data_frame)

tao_orders = fill_orders_na_with_all(tao_orders)
tao_orders = remove_comments(tao_orders)
get_genus_orderIds(tao_orders)
# print(get_order_providers(tao_orders))
# print(get_order_genus(tao_orders))
# print(departments)
# print(athena_data_frame['Order Type ID'])
# print(get_departments(athena_data_frame))

# tao_orders = pd.concat([pd.DataFrame([new_row]), tao_orders], ignore_index=True) 
get_providers('fljac_providers.json')