# 辞書のコピー
d = {'x': 10, 'y': 20}

print(d.keys())
print(d.values())

x = {'x': 50, 'z':100}
d.update(x)
print(d)

# d['x'] == d.get('x')

d.get('x')
d.pop('x')

print(d)

# 辞書型の値か空にするにはclear()関数を使用する
# この場合は値が空の{}が返ってくるため、エラーは発生しない
# d.clear()
# print(d)

# この場合は変数自体削除しているため、エラーは発生
# del d
# error
# print(d)

print('x' in d )
print('y' in d )
