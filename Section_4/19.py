# リストのコピー
i = [1, 2, 3, 4, 5]
j = i
j[0] = 100

# listは参照渡し
print(j)
print(i)
# id()は有効期限内でユニークな値を持つ
print(id(i))
print(id(j))

x = [1, 2, 3, 4, 5]

# list型をコピーする場合はcopy()関数　or indexに:を指定する
# y = x.copy()
y = x[:]
y[0] = 100

print(x)
print(y)


x = 20
y = x
y = 5

# 数字は値渡し
print(x)
print(y)

print(id(x))
print(id(y))


