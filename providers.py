import pandas as pd


def get_providers(fileName):
    providers_df = pd.read_json(fileName)
    providers = providers_df["providers"]
    provider_list = [{'label': 'All', 'value': '0'}]
    provider_staff_list = []
    for provider in providers:
        if provider['entitytype'] == 'Person':
            curProvider = {'label': provider['displayname'], 'value': provider['providerid']}
            curBucket = {'label': provider['displayname'] + ' STAFF', 'value': provider['providerid']  }
            provider_list.append(curProvider)
            provider_staff_list.append(curBucket)
    return provider_list, provider_staff_list

        