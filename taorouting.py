import pandas as pd

# from utilities import  get_departments
from orders import order_dtypes, fill_orders_na_with_all, remove_comments
from providers import get_providers
from routing import route
from tao_rules import get_tao_rules, add_new_route
from departments import get_departments
from genus import get_genus, get_genus_orderIds
from drop_downs import get_dropdowns


athena_tao_rules = get_tao_rules('TAO.csv','FL - Ascension - Florida')

tao_orders = pd.read_csv('TAOOrders.csv', dtype=order_dtypes)
tao_orders = fill_orders_na_with_all(tao_orders)
tao_orders = remove_comments(tao_orders)
drop_downs = get_dropdowns(tao_orders,athena_tao_rules)
add_new_route(athena_tao_rules,'-1', ['All'],['All'],['All'],['All'],'-1',['All'],['All'],['All'])
# print(drop_downs['departments'])
# get_genus_orderIds(tao_orders)
# print(get_genus(tao_orders))
# print(get_genus_orderIds(tao_orders))
# print(get_order_providers(tao_orders))
# print(get_order_genus(tao_orders))
# print(departments)
# print(athena_data_frame['Order Type ID'])
# print(get_departments(athena_tao_rules))
# tao_orders = pd.concat([pd.DataFrame([new_row]), tao_orders], ignore_index=True) 
# get_providers('fljac_providers.json')
# print(athena_data_frame.columns)
# print(athena_data_frame[athena_data_frame['Department ID'] == '768'])
# routes = route(athena_tao_rules, 'All', 'All', 'All', 427181).sort_values(by='Ordering')
# print(routes[['TAO ID','Ordering','Assigned To']])
# print(athena_data_frame[athena_data_frame['TAO ID'] == 7787 ])