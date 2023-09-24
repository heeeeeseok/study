import copy
from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

if __name__ == '__main__':
    bfs_count = 0
    size_count_list = []
    N = int(input())

    m = [[0 for _ in range(N)] for _ in range(N)]
    visited = copy.deepcopy(m)

    for y in range(N):
        line = list(input())
        for i in range(len(line)):
            m[y][i] = int(line[i])

    def bfs(y, x):
        count = 0
        visited[y][x] = 1
        q = deque()
        q.append((y, x))
        count += 1

        while q:
            cur_y, cur_x = q.popleft()
            visited[cur_y][cur_x] = 1

            for i in range(4):
                new_y = cur_y + dy[i]
                new_x = cur_x + dx[i]
                if 0 <= new_x < N and 0 <= new_y < N:
                    if m[new_y][new_x] == 1 and visited[new_y][new_x] == 0:
                        q.append((new_y, new_x))
                        visited[new_y][new_x] = 1
                        count += 1

        return count

    for y in range(N):
        for x in range(N):
            if m[y][x] == 1 and visited[y][x] == 0:
                size_count = bfs(y, x)
                size_count_list.append(size_count)
                bfs_count += 1

    print(bfs_count)
    size_count_list.sort()
    for count in size_count_list:
        print(count)
