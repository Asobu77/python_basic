# 例外処理

l = [1, 2, 3]
i = 5

# try内でエラーが生じた場合exceptに入る
try:
    l[i]
except IndexError as ex:
    print("Don't worry {}".format(ex))
except NameError as ex:
    print(ex)
# 極力エラーは分ける必要がある
except Exception as ex:
    print("other:{}".format(ex))
# exceptに引っかからなかった場合に使用する
else:
    print("done")
# finallyはexceptが生じた場合、必ず起きる
finally:
    print('clean up')
