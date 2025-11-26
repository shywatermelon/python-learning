celsius = input("请输入温度")
fahrenheit = (int(celsius)* 9/5) + 32
print(fahrenheit)
# 关键在于 if-elif-else 的 “排他性” 和 “顺序性”。它只会执行它遇到的第一个为 True 的分支。
# 这就是为什么在写这类条件判断时，条件的顺序非常重要。通常，我们会把最严格、范围最窄的条件放在最前面，然后依次放宽，这样才能保证逻辑的正确性。
score = int(input("请输入成绩"))
if score>=90:
    print("优秀")
elif score>=80:
    print("良好")
elif score>=70:
    print("一般")
else:
    print("不及格")