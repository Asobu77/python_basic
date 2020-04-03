def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

d = {
    'entree' : 'beef',
    'drink'  : 'ice coffee',
    'dessert': 'tapioka'
}

menu(**d)

def dinner(welcome, *args, **kwargs):
    print(welcome)
    print(args)
    print(kwargs)

d = {
    'entree' : 'beef',
    'drink'  : 'ice coffee',
    'dessert': 'tapioka'
}

# 第一引数はwelcome、第二,三引数は*args、第四引数は**kwargsに代入される
dinner('berry', 'vegi', 'meat', **d)

