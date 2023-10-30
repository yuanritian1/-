strInit = str(1.111111111)
# 字符串拼接
str1 = "hello"
str2 = "world！！！！%s"
nums = 100
# %s为占位符，表示字符串要拼接的内容
print(str1 + str2 % nums)
# 拼接多个字符串
str3 = "let%s,%s join in str3"
print(str3 % (1, 2))
# %d占位符号的使用
name = "zhangsan"
age = 18.99
print("my name is %s,age is %d" % (name, age))
