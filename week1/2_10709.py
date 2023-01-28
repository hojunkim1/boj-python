# Input height and width
h, w = map(int, input().split())

# Save cloud information as list of string
clouds = []
for _ in range(int(h)):
    cloud = input()
    clouds.append(cloud)

# Read strings sequentially and save results as matrix
matrix = []
for cloud in clouds:
    numbers = []
    # Number is -1 as default
    num = -1
    for c in cloud:
        # Set 0 when 'c' is there
        if c == "c":
            num = 0
        # Start counting when c is gone
        elif num >= 0:
            num += 1
        numbers.append(num)
    matrix.append(numbers)

# Print cloud matrix as string
for nums in matrix:
    result = ""
    for num in nums:
        result += str(num) + " "
    print(result)
