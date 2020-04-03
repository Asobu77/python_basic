y = [1, 2, 3]
x = 1

# 要素の確認で使用
if x in y:
    print('in')

# not 判定を逆にする
if 100 not in y:
    print('not in')


# notの使い時
# 下記is_okがfalseの場合でもifのケースに入れたい場合
is_ok = False
if not is_ok:
    print('hello')

