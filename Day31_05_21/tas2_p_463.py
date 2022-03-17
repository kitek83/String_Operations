#this program shows how many apeces are in the text string
my_string = 'Ma favorite food is chocolate.'
count = 0
for ch in my_string:
    if ch == ' ':
        count += 1
print('There are ', count, 'spaces in my_string')
