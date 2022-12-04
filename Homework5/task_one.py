while True:
    result = {}
    error = False
    user_input = input('Введите номер телефона в международном формате: ')

    if len(user_input) != 13:
        result['success'] = False
        result['description'] = 'The number must contain 13 characters.'
        error = True
        print(result['description'])

    if user_input[0] != '+':
        result['success'] = False
        result['description'] = 'The first character entered is not a + sign.'
        error = True
        print(result['description'])

    for char in user_input[1:]:
        if not char.isdigit():
            result['success'] = False
            result['description'] = 'invalid input format.'
            error = True
            print(result['description'])

    if user_input[1:4] != '375':
        result['success'] = False
        result['description'] = 'Invalid: international format code: 375'
        error = True
        print(result['description'])

    operator_number = user_input[4:6]
    digit_after_operator_number = user_input[6:7]
    mobile_operator = ''
    if operator_number == '25':
        mobile_operator = 'Life'
    elif operator_number == '33':
        mobile_operator = 'MTS'
    elif operator_number == '44':
        mobile_operator = 'A1'
    elif operator_number == '29':
        if (digit_after_operator_number in ['1', '3', '6', '9']):
            mobile_operator = 'A1'
        elif (digit_after_operator_number in ['2', '5', '7', '8']):
            mobile_operator = 'MTS'

        else:
            result['success'] = False
            result['description'] = 'Operator not defined'
            error = True
            print(result['description'])
    else:
        result['success'] = False
        result['description'] = 'Unknow operator mobile'
        error = True
        print(result['description'])

    if error:
        print(result)
    else:
        result['success'] = True
        result['phone'] = user_input
        result['mobile_operator'] = mobile_operator
        print(result)

    exit_chois = input('Хотите завершить сеанс (Y/N): ')

    if exit_chois == 'Y':
        break
