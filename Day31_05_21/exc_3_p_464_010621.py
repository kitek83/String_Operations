def main():
    nums = input('Please enter series of numbers.')
    nums2 =str(nums)

    total = 0
    for num in nums2:
        total += int(num)
    print('Sum of series of numbers is:', total)

main()