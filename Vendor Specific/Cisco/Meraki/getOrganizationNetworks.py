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

response = dashboard.organizations.getOrganizationNetworks(
    organization_id, total_pages='all'
)

#responseDict = {}
listOfNetworks = []
dictOfNetworks = Box({})
i = 1

for item in response:
#   listOfNetworks.append(item['name'])
    dictOfNetworks[f'Network{i}'] = item['name']
    i += 1

#response_dict = json.loads(response)

#print(listOfNetworks)
#print(dictOfNetworks.Network1)
print(response[0])
#print(responseDict)