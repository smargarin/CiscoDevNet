import sys
import json
from webbrowser import get
import yaml
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD

# Main funtion
if __name__== "__main__":
 ##############################################
 #     Procedure 1                            #
 # ############################################ 
# Add Print Statement here:
# Add another print statement
    print('DevNet')

##############################################
#             Procedure 2                    #
# ############################################ 

print('##########################')
print('######## YAML ############')
print('##########################')


# Open the user.yaml file as read only
with open('yaml_example1.yaml', 'r') as file:
    user_yaml = yaml.safe_load(file)
    user = user_yaml['user']

print(user['name'])


for role in user['roles']:
    print(role)
    
print(user_yaml)
    
print('##########################')
print('######## JSON ############')
print('##########################')

with open('json_example.json', 'r') as stream:
    user_json = json.load(stream)


print(user_json['user'])

print(user_json)

print('##########################')
print('#######  XML  ############')
print('##########################')


import xml.etree.cElementTree as ET

with open('xml_example.xml', 'r') as stream:
    my_tree = ET.parse(stream)
    my_root = my_tree.getroot()

user = my_root.find('user')

print(type(user))

print(user.find('name').text)
print(user.find('roles').text)
print(user.find('location').find('city').text)














