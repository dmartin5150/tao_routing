import pandas as pd


def get_providers(fileName):
    providers_df = pd.read_json(fileName)
    providers = providers_df["providers"]
    provider_list = []
    provider_staff_list = []
    for provider in providers:
        if provider['entitytype'] == 'Person':
            curProvider = {'name': provider['displayname'], 'value': provider['providerid']}
            curBucket = {'name': provider['displayname'] + ' STAFF', 'value': provider['providerid']  }
            provider_list.append(curProvider)
            provider_staff_list.append(curBucket)
    return provider_list, provider_staff_list

        