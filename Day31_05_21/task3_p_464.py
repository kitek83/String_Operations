#program convert date in format dd/mm/rrrr on dd.month.rrrr
def main():
    date = input('Enter the date in the format dd/mm/rrrr:')
    #creating the list
    date2 = date.split('/')
    if date2[1] == '01':
        date2[1] = 'January'
    elif date2[1] == '02':
        date2[1] = 'February'
    elif date2[1] == '03':
        date2[1] = 'March'
    for day in date2:
        print(day, end='.')

main()