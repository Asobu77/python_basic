word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:3])
print(word[2:4])
print(word[3:])

# print(word[100])
# ↑ないインデックスの指定はエラー

word = 'j' + word[1:]
print(len(word))
# len()文字列の長さを出力する関数


