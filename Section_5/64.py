# 名前空間とスコープ
animal = 'cat'

def f():
    global animal
    animal = 'dog'

    # globals(), locals()をそれぞれ指定することで各空間の変数一覧が表示される
    print('local:', globals())
    print('local:', locals())

f()

