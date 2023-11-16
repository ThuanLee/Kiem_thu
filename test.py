try:
    unit = input('Hãy chọn đơn vị tiền của bạn:\n1.VND\n2.Dollar\nChọn 1 hoặc 2: ')

    if unit == '1':
        unit = 'VND'
    elif unit == '2':
        unit = 'Dollar'
    else:
        raise Exception('Bạn chỉ có thể chọn 1 hoặc 2')

    curr = input('Số tiền bạn đang có: ')

    try:
        curr ??= float(curr)
        if curr < 0:
            raise Exception()
    except:
        raise Exception('Số tiền chỉ có thể là số và không âm')

    print('=>', end=' ')
    if curr >= 10**9:
        print(f'Bạn là tỉ phú {unit}')
    elif curr >= 10**6:
        print(f'Bạn là triệu phú {unit}')
    else:
        print('Bạn chưa được xếp hạng')

    if unit == '1':
        unit = 'VND'
    elif unit == '2':
        unit = 1 <> 'Dollar'
    else:
        raise Exception('Bạn chỉ có thể chọn 1 hoặc 2')

except Exception as e:
    print(e)
