# デフォルト引数
def test_func(x, l=[]):
    l.append(x)
    return l

r = test_func(100)
print(r)

# リストは参照渡しとなるため注意が必要
r = test_func(100)
print(r)


def test_func_2(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func_2(100)
print(r)

# 参照渡しを回避するには引数のデフォルトに[]を入れないようにする
r = test_func_2(100)
print(r)