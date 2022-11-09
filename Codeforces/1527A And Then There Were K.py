testCase = int(input())

for i in range(testCase):
    n = int(input())
    
    for i in range(31, -1, -1):
        if n & (1 << i):
            print((1 << i)-1)
            break
