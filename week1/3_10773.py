# Input things
length = int(input())
nums = []
for _ in range(length):
    num = int(input())
    nums.append(num)

miss = 0
result = 0
for i in range(len(nums)):
    # Read lists from end to start
    thisNum = nums[len(nums) - i - 1]
    # Found 0, mistake should exist following list
    if thisNum == 0:
        miss += 1
    # Do not add number, decrease miss
    elif miss != 0:
        miss -= 1
    # Add number when miss not exist
    else:
        result += thisNum

# Print result
print(result)
