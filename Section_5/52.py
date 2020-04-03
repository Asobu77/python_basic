# 引数にタプルに入れる
def say_something(*args):
    for arg in args:
        print(arg)

# 引数に単語を指定すると*argsに含まれる
say_something('Mike', 'Bob', 'Cathy')

# 引数に参照渡しすることもできる
tpl = ('elly', 'poal')
say_something('Edy', *tpl)
