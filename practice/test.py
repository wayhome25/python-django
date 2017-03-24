class Text:
    def __init__(self, str):
        self.text = str

    def __str__(self):
        return "Text Class " + self.text

    def getLength(self):
        return len(self.text)

class Article(Text): #Article 클래스(자식클래스)는 Text 클래스(부모클래스, 슈퍼클래스)를 상속 받았다.
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __str__(self):
        return 'Article Class %s %s' % (self.title, self.text)

class User:
    numUsers = 0 # 클래스 변수
    def __init__(self, name):
        self.numArticle = 0 # 인스턴스 변수로 초기화
        self.name = name
        self.articles = [] # 인스턴스 변수
        User.numUsers += 1

    def write(self, text):
        self.articles.append(text)
        self.numArticle += 1

    def __str__(self):
        return "%s, %s" % (self.name, ' / '.join(str(p) for p in self.articles))

t = Article('hello', 'This is some text') # Text Class This is some text
t2 = Article('hello2', 'This is some text2')
user = User('monkey') # User Class : monkey []
user.write(t)
user.write(t2)

# print([t][0])
print(t,', ',t.getLength()) # Article Class hello This is some text ,  17
print(user,',',user.numArticle)
# monkey, Article Class hello This is some text / Article Class hello2 This is some text2 , 2
