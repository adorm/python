# coding = utf-8

# 打印三角形
i = 1  # 控制行数

while i<=5:  # while 循环确定循环的行数

    j = 1     # 控制每一行打印的* 的个数
    while j<=i:
        print("*",end="")  # 在python中print 会实现自动换行 ，end取消自动换行
        j+=1  # 每一行打印的* 个数加一

    print("") #  实现自动换行  因为python 在pritn后会有自动换行的操错，所以打印一个空 字符   实现自动换行

    i+=1    # 行号加一

#  九九乘法表的打印

i = 1

while i<=9:

    j = 1               # 每次循环时j都是从一开始
    while j<=i:

        print("%d*%d=%d\t"%(j,i,i*j),end="")#  end 表示打印字符以空格结尾    \t 表示制表符  每一个%d所代表的东西
        j+=1

    print("")  # 换行操作

    i+=1            # 九九乘法表的一行打印完成