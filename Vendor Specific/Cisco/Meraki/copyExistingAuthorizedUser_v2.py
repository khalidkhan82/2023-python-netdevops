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

organization_id = '####' # MO's Organization ID

# Uses a the following GET API request
# {{baseUrl}}/organizations/{{organizationId}}/networks 
responseNetworks = dashboard.organizations.getOrganizationNetworks(
    organization_id, total_pages='all'
)

# We're saving the list of network IDs, network Names and the user emails in these lists
networkIds = []
networkNames = []

user_is_missing = []
dct_of_missing_users = {}
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

del dct_of_lists['network_L_714946440845072487']
del dct_of_lists['network_N_3741928340391462989']
del dct_of_lists['network_N_3741928340391463008']

#print(dct_of_lists)


for network, users in dct_of_lists.items():
    user_is_missing=[]
    for user in users:
        for n, u in dct_of_lists.items():
            if user not in u:    # evaluates whether the user is in the list of user for the particular network
                user_is_missing.append(user)  # if the user is not in the list, add it to the list of missing users  
        # create a dictionary for that particular network and add missing users to it
        dct_of_missing_users['%s' % n] = user_is_missing


for key, value in dct_of_missing_users.items():
    print(key, len(value), '\n')


