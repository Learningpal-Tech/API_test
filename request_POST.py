import requests, sys, json, time

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
task_ID = result['task_ID']
status = result['status']
res_url = url + '/result/{}'.format(task_ID)
while status == 'In Progress':
    time.sleep(2)
    response_res = requests.get(res_url)
    status = response_res.json()['status']
    print('\ttask status: {}'.format(status))
    if status == 'Completed':
        result_json = response_res.json()['result']
        with open('get_result.json', 'w') as outf:
            outf.write(json.dumps(result_json, indent=4, sort_keys=True, ensure_ascii=False)) 
