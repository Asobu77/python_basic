# if文
# インデント依存

x = -10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

# ifのネスト
a = 5
b = 10

if a < 10:
    print('a < 10')
    if b < 20:
        print('b < 20')