import configparser

## creating config file with following structure
# 
#   [DEFAULT]
#   username =  "username"
#   password = "password"
#   URL = 'http://ipv4.icanhazip.com/'
##

user = input("Username: ")
password = input("Password: ")
cat = input("Categorie: ")

config = configparser.ConfigParser()
config['DEFAULT'] = {
    'username': user,
    'password': password,
    'cat' : cat
}
with open('config.ini', 'w') as configfile:
    config.write(configfile)
