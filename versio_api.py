## requests to easy handle REST requests
import requests
import socket
import configparser
from requests.auth import HTTPBasicAuth

## read from config file

config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

## fill credentials

user = config['DEFAULT']['username']
password = config['DEFAULT']['password']
cat = config['DEFAULT']['cat']

print(user, password, cat)

## create request sesion 

session = requests.Session()

## Obtain public IP
ip = session.get('https://api.ipify.org').text
print(ip)

#session.auth = (user, password)
#hostname = 'https://www.versio.nl/testapi/v1'
#response = session.get(hostname + cat)


#print(response.json())