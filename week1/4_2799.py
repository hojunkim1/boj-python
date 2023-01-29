# Input
n, m = map(int, input().split())
input_arr = [list(input().strip()) for _ in range(5 * n + 1)]

# Extract useful datas
new_arr = []
for i in range(n):
    for j in range(m):
        new_arr.append([
            input_arr[i * 5 + 1][j * 5 + 1],
            input_arr[i * 5 + 2][j * 5 + 1],
            input_arr[i * 5 + 3][j * 5 + 1],
            input_arr[i * 5 + 4][j * 5 + 1]
        ])

# Set type of blinds
a, b, c, d, e = 0, 0, 0, 0, 0
for blinds in new_arr:
    blind_type = 0
    for i in blinds:
        if i == "*":
            blind_type += 1
    if blind_type == 0:
        a += 1
    elif blind_type == 1:
        b += 1
    elif blind_type == 2:
        c += 1
    elif blind_type == 3:
        d += 1
    else:
        e += 1

# Print
print(f"{a} {b} {c} {d} {e}")
