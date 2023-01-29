# Input things
length = int(input())
nums = []
for _ in range(length):
    num = int(input())
    nums.append(num)

# Read lists from end to start
# Found 0, mistake should exist following list
miss = 0
result = 0
for i in range(len(nums)):
    thisNum = nums[len(nums) - i - 1]
    if thisNum == 0:
        miss += 1
    elif miss != 0:
        miss -= 1
    else:
        result += thisNum

# Print result
print(result)
