# 함수 (클래스 내부에 있는 것이 아닌 것들은 함수이다.)
def add():
    print("더하기")

def minus():
    return 1

add()
n = minus()

print(n)

def multi(n2, n1 = 3): # 디폴트값이 있는 것은 앞에다 둬야 됨
    print(f"곱하기{n1}*{n2}")

#multi(3, 2)

multi(2) # 오버로딩

#dic 변환 문법
def my_dict(**data): # 인수가 두 개인 것을 합쳐준다.
    print(data)
    pass

# 키값이 반드시 있어야 됨
my_dict(id=1, username="ssar") # 이렇게 인수가 두 개

# 1급 객체, 외부에 혼자 있으니까, 타입이 없어서 뭘 쓰는 지 모름, 그래서 선언 해줘야 됨
n1 = 1 # 전역 변수로 쓰려면 어떻게?

def vartest():
    global n1 # 전역 변수를 사용하겠다고 선언
    n1 = 2 # 지역 변수

vartest()
print(n1)

