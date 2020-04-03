# 独自例外
class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            # raiseでエラーを投げる
            raise UppercaseError(word)

try:
    check()
# 自分で作成したエラーはexceptで指定することができる
except UppercaseError as ex:
    print('This is my Error class')