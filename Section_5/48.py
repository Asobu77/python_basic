# 関数定義
def say_something():
    print('hi')

say_something()

def return_function():
    return 'hi'

print(return_function())

# 引数指定、返り値
def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this('green')
print(result)

