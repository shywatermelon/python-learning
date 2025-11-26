fruits = ["apple","banana","orange"]
for  fruit in fruits:
    print(fruit)

age_str = input("请输入年龄")
age = int(age_str)
print(age)

user = {
    "name": "张三",
    "age": 24,
    "is_admin": False
}
print(user["name"])
user["age"] = 25
user["score"] = 100  # 如果 Key 不存在，会自动添加
print(user["score"])

