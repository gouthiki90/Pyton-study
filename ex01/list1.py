# 리스트 슬라이싱
print('='*60)

# 리스트 만들기
list = [1, 2, 3, 4]
list2 = ['1', 2, '3', 4]

print(list[0])

# 리스트 추가하기
list.append(5)
print(list)

# 리스트 요소 제거
del list[0] 
print("0번지 제거", list)

# 리스트 정렬
list3 = [3, 1, 2]
list3.sort()
print(list3)
list3.reverse()
print(list3)

# 리스트 값의 위치 찾기
print(list3.index(3))

# 문자열 슬라이싱
# char가 모인 배열이 문자열이니까 번지수 찾을 수 있음
str1 = "안녕하세요"
print(str1[0])
print(str1[0:5]) # 시작위치:끝위치
print(str1[-1]) # 마지막 문자 가져옴
print(str1[1:]) # 끝까지 감
