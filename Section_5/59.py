# ジェネレータ
l = ['Good morning', 'Good afternoon' ,'Goog night']

for i in l:
    print(i)

print('-------------')

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

# for g in greeting():
#     print(g)

# forループとは違い、実行のタイミングを制御したいときし使用する
g = greeting()
print(next(g))
print(next(g))