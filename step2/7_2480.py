a, b, c = map(int, input().split())

nums = {a, b, c}
duplicated = None
if len(nums) == 1:
    print(10000 + (1000 * a))
elif len(nums) == 2:
    if a in [b, c]:
        duplicated = a
    else:
        duplicated = b
    print(1000 + (duplicated * 100))
else:
    print(max(a, b, c) * 100)
