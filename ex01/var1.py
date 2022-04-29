# 파이썬 자료형

# 정수
n1 = 1

# 실수
n2 = 1.1

# 문자열
# 전부 다 객체이고 포인터, 인터프리터 언어이기 때문에 모두 4Byte로 잡음
# 공간은 모두 heap의 포인터에 있겠다
s1 = '문자'

# 긴문자열
# 스트링빌더처럼 문자열을 합칠 수 있다.
s2 = '''
안녕하세요
반갑습니다
안녕히 가세요
'''

# 문자 안에 쌍따옴표 추가
# + 안 해도 됨
s3 = '그는 말했다. 왈 "반가워"라고'

# 문자 안에 변수 바인딩 f-str f'내용{변수}'
username = '홍길동'
s4 = f'안녕 내 이름은 {username}야'

print(n1)
print(n2)
print(s1)
print(s2)
print(s3)
print(s4)

print('='*30)

print(type(n1))
print(type(n2))
print(type(s1))
print(type(s2))
print(type(s3))
print(type(s4))