#the functon will return initials of the name
def main():
    name = input('Enter your name:')
    surname = input('Enter your  surname:')
    print(get_initials(name,surname))

def get_initials(first, last):
    set1 = first[0:1]
    set2 = last[0:1]
    initials = set1 + set2
    return initials

main()