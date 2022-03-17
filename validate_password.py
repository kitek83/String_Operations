import exlogin
passw = input('Enter the password.')
while not exlogin.valid_password(passw):
    print('Password is not correct.')
    passw = input('Enter the correct password.')
print('Password is correct.')
