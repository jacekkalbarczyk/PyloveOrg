import requests
resp = requests.get('http://py.net/query_string?onawidziwemnie_co=piniadz&Coca=Cola')
from pprint import pprint
pprint(resp.args)