import requests, sys, json

url = 'http://test.learningpal.com:8887'
if len(sys.argv) > 1:
    f = open(sys.argv[1], 'rb')
else:
    f = open('./sample1.png', 'rb')

files = {'file': f}
data = {'lang': 'jpn'}
response = requests.post(url, files=files, data=data)
result = response.json()

with open('get_result.json', 'w') as outf:
    outf.write(json.dumps(result, indent=4, sort_keys=True, ensure_ascii=False)) 
