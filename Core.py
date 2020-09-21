from hashlib import sha256
from os import path
from random import randint

class Password_Manager():
    def __init__(self):
        self.filepath = './helper.txt'
        self.user_data = []
        self.read_file()

    def get_new_salt(self):
        new_salt = ''
        for i in self.user_data:
            new_salt += i[randint(0,len(i)-1)]
            new_salt += i[randint(0,len(i)-1)]
        return new_salt

    def register_client(self):
        print('You are registering... Please remember the info below')
        print('Disclaimer: we do not store this data on our side. ' + 
              'Your Data is safe on your computer.')
        print('Please complete the form below:')
        name = input('name: ').strip().lower()
        lastname = input('lastname: ').strip().lower()
        some_random_info = input('some random info: ').strip().lower()
        important_number = input('an important number to you: ').strip().lower()
        self.user_data = [name,lastname,some_random_info,important_number]
        user_salt = self.get_new_salt()
        self.user_data.append(user_salt)
        self.save_file()
        print('register successful')
    
    def save_file(self):
        o_file = open(self.filepath,'w+')
        for i in self.user_data:
            o_file.write(str(i)+'\n')
        o_file.close()
    
    def print_user_info(self):
        print('name: ' + str(self.user_data[0]))
        print('lastname: ' + str(self.user_data[1]))
        print('your random info: ' + str(self.user_data[2]))
        print('your important number: ' + str(self.user_data[3]))
        print('')
    
    def read_file(self):
        if (not path.exists(self.filepath)):
            print('You are yet to be registered...')
            self.register_client()
        else:
            i_file = open('helper.txt', 'r+')
            for line in i_file.readlines():
                self.user_data.append(line.strip())
            i_file.close()
    
    def get_help(self):
        print('To get a password of yours enter the name of the media' + 
              '\ncommands:'
              '\n    "exit"' + 
              '\n    "reset": To reset your passwords' + 
              '\n    "my_info": to see your info' + 
              '\n    "help": you are already in it\n')
    
    def do_exit(self):
        print('goodbye and goodluck!')
        exit()
    
    def reset(self):
        print('NOTICE: YOU ARE RESETING ALL OF YOUR PASSWORDS!' + 
              ' YOU CANNOT GET YOUR OLDPASSWORDS BACK!\n')
        confirm = input('Continue?(y/n) ').strip().lower()
        if (confirm == 'y' or confirm == 'yes'):
            print('reseting...')
            self.reset_passwords()
            print('done!')
        elif (confirm == 'n' or confirm == 'no'):
            print('reset cancelled')
        else:
            print('invalid input')
    
    def reset_passwords(self):
        self.user_data[-1] = self.get_new_salt()
        self.save_file()

    def run(self):
        print('if you feel lost, use "help"')
        while (1):
            user_input = input('Please Enter Command: ').strip().lower()
            print('')
            if (user_input == 'exit'):
                self.do_exit()
            elif (user_input == 'reset'):
                self.reset()
            elif (user_input == 'my_info'):
                self.print_user_info()
            elif (user_input == 'help'):
                self.get_help()
            else:
                print('getting password for ' + user_input)
                full_stringfied_data = user_input
                for x in self.user_data:
                    full_stringfied_data += str(x)
                    full_stringfied_data += str(x)[0]
                    full_stringfied_data += str(self.user_data[-1])
                final_hash = sha256(full_stringfied_data.encode()).hexdigest()
                print('this is your password: ', end='')
                print(final_hash[10:26])
                print('')


h = Password_Manager()
h.run()
