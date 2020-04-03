# 辞書内包表記
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'wear']

d = {}
for x, y in zip(w, f):
    d[x] = y
print(d)

d_ = {x : y for x, y in zip(w, f)}
print(d_)
