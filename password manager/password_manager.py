from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key) 
write_key()'''


def read_key():
    file = open('key.key','rb')
    key = file.read()
    file.close()
    return key

key = read_key()
fer = Fernet(key)
     

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print('User name: ',user ,',Password:',fer.decrypt(passw.encode()).decode())
            

def new_pass():
    name = input('Enter account name: ')
    password = input('Enter password: ')
    
    with open('password.txt','a') as f:
        f.write(name + '|' + fer.encrypt(password.encode()).decode() + '\n')
    


while True:
    mode = input('\nEnter your choice\nv: for view existing password\nn: for store new password\nq: for quit:').lower()
    if mode == 'q':
        break
    
    if mode == 'v':
        view()
    elif mode == 'n':
        new_pass()
    else :
        print("Invalid mode !.Please enter correct mode.")
        continue