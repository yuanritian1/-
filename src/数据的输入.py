# name = input("请输入你的名字:")
# print("你好，", name)

# 输入数字类型
# num = input("请输入数字:")
# print("你输入的数字是:", type(num))
user_name = input("请输入你的名字:")
role_list = [{"user_name": "zhangsan", "role": "admin"},
             {"user_name": "lisi", "role": "user"}]
for role in role_list:
    if role["user_name"] == user_name:
        print("你输入的用户名是:", user_name)
        print("你输入的角色是:", role["role"])
else:
    print("你输入的用户名不存在")
