#program count number of digits in text string
my_string = 'I have 1 house, 1 car, 1 brother, 2 legs, 2 hands.'
count = 0
for ch in my_string:
    #print(ch)
    if ch.isdigit():
        count += 1

print(count)