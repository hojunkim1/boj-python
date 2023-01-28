a, b = map(int, input().split())
if b >= 45:
    print(f"{a} {b - 45}")
else:
    a -= 1
    if a < 0:
        a += 24
    print(f"{a} {b + 15}")
