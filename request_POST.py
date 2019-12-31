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
res_url = url + '/results/{}'.format(task_ID)
idx = 1
while status == 'In Progress':
    time.sleep(3)
    response_res = requests.get(res_url)
    status = response_res.json()['status']
    status_display = '\tTask status: {}... {}s has passed'.format(status, (idx * 3))
    print(status_display, end="\r")
    idx += 1
    if status == 'Completed':
        result_json = response_res.json()['result']
        with open('get_result.json', 'w') as outf:
            outf.write(result_json)
        print("\r{}, result JSON save to {}".format(status_display, 'get_result.json'))
