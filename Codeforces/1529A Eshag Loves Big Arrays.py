testCase = int(input())

for i in range(testCase):
    arr_len = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    count = 0
    
    while True:
        if (arr[0] + arr[-1]) / 2 < arr[-1]:
            arr.pop(-1)
            count += 1
        else: break

    print(count)
