keyboard = {1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            7: (2, 0), 8: (2, 1), 9: (2, 2),
            0: (3, 1)}

def cal_weight(src, dest):
    weight = 0
    src_pos = keyboard[src]
    dest_pos = keyboard[dest]

    diff_y = abs(src_pos[0] - dest_pos[0])
    diff_x = abs(src_pos[1] - dest_pos[1])

    if diff_x == 0 and diff_y == 0:
        return 1
    elif diff_x == 0:
        return 2 * diff_y
    elif diff_y == 0:
        return 2 * diff_x
    else:
        while diff_y != 0 and diff_x != 0:
            weight += 3
            diff_x -= 1
            diff_y -= 1
        if diff_x == 0:
            weight += (2 * diff_y)
        elif diff_y == 0:
            weight += (2 * diff_x)
        return weight

def solution(numbers):
    cache = [[[float('inf') for _ in range(10)] for _ in range(10)] for _ in range(len(numbers) + 1)]
    cache[0][4][6] = 0

    for i in range(len(numbers)):
        number = int(numbers[i])

        for left in range(10):
            for right in range(10):
                pre_value = cache[i][left][right]

                if left == right or pre_value == float("inf"):
                    continue

                if cache[i + 1][number][right] > cache[i][left][right] + cal_weight(left, number):
                    cache[i + 1][number][right] = cache[i][left][right] + cal_weight(left, number)
                if cache[i + 1][left][number] > cache[i][left][right] + cal_weight(right, number):
                    cache[i + 1][left][number] = cache[i][left][right] + cal_weight(right, number)

    min_list = []
    for i in range(10):
        min_list.append(min(cache[len(numbers)][i]))
    return min(min_list)
