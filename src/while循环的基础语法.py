# 计算1-100的累加值
# sum = 0
# i = 1
# while i <= 100:
#     sum = sum + i
#     i += 1

# print(sum)

# import random

# num = random.randint(1, 100)
# count = 0

# flag = True
# while flag:
#     guess = int(input("请输入你猜测的数字:"))
#     count += 1
#     if guess == num:
#         print("恭喜你，猜对了")
#         flag = False
#     elif guess > num:
#         print("猜大了")
#     else:
#         print("猜小了")

# print("你总共猜了", count, "次")

# 99乘法表

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("%d*%d=%d" % (j, i, i*j), end="\t")
#         j += 1
#     print("")
#     i += 1
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%d" % (j, i, i*j), end="\t")
    print("")
