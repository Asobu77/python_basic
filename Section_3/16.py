s = ['a', 'b', 'c', 'd', 'e', 'f']
s[0] = 'X'
print(s)

n = [1, 2, 3, 4, 5, 6, 7, 8]
# append()関数は入力した文字 or 数字をリストの末尾に追加する
n.append(100)
print(n)

# insert関数は第一引数にインデックスを選択し、第二引数で差し込む値を記入する
n.insert(0, 50)
print(n)

# pop関数は引数なしで末尾、インデックスを引数で指定することでその値を削除
print(n.pop())
print(n)

n.pop(0)
print(n)

# delは変数を削除する　引数を指定することで一部削除も可能
del n[0]
print(n)

del n


n = [1, 2, 2, 3]
# remove()関数は引数で指定した値を削除する
n.remove(2)
n.remove(2)
print(n)

list_1 = ['a','b']
list_2 = [1, 2]

list_1 += list_2
print(list_1)

list_3 = ['a','b']
list_4 = [1, 2]

# extend()関数はリストの結合で使用する
list_3.extend(list_4)
print(list_3)