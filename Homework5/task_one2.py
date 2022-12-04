while True:
    result = {}
    errors = []
    user_input = input('Введите номер телефона в международном формате: ')

    if len(user_input) != 13:
        errors.append('The number must contain 13 characters.')

    if user_input[0] != '+':
        errors.append('The first character entered is not a + sign.')

    for char in user_input[1:]:
        if not char.isdigit():
            errors.append('Invalid input format.')

    if user_input[1:4] != '375':
        errors.append('Invalid: international format code for Belarus: 375')

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
            errors.append('Operator by code "29" not defined')
    else:
        errors.append('Operator not defined by code')

    if len(errors):
        result['success'] = False
        result['rrors'] = errors
        print(result)

    else:
        result['success'] = True
        result['phone'] = user_input
        result['mobile_operator'] = mobile_operator
        print(f'Номер:{user_input} принадлежит оператору {mobile_operator}.')

    exit_chois = input('Хотите завершить сеанс (Y/N): ')
    if exit_chois == 'Y':
        break
