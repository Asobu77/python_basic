# デコレータ
def print_more(func):
    def wapper(*args, **kwards):
        print('func:'  , func.__name__)
        print('args:'  , args)
        print('kwards:', kwards)
        print('reslut:', func(*args, **kwards))

        return True
    return wapper

def print_info(func):
    def wrapper(*args, **kwards):
        print('start')
        result = func(*args, **kwards)
        print('end')
        return result
    return wrapper


# デコレーターを使う場合は@デコレーター名の下に関数を定義する
@print_info
@print_more
def add_num(a, b):
    print(a + b)
    return True

add_num(3, 5)


