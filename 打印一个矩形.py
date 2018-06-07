# coding = utf-8

i = 1     # 用来控制行数
while i<=5:

    j=1    # 用来控制每一行的列数
    while j<=5:
        print("*",end="")   # end=""用来实现python 不换行，python总是默认换行的

        j+=1

    print("")   #用来实现换行

    i = i+1