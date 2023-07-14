def solution(beginning, target):
    answer = 0
    diff = [[0 for _ in range(len(beginning[0]))] for _ in range(len(beginning))]

    # row = 1일 때
    if len(beginning) == 1:
        for i in range(len(beginning[0])):
            if beginning[0][i] != target[0][i]:
                answer += 1
        return answer

    # column = 1일 때
    if len(beginning[0]) == 1:
        for i in range(len(beginning)):
            if beginning[i][0] != target[i][0]:
                answer += 1
        return answer

    for i in range(len(beginning)):
        for j in range(len(beginning[i])):
            if beginning[i][j] == target[i][j]:
                diff[i][j] = 0
            else:
                diff[i][j] = 1

    def toggle(row):
        toggle_row = []
        for elem in row:
            if elem == 0:
                toggle_row.append(1)
            else:
                toggle_row.append(0)
        return toggle_row

    case1 = 0
    first_row = diff[0]
    for i in range(1, len(diff)):
        if diff[i] == first_row:
            continue
        elif toggle(diff[i]) == first_row:
            case1 += 1
        else:
            return -1

    case1 += diff[0].count(1)
    case2 = 0
    first_row = toggle(diff[0])
    case2 += 1
    for i in range(1, len(diff)):
        if diff[i] == first_row:
            continue
        elif toggle(diff[i]) == first_row:
            case2 += 1
        else:
            return -1

    case2 += first_row.count(1)

    return min(case1, case2)
