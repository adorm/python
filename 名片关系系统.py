# coding = utf-8

#1. 打印功能提示
print("="*50)
print(" 1. 添加一个新的名片")
print(" 2. 删除一个名片")
print(" 3. 修改一个名片")
print(" 4. 查询一个名片")
print(" 5. 显示所有的名片")
print(" 6. 退出系统")
print("="*50)

# 预定义一个存储空间用来存储名片

card_infors = []

while True:

    # 实现人与计算机的交互  ，通过输入命令来进行下一步的操作
    num = int(input("请输入您要实现的功能："))

    if num == 1:

        new_name = input("请输入您的名字")
        new_QQ = input("请输入您的QQ号:")

        # 定义一个新的字典来存储新的名片

        new_infors = {}
        new_infors["name"] = new_name
        new_infors["QQ"] = new_QQ

       # 将一个字典添加到列表中来

        card_infors.append(new_infors)

    elif num == 2:
        pass

    elif num == 3:
        pass

    elif num == 4:

        find_name = input("请输入您要查找的内容：")

        find_flag = 0  # 默认为没有找到    即遍历了所有数组后没有要查找的值

        for temp in card_infors:

            if find_name == temp["name"]:
                print("%s\t%s\t"%(temp["name"],temp["QQ"]))

                find_flag = 1

                break             # break 和conture  break是中止循环，直接结束循环，执行下一条语句

            if find_flag == 0:
                print("")

    else:
        print("输入有误，请重新输入")