import pandas as pd

from utilities import fill_na_with_all,create_routing_table,add_departments_and_providers;

taos_raw_data = pd.read_csv('TAO.csv')
providers = {'NF':'-1'}
departments = {'NF':'-1'}
providers.setdefault('NF','-1')
departments.setdefault('NF', '-1')


columns = ['CONTEXT_ID', 'CONTEXT_NAME', 'TAO ID', 'Last Modified Date',
       'Document Class/Subclass', 'Document Class/Subclass ID', 'Ordering',
       'Action', 'Next Status', 'Department', 'Department ID', 'Provider',
       'Provider ID', 'Order Type', 'Order Type ID', 'Order Genus',
       'Assigned To']

athena_data_frame = pd.DataFrame(columns=columns)

tao_fl = taos_raw_data[taos_raw_data['CONTEXT_NAME'] == 'FL - Ascension - Florida']
tao_fl = fill_na_with_all(tao_fl)
departments, providers = add_departments_and_providers(tao_fl,departments,providers)
athena_data_frame = create_routing_table(tao_fl,departments,providers,athena_data_frame)
# athena_data_frame.to_csv('athena.csv')
print(athena_data_frame)
# print (tao_fl.columns)
# print (create_routing_table(tao_fl))