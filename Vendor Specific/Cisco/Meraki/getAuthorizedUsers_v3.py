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

organization_id = '#######' # MO's Organization ID

# Uses a the following GET API request
# {{baseUrl}}/organizations/{{organizationId}}/networks 
responseNetworks = dashboard.organizations.getOrganizationNetworks(
    organization_id, total_pages='all'
)

# We're saving the list of network IDs, network Names and the user emails in these lists
networkIds = []
networkNames = []
list_of_users = []

dct_of_lists = {}

for item in responseNetworks:
    networkIds.append(item['id'])
    networkNames.append(item['name'])

for id in networkIds:
    #dct_of_lists['network_%s' % id] = []
    responseUsers = dashboard.networks.getNetworkMerakiAuthUsers(id)
    for user in responseUsers:
        list_of_users.append(user['email'])
    dct_of_lists['network_%s' % id] = list_of_users

for item in dct_of_lists.values():
    print(len(item))

for network, users in dct_of_lists.items():
    for user in users:
        for existing_users in dct_of_lists.values():
            if user not in existing_users:
                existing_users.append(user)


for item in dct_of_lists.values():
    print(len(item))





