# 引数、返り値の明示的な型指定
# 仮に型が一致していなくてもプログラムは実行される
def add_num(a: int, b: int) -> int:
    return a + b

r = add_num(10, 20)
print(r)

