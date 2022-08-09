#Modified this original example.py from the Threatstack Github to prompt for keys and export high vulnerabilties with Security Notices to CSV (WIP) 
#Source https://github.com/threatstack/rest-api-examples/tree/master/python
from mohawk import Sender
import requests
import os
import sys
import csv
 
 
def get_or_throw(key_name):
    res = os.getenv(key_name, None)
    if res is None:
        print("Environment variable '" + key_name + "' is required.")
        sys.exit(1)
    return res
 
 
HOST = os.getenv("TS_HOST", 'api.threatstack.com')
USER_ID = input("Enter TS_USER_ID = ")
ORGANIZATION_ID = input("Enter TS_ORGANIZATION_ID = ")
API_KEY = input("Enter TS_API_KEY = ")
 
BASE_PATH = 'https://' + HOST
URI_PATH = '/v2/vulnerabilities?status=active&hasSecurityNotices=true&severity=high&severity=high'
 
credentials = {
    'id': USER_ID,
    'key': API_KEY,
    'algorithm': 'sha256'
}
URL = BASE_PATH + URI_PATH
sender = Sender(credentials, URL, "GET", always_hash_content=False, ext=ORGANIZATION_ID)
 
response = requests.get(URL, headers={'Authorization': sender.request_header})
print(response.text)
# Note a warning is logged out during the authenticate call:
# seen_nonce was None; not checking nonce. You may be vulnerable to replay attacks
# This is not an issue because the nonce is randomly generated above and a different
# nonce is used for each request.
sender.accept_response(response.headers['Server-Authorization'],
                       content=response.text,
                       content_type=response.headers['Content-Type'])
 
# accept_response will throw if the response is not authentic
# after this call we know the response is authentic
print('Response is authentic')

#print to CSV WIP
file = open('C:\output.csv', 'w')
writer = csv.writer(file)
writer.writerow(response)
file.close()
print('File output to C:\output.csv')
