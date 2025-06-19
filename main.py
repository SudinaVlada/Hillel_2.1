_user_input = input("Введіть число:  ")
user_input = int(_user_input)
a = user_input // 1000
b = (user_input // 100) % 10
c = (user_input // 10) % 10
d = user_input% 10
print(a)
print(b)
print(c)
print(d)