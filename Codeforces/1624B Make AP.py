testCase = int(input())

for i in range(testCase):
    arr = list(map(int, input().split()))

    a = 2*arr[1] - arr[2]
    b = (arr[0]+arr[2])/2
    c = 2*arr[1]-arr[0]

    if arr[1] - arr[0] == arr[2] - arr[1]: print("YES")
    elif a > 0 and a % arr[0] == 0: print("YES")
    elif b % arr[1] == 0: print("YES")
    elif c > 0 and c % arr[2] == 0: print("YES")
    else: print("NO")
