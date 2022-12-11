def is_right_angle_triangle (a, b, c):
    triangle_some = sorted([a, b, c])
    print(triangle_some)
    result = {
    'result': False,
    'description': 'no such triangle exists'
}


    if triangle_some[0] + triangle_some[1] <= triangle_some[2]:
        True
    elif triangle_some[0]**2 + triangle_some[1]**2 == triangle_some[2]**2:
        result['result'] = True
        result['description'] = 'the triangle is right-angled'
    else:
        result['description'] = 'the triangle is not right-angled'
    return result

print(is_right_angle_triangle(11, 11, 21))
