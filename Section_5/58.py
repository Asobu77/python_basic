# ラムダ
l = ['Mon', 'tue', 'Web', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

change_words(l, sample_func)

# 関数を作成せずラムダ(無名関数)を入力する
change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())
