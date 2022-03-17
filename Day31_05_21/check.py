nums = '1234'
nums2 = nums.split('/')
print(nums2)
total = 0
for x in nums:
    total += int(x)
print(total)
print('####################')
date = '01/06/2021'
print(date.split('/'))
date2 = date.split('/')
print(date2[1])
if date2[1] == '06':
    date2[1] = 'June'
print('---------------')
print(date2)
for x in date2:
    print(x, end='.')