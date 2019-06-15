# 文字のメソッド
s = 'My name is Mike'
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

# string型のメソッド
print(s.find('Mike'))
# find()前から何番目に引数の文字があるの調べる
print(s.rfind('Mike'))
# rfind()後ろから何番目に引数の文字があるの調べる rはリバースの略??
print(s.count('Mike'))
# count()引数の文字が何回出現しているか調査
print(s.capitalize())
# capitalize()先頭の文字を大文字に。。
print(s.title())
# title()各単語の先頭文字を大文字に変換
print(s.upper())
# upper()文字を全て大文字に変換
print(s.lower())
# lower()文字を全て小文字に変換
print(s.replace('Mike', 'Nancy'))
# replace()引数の文字を置換する
