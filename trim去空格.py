def trim(str):
    if len(str) == 0:  # 用长度判定，也可以用空表本身就是一个false的特征来判定
        return str
    while str[0] is ' ':
        str = str[1:]
        if len(str) == 0:  # 用长度判定，也可以用空表本身就是一个false的特征来判定
            return str
    while str[-1] is ' ':
        str = str[:-1]
        if len(str) == 0:  # 用长度判定，也可以用空表本身就是一个false的特征来判定
            return str
    return str


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')