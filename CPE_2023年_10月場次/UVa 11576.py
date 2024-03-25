times = int(input())

for _ in range(times):
    col,row = map(int,input().split())
    tmp = ""
    for x in range(row):
        arr = input()
        if x == 0:
           tmp = arr

        for i in range(col,0,-1):
            if tmp[-i:] == arr[:i]:
                tmp += arr[i:]
                break
            if i == 1:
                tmp += arr
    
    print(len(list(tmp)))