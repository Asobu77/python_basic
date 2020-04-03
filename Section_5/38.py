# null1の判定
is_empty = None

print(is_empty)

# 下記の条件は非推奨
if is_empty == None:
    print('None!')

# 書くなら下記の方法
if is_empty is None:
    print('None!')

# isはオブジェクト同士の判定
print(1 is True)
