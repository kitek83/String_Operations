import login_in
def main():
    name = input('Enter Your name:')
    last = input('Enter you surname:')
    id = input('Enter you id nr:')
    #login_in(name,last,id)
    print('Your login is:')
    print(login_in.login_in(name,last,id))
main()