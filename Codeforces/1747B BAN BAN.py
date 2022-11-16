testCase = int(input())

for i in range(testCase):
    n = int(input())

    m = max(n//2, (n+1)//2)
    print(m)

    first = 1 - 3 
    second = n*3 + 3
    for it in range(m):
        first += 3
        second -= 3
        print(first, second)
