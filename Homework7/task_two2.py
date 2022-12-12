def is_right_angle_triangle(a_, b_, c_):
    a, b, c = sorted([a_, b_, c_])
    result = {'result': False, 'description': 'no such triangle exists'}

    if a + b <= c:
        True
    elif a**2 + b**2 == c**2:
        result['result'] = True
        result['description'] = 'the triangle is right-angled'
    else:
        result['description'] = 'the triangle is not right-angled'
    return result


print(is_right_angle_triangle(11, 11, 21))
