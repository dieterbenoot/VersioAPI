import requests
from requests.auth import HTTPBasicAuth
user = 'user'
password = 'password'

cat = '/dnstemplates'

session = requests.Session()
session.auth = (user, password)
hostname = 'https://www.versio.nl/testapi/v1'
response = session.get(hostname + cat)


print(response.json())