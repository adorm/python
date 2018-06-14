# coding = utf-8

# 遍历列表的方式
nums = [11,22,33,44,55,66]

for temp in nums:
    print(temp)


# for else 命令

num =[12,13,14]
for A in num:
    print(A)
    break   #  这里的break 是什么意思 ，有什么作用？ break 指结束本次循环  执行下一条语句
else:
    print("=========")

# 名片管理器   for --else 命令   实现查找的功能

card = [{"名字":"小明","age":"18"},{"名字":"小李","age":"18"}]  #  元组的书写  内容的填充

find_name = input("请输入您要查找的内容：")
for S in card:
    print(S)
    if S['名字'] == find_name:   #  这里遇到了bug  s中的内容要与card 的内容一致   有一致的
        print("找到了")
        break
    else:
        print("查无此人")
# a.append 的注意事项  需要认真理解该程序

a = [11,22,33,44]
b = [66,77]

#  a.append(b)   打印a的结果[11, 22, 33, 44, [66, 77]]

a = a.append(b)  # 打印none   这是为什么呢？ a.apppend 并没有一个结果






