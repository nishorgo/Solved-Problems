def isChunkSame(j, k):
    for l in range(r):
        for m in range(c):
            if grid[j+l][k+m] != pattern[l][m]:
                return False
    return True

def parseGrid():
    for j in range(R-r+1):
        for k in range(C-c+1):
            if grid[j][k] == pattern[0][0] and grid[j+r-1][k+c-1] == pattern[r-1][c-1] and grid[j][k+c-1] == pattern[0][c-1] and grid[j+r-1][k] == pattern[r-1][0]:
                if isChunkSame(j, k):
                    return  "YES"
    return "NO"
    

testCase = int(input())

for i in range(testCase):
    R, C = map(int, input().split())
    grid = []
    for j in range(R):
        row = input()
        grid.append(row)

    r, c = map(int, input().split())
    pattern = []
    for j in range(r):
        row = input()
        pattern.append(row)

    print(parseGrid())
