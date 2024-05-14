import meraki
import json
from box import Box
import os

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = os.environ['MERAKI_DASHBOARD_API_KEY'] # MO's Meraki API Key - Use the non-SAML admin to obtain the key

# The dashboard URL - its global (except for China which has .cn domain)
# https://api.meraki.com/api/v1
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True) 

organization_id = '######' # MO's Organization ID

# Uses a the following GET API request
# {{baseUrl}}/organizations/{{organizationId}}/networks 
responseNetworks = dashboard.organizations.getOrganizationNetworks(
    organization_id, total_pages='all'
)

# We're saving the list of network IDs, network Names and the user emails in these lists
networkIds = []
networkNames = []

list_missing_users = []
dict_missing_users = {}
dct_of_lists = {}

'''
def createUser(dct_of_lists, list_of_users_to_create): # arguments = dict of lists of users, and the list of users to create
    for net, users in dct_of_lists:                    # we go over the dict of lists of users 
        temp_networks = dct_of_lists                   # we create a temp dic
        del temp_networks[f'net']                      # we delete the current network from the temp dictionary
        for user_to_create in list_of_users_to_create:
            for 
'''

for item in responseNetworks:
    networkIds.append(item['id'])
    networkNames.append(item['name'])

for id in networkIds:
    list_of_users = []
    responseUsers = dashboard.networks.getNetworkMerakiAuthUsers(id)
    for user in responseUsers:
        list_of_users.append(user['email'])
    dct_of_lists['network_%s' % id] = list_of_users # create new dicstionary for each of our networks and add list of users

#del dct_of_lists['network_L_714946440845072487']
#print(dct_of_lists)


for network, users in dct_of_lists.items():
    #dict_missing_users[f'network'] = {}
    temp_dict = dct_of_lists.copy()
    #print(temp_dict.keys())
    del temp_dict[f'{network}']
    #print(temp_dict.keys())
    for user in users:
        for network2, existing_users in temp_dict.items():
            print(network, user)
            if user not in existing_users:
                    #print(f'user does not exist in {network2}', user)
                    list_missing_users.append(user)
            dict_missing_users[f'{network2}'] = list_missing_users
                    
#print("Missing Users", dict_missing_users.keys())



#for item in dct_of_lists.values():
#    print(len(item))

