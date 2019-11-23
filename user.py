from werkzeug import generate_password_hash, check_password_hash

class User_info:
    '''
    该类用于创建用户账号
    '''

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = self.save_password(password)

    def check_email(self, email):
        return self.email == email

    def save_password(self, password):
        '''生成hash密码的方法
        '''
        return generate_password_hash(password)

    def check_password(self, password):
        '''检查hash密码的方法
        '''
        return check_password_hash(self.password_hash, password)


def main():
    userList = []
    print('------Welcome------')
    while True:
        choice = int(input('''
        请通过数字选择：
        1. 注册
        2. 登录
        3. 退出
        '''))
        if choice == 1:
            print('请输入： ')

            name = input('Name: ')
            email = input ('Email: ')
            password = input('Password: ')

            newUser = User_info(name, email, password)
            userList.append(newUser)
            print(newUser)

        if choice == 2:
            print('请输入： ')
            email = input('Email: ')
            password = input('Password: ')
            inList = False
            for user in userList:
                if user.check_email(email):
                    inList = True
                    if user.check_password(password):
                        print(' 登录成功')
                    else:
                        print(' 用户名或密码错误')
                    break
            if inList == False:
                print(' 请输入正确的 email')

        if choice == 3:
            break
   
if __name__ == '__main__':
    main()