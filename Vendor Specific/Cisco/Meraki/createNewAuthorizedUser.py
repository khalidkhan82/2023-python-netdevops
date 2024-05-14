import meraki
import os

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = os.environ['MERAKI_DASHBOARD_API_KEY']

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_#########'
email = 'khalidkhan82@gmail.com'
authorizations = [{'ssidNumber': 5, 'authorizedZone': 'MO External', 'expiresAt': 'Never'}]

response = dashboard.networks.createNetworkMerakiAuthUser(
    network_id, email, authorizations, 
    name='Khalid Mehmood', 
    password='######', 
    accountType='Guest', 
    emailPasswordToUser=False, 
    isAdmin=False
)

print(response)