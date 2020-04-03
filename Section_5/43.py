# for else
# while文と同様、breakなしでループが終わる場合elseに入る
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('increde weight')