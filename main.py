import hashlib


class Member:
    name = ""
    username = ""
    password = 1234

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        m = hashlib.sha256()

        self.password = m.update(password.encode('utf-8'))

    def display(self):
        print(f'이름 : {self.name}, 아이디 : {self.username}')


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


posts = []
members = []
members.append(Member('kim', 'kim123', 'password123'))
members.append(Member('lee', 'lee456', 'password456'))
members.append(Member('jo', 'jo789', 'password789'))
