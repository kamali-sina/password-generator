from hashlib import md5,sha256
from os import path

class Password_Manager():
    def __init__(self):
        self.filepath = './helper.txt'
        self.user_data = []
        self.read_file()

    def register_client(self):
        o_file = open(self.filepath,'w+')
        print('You are yet to be registered... Please remember the info below')
        print('Please complete the form below:')
        name = input('name: ').strip()
        lastname = input('lastname: ').strip()
        some_random_info = input('some random info: ').strip()
        an_important_number = input('an important number to you: ').strip()
        o_file.write(name+'\n')
        o_file.write(lastname+'\n')
        o_file.write(some_random_info+'\n')
        o_file.write(an_important_number+'\n')
        o_file.close()
        print('register successful')

    def read_file(self):
        if (not path.exists(self.filepath)):
            self.register_client()
        i_file = open('helper.txt', 'r+')
        for line in i_file.readlines():
            self.user_data.append(line.strip())
        i_file.close()




h = Password_Manager()
m = sha256()
x = 'sina'
x = x.encode('utf-8')
m.update(x)
print(m.hexdigest())