testCase = int(input())

for i in range(testCase):
    n = int(input())
    binary = input()
    count = 0

    for i in range(n-1):
        if binary[i] != binary[i+1]: count += 1

    if binary[0] == '0': ans = max(count-1, 0)
    else: ans = count

    print(ans)
