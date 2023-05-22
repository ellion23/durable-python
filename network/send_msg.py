#!/usr/bin/python3
import json
code, log, psw = map(str, input("code, log, psw: ").split())
x = {
    'code': int(code),
    'login': log,
    'password': psw
}
y = json.dumps(x)
print(y)
