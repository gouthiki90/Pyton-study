# 파이썬은 언제 클래스를 써야 할까?
# 찍어내야 할 때 사용한다.
# 추상적인 설계를 한 후에 new 해서 찍어내야 할 때.
# 자료형으로 사용할 필요는 없다.

class User: # static이 아닌 것을 빼고 안 뜸
    username = "ssar"
    password = "1234"

def hello(): # 메모리 안 뜸, 호출해야 돼서
    n1 = 10

