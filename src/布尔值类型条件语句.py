# print("欢迎来到黑马儿童游乐场，儿童免费，成人收费")
# age = input("请输入你的年龄:")
# age = int(age)
# if age >= 18:
#     print("你已成年,需要补票10元")
#     print("祝你游玩愉快")
# else:
#     print("你还未成年，可以免费游玩")
# print("猜猜我心里想的数字是什么？")
# guessNumber = 50
# for i in range(3):
#     guess = input("请输入你猜测的数字:")
#     guess = int(guess)
#     if i == 2:
#         print(f"很遗憾，你没有猜中我心里想的数字,我想的数字是：{guessNumber}")
#         break

#     if guess == guessNumber:
#         print("恭喜你，猜对了")
#         break
#     else:
#         print("很遗憾，猜错了")
# 定义一个1-10的数字随机产生,通过三次判断来猜出数字的

import random
num = random.randint(1, 10)
rangeNums = 3
for i in range(rangeNums):
    guess = input("请输入你猜测的数字:")
    guess = int(guess)
    if (rangeNums-1 == i):
        print(f"很遗憾，你没有猜中我心里想的数字，游戏结束。我想的数字是：{num}")
        break
    if guess == num:
        print("恭喜你，猜对了")
        break
    elif (guess > num):
        print("你猜测的数字太大了")
    else:
        print("你猜测的数字太小了")
