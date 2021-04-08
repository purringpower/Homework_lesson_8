users_list = ['Masha', 'Vasya', 'Kostya', 'Vika']

login = input('Enter your login:')


def decorator_func(func):
    def wrapper():
        if login not in users_list:
            print("You cant see a secret!")
        else:
            func()

    return wrapper


@decorator_func
def secret():
    print('There is a secret message for you,', login, "<3")


secret()
