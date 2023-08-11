def next_range(s, e, move, max_bound):
    next_s = 0 if (s == 0 and move > 0) else s + move
    next_e = max_bound - 1 if (e == max_bound - 1 and move < 0) else e + move

    if (next_s < 0 and next_e >= max_bound) or next_s >= max_bound or next_e < 0:
        return -1, -1
    elif next_s < 0 and next_e < max_bound:
        return 0, next_e
    elif next_s >= 0 and next_e >= max_bound:
        return next_s, max_bound - 1
    else:
        return next_s, next_e

def solution(n, m, x, y, queries):
    sx = ex = x
    sy = ey = y

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for move_type, move_length in queries[::-1]:
        if move_type == 0 or move_type == 1:
            next_s, next_e = next_range(sy, ey, move_length * dy[move_type], m)
            if next_s == -1:
                return 0
            sy, ey = next_s, next_e
        else:
            next_s, next_e = next_range(sx, ex, move_length * dx[move_type], n)
            if next_s == -1:
                return 0
            sx, ex = next_s, next_e

    return (ex - sx + 1) * (ey - sy + 1)
