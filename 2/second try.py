import random
a = random.randint(1,100)
guess = 0 

while guess<5:
    User = int(input("请输入姓名"))
    if User > a:
        print("猜大了") 
        guess=guess+1

    if User < a:
        print("猜小了")
        guess=guess+1

    if User ==a:
        print("猜对了")
        break

# import random

# # 1. 生成随机数
# secret = random.randint(1, 100)
# guess_count = 0 

# # 2. 游戏开始
# print("游戏开始！你有5次机会。")

# while guess_count < 5:
#     # 3. 计数器先 +1，并展示是第几次
#     guess_count = guess_count + 1
    
#     # 4. 获取输入 (注意提示语)
#     user_input = int(input(f"第 {guess_count} 次尝试，请输入数字: "))

#     # 5. 判断逻辑 (互斥逻辑用 elif)
#     if user_input == secret:
#         print("恭喜你！猜对了！")
#         break  # <--- 关键！赢了直接结束循环
#     elif user_input > secret:
#         print("猜大了")
#     else:
#         print("猜小了")

# # 6. (选做) 如果循环正常结束(没触发break)说明输了
# if user_input != secret:
#     print(f"很遗憾，机会用光了。正确答案是 {secret}")
    