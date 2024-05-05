import pandas as pd
from flask import Flask,  request
from flask_cors import CORS
import json

# from utilities import  get_departments
from orders import order_dtypes, fill_orders_na_with_all, remove_comments
from providers import get_providers
from routing import route
from tao_rules import get_tao_rules, add_new_route
from departments import get_departments
from genus import get_genus, get_genus_orderIds
from drop_downs import get_dropdowns


app = Flask(__name__)
CORS(app)
app.secret_key = "seamless care" # for encrypting the session
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


athena_tao_rules = get_tao_rules('TAO.csv','FL - Ascension - Florida')
tao_orders = pd.read_csv('TAOOrders.csv', dtype=order_dtypes)
tao_orders = fill_orders_na_with_all(tao_orders)
tao_orders = remove_comments(tao_orders)
drop_downs = get_dropdowns(tao_orders,athena_tao_rules)
print(drop_downs[0])
athena_tao_rules = add_new_route(athena_tao_rules,'-1', ['New Deparment'],['New DepartmentID'],['All'],['All'],'-1',['All'],['All'],['All'])
# print(athena_tao_rules[athena_tao_rules['TAO ID'] == '-1'])
# routes = route(athena_tao_rules, 'All', 'All', 'All', 427181).sort_values(by='Ordering')



def get_data(request, string):
    data_requested = request[string]
    return data_requested


@app.route('/dropdowns', methods=['GET'])
def get_all_dropdowns_async():
    drop_downs = get_dropdowns(tao_orders,athena_tao_rules)
    return json.dumps(drop_downs), 200


app.run(host='0.0.0.0', port=5001)