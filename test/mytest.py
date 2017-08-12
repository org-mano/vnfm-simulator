import requests
from requests.auth import HTTPBasicAuth

#url = 'http://192.168.104.30/api/v3/blueprints'
#url = 'http://192.168.104.30/api/v3/version'
#url = 'http://192.168.104.30/api/version2'
#url = 'http://192.168.104.30/api/mytest'
#url = 'http://192.168.104.30/api/v1/mytest'
url = 'http://192.168.104.30/v1/resource/grant'
headers = {'Tenant': 'default_tenant'}
querystring = {'_include': 'value'}

#resp = requests.get(
#    url,
#    auth=HTTPBasicAuth('admin', 'admin'),
#    headers=headers,
#    params=querystring,
#)


resp = requests.put(
    url,
    #auth=HTTPBasicAuth('admin', 'admin'),
    headers=headers,
)


print(resp.status_code)
print(resp.text)

