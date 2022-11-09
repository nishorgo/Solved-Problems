testCase = int(input())

for i in range(testCase):
    min_sum = 0
    flag = False
    arr = input()

    for ind, ch in enumerate(arr[:-1]):
        if arr[ind] != arr[ind+1]:
            min_sum += 1 if arr[ind] == '0' else 0

        if min_sum >= 2:
            print("2")
            flag = True
            break

    if not flag:
        if arr[-1] == '0':
            min_sum += 1
        print(min_sum)