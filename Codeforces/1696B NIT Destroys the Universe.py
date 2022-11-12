testCase = int(input())

for i in range(testCase):
    arr_len = int(input())
    arr = list(map(int, input().split()))

    count = 0
    flag = 0
    for i in range(arr_len):
        if arr[i]: flag = 1
        elif flag: 
            count += 1
            flag = 0

        if count >= 2:
            print("2")
            break
    
    if count < 2:
        count += flag
        print(count)
