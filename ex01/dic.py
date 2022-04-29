
# dictionoary 타입, JSON이랑 똑같음

import json

dic1 = {
    "id":1,
    "username":"cos"
}

print(dic1)

# string 타입
dic2 = '''
{"id":1, "username":"cos"}
'''
print(dic2)

print(type(dic1))
print(type(dic2))

print(dic1)
print(dic1["username"])

dic3 = json.loads(dic2) # JSON으로 만들고

print(dic3["id"]) # JSON 파싱한 데이터 찾기