def solution(commands):
    answer = []
    table = [['EMPTY' for _ in range(50)] for _ in range(50)]
    parent = [[[] for _ in range(50)] for _ in range(50)]

    for i in range(50):
        for j in range(50):
            parent[i][j].append([i, j])

    def find(i, j):
        r = parent[i][j][0][0]
        c = parent[i][j][0][1]
        if r == i and c == j:
            return [i, j]
        else:
            return find(r, c)

    for command in commands:
        args = command.split(' ')
        if args[0] == 'UPDATE':
            if len(args) == 4:
                input_r = int(args[1]) - 1
                input_c = int(args[2]) - 1
                parent_r, parent_c = find(input_r, input_c)

                table[parent_r][parent_c] = args[3]
            elif len(args) == 3:
                for i in range(50):
                    for j in range(50):
                        parent_r, parent_c = find(i, j)
                        if table[parent_r][parent_c] != 'EMPTY' and table[parent_r][parent_c] == args[1]:
                            table[parent_r][parent_c] = args[2]

        elif args[0] == 'MERGE':
            # 두 좌표가 같을 때
            if args[1] == args[3] and args[2] == args[4]:
                continue

            parent_r1, parent_c1 = find(int(args[1]) - 1, int(args[2]) - 1)
            parent_r2, parent_c2 = find(int(args[3]) - 1, int(args[4]) - 1)

            # 이미 두 부모가 같을 때
            if parent_r1 == parent_r2 and parent_c1 == parent_c2:
                continue

            if table[parent_r1][parent_c1] == 'EMPTY':
                table[parent_r1][parent_c1] = table[parent_r2][parent_c2]

            if len(parent[parent_r2][parent_c2]) == 1:
                parent[parent_r1][parent_c1].append([parent_r2, parent_c2])
                parent[parent_r2][parent_c2] = [[parent_r1, parent_c1]]
                table[parent_r2][parent_c2] = 'EMPTY'
            else:
                for child in parent[parent_r2][parent_c2][1:]:
                    child_r, child_c = child[0], child[1]
                    parent[parent_r1][parent_c1].append(child)
                    table[child_r][child_c] = 'EMPTY'
                    parent[child_r][child_c].clear()
                    parent[child_r][child_c].append([parent_r1, parent_c1])

                table[parent_r2][parent_c2] = 'EMPTY'
                parent[parent_r2][parent_c2].clear()
                parent[parent_r2][parent_c2].append([parent_r1, parent_c1])
                parent[parent_r1][parent_c1].append([parent_r2, parent_c2])

        elif args[0] == 'UNMERGE':
            input_r = int(args[1]) - 1
            input_c = int(args[2]) - 1
            parent_r, parent_c = find(input_r, input_c)

            if len(parent[parent_r][parent_c]) == 1:
                continue

            for child in parent[parent_r][parent_c][1:]:
                child_r, child_c = child[0], child[1]
                parent[child_r][child_c] = [child]
                table[child_r][child_c] = "EMPTY"

            if (input_r, input_c) != (parent_r, parent_c):
                table[input_r][input_c] = table[parent_r][parent_c]
                table[parent_r][parent_c] = "EMPTY"

            parent[parent_r][parent_c].clear()
            parent[parent_r][parent_c] = [[parent_r, parent_c]]

        elif args[0] == 'PRINT':
            input_r = int(args[1]) - 1
            input_c = int(args[2]) - 1
            r, c = find(input_r, input_c)

            answer.append(table[r][c])

    return answer
