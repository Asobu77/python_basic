# リスト内包表記
t = (1, 2, 3, 4, 5)

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)

print(r)

# 上記の意味合いと同じ
r = [i for i in t if i % 2 == 0]
print(r)

# リスト内包表記のループは可読性を下げるため使いすぎ注意
