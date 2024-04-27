import pandas as pd

from utilities import fill_na_with_all,add_departments, add_providers,add_orders;

taos_raw_data = pd.read_csv('TAO.csv')

tao_fl = taos_raw_data[taos_raw_data['CONTEXT_NAME'] == 'FL - Ascension - Florida']
tao_fl = fill_na_with_all(tao_fl)

tao_fl = add_departments(tao_fl)
tao_fl = add_providers(tao_fl)
tao_fl = add_orders(tao_fl)

print (tao_fl['orders'])