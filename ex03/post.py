
# self는 heap 공간, this.와 똑같음 new 될 때 대입됨
class Post:
    def __init__(self, username, password): # 생성자
        self.username = username # username은 지역변수를 넣어줌
        self.password = password

p = Post("ssar", "1234")

print(p.username)
print(p.__dict__) # JSON으로 바로 변경 가능