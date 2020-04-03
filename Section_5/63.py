# ジェネレータ内包表記
def g():
    for i in range(10):
        yield i

g = g()

g = (i for i in range(10))
print(g)

