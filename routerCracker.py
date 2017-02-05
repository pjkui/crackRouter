# coding=utf-8

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
    pwd1 = seurityEncode('1234')
    print(pwd1)
    pwd1 = seurityEncode('1111')
    print(pwd1)


if __name__ == '__main__':
    main()
