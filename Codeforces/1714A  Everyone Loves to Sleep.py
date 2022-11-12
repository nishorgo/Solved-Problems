testCase = int(input())

for i in range(testCase):
    arr = list(map(int, input().split()))
    sleep = arr[1]*60 + arr[2]
    diff = 100000

    for j in range(arr[0]):
        alarm = list(map(int, input().split()))
        alarm = alarm[0]*60 + alarm[1]
        if alarm < sleep: alarm += 1440

        diff = min(diff, alarm - sleep)

    print("{0} {1}".format(diff//60, diff%60)) 
