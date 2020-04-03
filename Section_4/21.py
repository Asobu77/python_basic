    # parentice
t = (1, 2, 3, 4, 2, 3)
print(type(t))

# t[0] = 100

# help(tuple)

# index()関数,第一引数で指定した値のindexを番をを返す
print(t.index(1))
print(t.index(2, 3))

# count()関数第引数で指定した値の数をカウントする
print(t.count(2))

# touple同士の結合は可能
n_touple = (1, 2, 3) + (4, 5, 6,)
print(n_touple)