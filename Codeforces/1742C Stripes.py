def check(str):
    for col in range(8):
        if str[col] != 'R':
            return False
    return True

testCase = int(input())

for i in range(testCase):
    blank = input()
    flag = False

    for j in range(8):
        row = input()
        
        if check(row): flag = True
            
    if flag: print("R")
    else: print("B")
