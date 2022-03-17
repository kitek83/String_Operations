import login_in

def main():
    password = input('Enter the password:')
    while not login_in.valid_passw(password):
        print('Password is not correct')
        password = input('Enter correct passwor.')
    print('Password is correct.')


main()