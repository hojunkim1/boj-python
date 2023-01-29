# Coding as more common way
length = int(input())
nums = []
for _ in range(length):
    num = int(input())
    if num == 0:
        nums.pop()
    else:
        nums.append(num)

result = 0
for num in nums:
    result += num

print(result)
