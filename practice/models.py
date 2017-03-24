class User:
    num_users = 0 # class 변수
    def __init__(self, name):
        self.name = name # instance 변수 (메소드 안에서 self라는 키워드를 사용해서 선언하는 변수)
        User.num_users += 1

u = User('monkey')
print(User.num_users, u.name)
u2 = User('sunshine')
print(User.num_users, u2.name)
print(User.num_users, u.num_users, u2.num_users)
# 클래스 변수는 모든 인스턴스들 간에 값을 공유한다. 
# class User의 인스턴스 u, u2 모두 똑같은 num_users 값을 가진다.

# class Text:
#     # pass # 아무것도 안하겠다는 의미
#     def __init__(self, str):
#         self.text = str
#
#     def __str__(self):
#         return "Object: " + self.text
#
# t = Text("hi")
# print(t) # Object: hi
# print(t.text) # hi
