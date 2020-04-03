# 集合内包表記
s = set()

for i in range(10):
    s.add(i)

print(s)

# 辞書型のValue値を指定しなければ集合になる
s_ = {i for i in range(10)}
print(s_)
