# 複数の引数
def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)

# 引数名を指定して値を与えると、引数の順番に関係はなくなる
menu(entree='beef', dessert='ice', drink='beer')


# デフォルト引数
def dinner(entree='beef', drink='wine', dessert='ice'):
    print(entree)
    print(drink)
    print(dessert)

dinner()

