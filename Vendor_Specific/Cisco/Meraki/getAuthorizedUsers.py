import meraki
import json
from box import Box

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '#######'

dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

organization_id = '######'

responseNetworks = dashboard.organizations.getOrganizationNetworks(
    organization_id, total_pages='all'
)

networkIds = []
networkNames = []
list_of_users = []
i = 1


for item in responseNetworks:
    networkIds.append(item['id'])
    networkNames.append(item['name'])

for id in networkIds:
    responseUsers = dashboard.networks.getNetworkMerakiAuthUsers(id)
    for user in responseUsers:
        list_of_users.append(user['email'])
    #print(f'users in network {id} are: ', list_of_users)
    print(f'number of users in network {id} are: ', len(list_of_users))




