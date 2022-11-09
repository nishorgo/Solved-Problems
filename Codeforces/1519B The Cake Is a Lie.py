testCase = int(input())

for i in range(testCase):
    n, m, k = map(int, input().split())
    k -= n-1
    k -= (m-1)*n
    
    print("YES") if k==0 else print("NO")
