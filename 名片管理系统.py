# coding = utf-8

# 1 打印功能显示

print("="*50)
print('名字管理系统 ')

print('1：添加一个名字')     # 名片管理系统所需要实现的功能  其中的数字只是起显示作用，在程序中没有实际的作用
print("2：删除一个名字")
print("3：修改一个名字")
print("4：查询一个名字")
print("="*50)

# 2 获取所要实现的功能
names = []   # 定义一个空间  对添加的名字的存储

num = int(input("请输入功能序号："))  # 通过读取键盘输入的信息，与用户实现交互


# 3 根据用户所需要完成的功能进行选择 实现操作
while True:

    if num == 1:
         new_name = input("请输入名字：")   # 如果用户要求添加一个名字，输入1 ，然后执行if的这条语句，提示用户输入名字
         names.append(new_name)              # 通过append 函数实现新名字添加到预先定义空间中
         print(names)
    elif num == 2:
        pass

    elif num == 3:
        pass

    elif num == 4:
        find_name = input("请输入要查找的名字：")
        if find_name in names:
             print("找到了你要找的信息")
        else:
             print("没有找到你要找的信息")

    elif num == 5:
        break
    else:
        print("您输入的命令有误，请重新输入")


#  该程序存在的问题是当执行4 中执行错误时会一值提示输入要查找的名字，没有退出