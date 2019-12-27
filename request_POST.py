import requests, sys, json

url = 'http://test.learningpal.com:8887'
if len(sys.argv) > 1:
    f = open(sys.argv[1], 'rb')
else:
    f = open('./sample1.png', 'rb')

files = {'file': f}
data = {'lang': 'JPN'}
response = requests.post(url, files=files)
result = response.json()

with open('get_result.json', 'w') as outf:
    outf.write(json.dumps(result, indent=4, sort_keys=True)) 
