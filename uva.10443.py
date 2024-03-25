#題目中文翻譯
# List發明了一種新的文明。在一個二維的格子空間中，一開始每個格子被下面三種生命模式其中之一佔據：
# 石頭（Rocks），剪刀（Scissors），布（Paper）。每一天中每個格子與鄰近（上下左右）格子之間彼此交戰。每次交戰中，石頭贏剪刀、剪刀贏布、布贏石頭。
# 在一天結束時，勝方擴展其領土到敗方的格子上，敗方則從格子中消失。
# 你的任務是算出在n天後，各格子的生命模式為何。
# 輸入的第一列有一個正整數，代表以下有多少組測試資料。
# 每組測試資料的第一列，有3個不大於100的整數 r,c,n。
# r是格子的列數，c是格子的行數，n則是要求的第幾天。接下來的r列每列有c個字元，代表格子空間。每個字元為R,S,P其中之一，分別代表石頭、剪刀、布。

num = int(input())#輸入測資數量
for i in range(num):
    row,col,days = map(int,input().split(" "))#將列、行、天數用成迭代物件
    arr = []
    for x in range(row):
        arr.append(list(input()))#輸入原二維數列
    for day in range(days):
        result = [list(range(col)) for _ in range(row)]#存放比較結果 必須弄成二維陣列
        for x in range(row):
            for j in range(col):
                if(arr[x][j] == 'R'):#判定猜拳機制
                    player = "R"
                    winner = "P"
                elif(arr[x][j] == 'S'):
                    player = 'S'
                    winner = 'R'
                else:
                    player = 'P'
                    winner = 'S'
                    
                if((x - 1) >= 0 and arr[(x - 1)][j] == winner):#判定當前元素上方是否有比它大的元素
                    result[x][j] = winner
                elif((x + 1) < row and arr[(x + 1)][j] == winner):#判定當前元素下方是否有比它大的元素
                    result[x][j] = winner
                elif((j + 1) < col and arr[x][(j + 1)] == winner):#判定當前元素左方是否有比它大的元素
                    result[x][j] = winner
                elif((j - 1) >= 0 and arr[x][(j - 1)] == winner):#判定當前元素右方是否有比它大的元素
                    result[x][j] = winner
                else:#若四個判定條件都沒達成 返回當前元素
                    result[x][j] = player
                
        arr = result#將判定結果回傳至arr做更新
    for x in range(row):
        for j in range(col):
            print(arr[x][j] ,end = "")#列印結果
        print("")
        
    if(i != num - 1):
        print("")