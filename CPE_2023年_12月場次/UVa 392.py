# 題目中文翻譯：
# 給你一個數學多項式的係數，從8次方到0次方。你的任務是把一些不需要的項次拿掉，然後以易讀的格式來輸出。
# 例如：給你 0, 0, 0, 1, 22, -333, 0, 1,  -1這9個係數，你應該要產生這樣的輸出： x^5 + 22x^4 - 333x^3 + x - 1
# 以下是詳細格式的規則：
# 項次必須按降冪出現。
# 指數部分出現在^符號之後。
# 常數項只要出現常數部分就好了，不需有x^0。
# 只有係數非0的項次才需出現。如果所有的係數都是0，那只要輸出常數項就可以了。
# 介於項次之間的+號和-號兩邊各有一空白字元。
# 假如第一項的係數是正的，那麼該係數不需要符號。如果第一項的係數是負的，那該係數必須有-這個符號。例如：-7x^2 + 30x + 66
# 若係數為負，則以減一個正數來表示（除了上面第6條所提到的第一項之外），而非以加一個負數來表示。例如：x^2 + -3x 這樣的表示法是錯誤的，應該是：x^2 - 3x才對。
# 1或-1，除了常數項之外都不應該出現。例如：-1x^3 + 1x^2 + 3x^1 - 1 這樣的表示法是錯誤的，應該是：-x^3 + x^2 + 3x - 1 才對。

#程式碼
while True:#連續資料輸入
    try:
        flag = 0
        end = 8
        list1 = list(map(int,input('').split(" ")))
        for i in list1:
            if i != 0:#判斷數列值是否大於0 沒有的話直接篩除
                if(flag != 1):#開始跑陣列
                    flag = 1
                    if i < 0:#如果i是負數則加負號
                        print("-",end = "")
                else:
                    if(i > 0):#如果i是正數則加加號 反之
                        print("+",end = "")
                    else:
                        print("-",end = "")
                if(abs(i) != 1 or end == 0):#判斷絕對值是否不等於1 並用end當作陣列長度來做迴圈
                    print(abs(i),end = "")
                if end > 1:#陣列位置大於1的就輸出次方
                    print(f'x^{end}',end = "")
                elif end == 1:
                    print("x",end = "")
            end -= 1
        if flag == 0:#跑完陣列後若最後常數項是0 就列印出來 不是就列印空格
            print(0)
        else:
            print("")
    except:
        break