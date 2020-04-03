# while文
count = 0
while count < 5:
    print(count)
    count += 1

count = 0
while True:
    if count >= 3:
        # breakでループと止める
        break

    if count == 2:
        count += 1
        # continueで次のループへ
        continue

    print(count)
    count += 1
