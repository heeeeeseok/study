def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = float('inf')
    map = [[0 for _ in range(102)] for _ in range(102)]
    visited = [[0 for _ in range(102)] for _ in range(102)]
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    def is_inner(matrix, y, x):
        for i in range(8):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if matrix[new_y][new_x] != 1:
                return False
        return True

    for rect in rectangle:
        for i in range(rect[1] * 2, (rect[3] * 2) + 1):
            for j in range(rect[0] * 2, (rect[2] * 2) + 1):
                map[i][j] = 1

    inner_list = []
    for i in range(1, 101):
        for j in range(1, 101):
            if map[i][j] == 1 and is_inner(map, i, j):
                inner_list.append((i, j))

    for (y, x) in inner_list:
        map[y][x] = 0

    cur_y = characterY * 2
    cur_x = characterX * 2
    stack = []
    stack.append((cur_y, cur_x, 0))

    while stack:
        (cur_y, cur_x, dist) = stack.pop()
        if cur_y == (itemY * 2) and cur_x == (itemX * 2):
            answer = min(answer, dist)
            continue

        visited[cur_y][cur_x] = 1
        for i in range(4):
            new_y = cur_y + dy[i]
            new_x = cur_x + dx[i]
            if map[new_y][new_x] == 1 and visited[new_y][new_x] == 0:
                stack.append((new_y, new_x, dist + 1))

    return answer // 2
