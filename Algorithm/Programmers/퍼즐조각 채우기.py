def solution(game_board, table):
    answer = 0
    puzzles = []
    dy = [0, 0, 1, -1]
    dx = [1, -1 ,0, 0]

    def is_inner(y, x, board):
        return 0 <= y < len(board) and 0 <= x < len(board[0])

    # 원점으로 이동
    def move_to_origin(puzzle):
        min_y = min(elem[0] for elem in puzzle)
        min_x = min(elem[1] for elem in puzzle)
        for elem in puzzle:
            elem[0] -= min_y
            elem[1] -= min_x

    def dfs(y, x, find, board, puzzle):
        puzzle.append([y, x])

        # blank 탐색 시
        if find == 0:
            board[y][x] = 1
        # puzzle 탐색 시
        else:
            board[y][x] = 0

        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if is_inner(new_y, new_x, board) and board[new_y][new_x] == find:
                dfs(new_y, new_x, find, board, puzzle)

    def remove_if_exist(blank):
        blank_copy = blank.copy()

        if blank_copy in puzzles:
            puzzles.remove(blank_copy)
            return True

        rotate90 = [[x, -y] for y, x in blank_copy]
        move_to_origin(rotate90)
        rotate90.sort()
        if rotate90 in puzzles:
            puzzles.remove(rotate90)
            return True

        rotate180 = [[-y, -x] for y, x in blank_copy]
        move_to_origin(rotate180)
        rotate180.sort()
        if rotate180 in puzzles:
            puzzles.remove(rotate180)
            return True

        rotate270 = [[-x, y] for y, x in blank_copy]
        move_to_origin(rotate270)
        rotate270.sort()
        if rotate270 in puzzles:
            puzzles.remove(rotate270)
            return True

        return False

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == 1:
                puzzle = []
                dfs(i, j, 1, table, puzzle)
                move_to_origin(puzzle)
                puzzle.sort()
                puzzles.append(puzzle)

    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 0:
                blank = []
                dfs(i, j, 0, game_board, blank)
                move_to_origin(blank)
                blank.sort()
                if remove_if_exist(blank):
                    answer += len(blank)

    return answer
