# range関数
for i in range(2, 10):
    print(i)

for i in range(2, 10, 2):
    print(i)

# for文に_をindexに入れることで明示的にindexし使用しないことを示す
for _ in range(2, 10, 2):
    print('uhoo!')