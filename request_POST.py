import requests, sys, json

url = 'http://test.learningpal.com:8887'
lang = 'eng'
if len(sys.argv) == 2:
    f = open(sys.argv[1], 'rb')
elif len(sys.argv) == 3:
    f = open(sys.argv[1], 'rb')
    lang = sys.argv[2]
elif len(sys.argv) == 1:
    f = open('./sample1.png', 'rb')
else:
    print('How to use: \npython <file_pathe> <language(option)>')
    sys.exit()

files = {'file': f}
data = {'lang': lang} # speicify language in data
response = requests.post(url, files=files, data=data)
result = response.json()

with open('get_result.json', 'w') as outf:
    outf.write(json.dumps(result, indent=4, sort_keys=True, ensure_ascii=False)) 
