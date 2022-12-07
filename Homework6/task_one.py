import math


def meaning(*args):
    k = 0
    dist_sum = 0
    print(args)
    for p in args[1:]:
        distance = math.hypot(p[0] - args[k][0], p[1] - args[k][1])
        dist_sum = dist_sum + distance
        k = k + 1
    return dist_sum


print(f'Длина маршрута между точками {meaning((1, 1), (1, 2))}')
