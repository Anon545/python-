# x = float(input())
# if x <= 0 and x // 0 == 0:
#     x = -x
# print(x)

x = float(input())
if x >= 0:
    print(x)
else:
# if not (x >= 0): - так тоже можно вместо else
    print(-x)