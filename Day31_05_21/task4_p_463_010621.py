my_string = 'Today is cloudy weather.'
count =0
for ch in my_string:
    if ch.islower():
        count += 1
print('There are',count,'lowercases in the text.')
