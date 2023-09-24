import copy
from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

if __name__=='__main__':
    T = int(input())
    answer_list = []

    for _ in range(T):
        answer = 0
        M, N, K = map(int, input().split())

        m = [[0 for _ in range(M)] for _ in range(N)]
        visited = copy.deepcopy(m)

        for _ in range(K):
            x, y = map(int, input().split())
            m[y][x] = 1

        def bfs(y, x):
            visited[y][x] = 1
            q = deque()
            q.append((y, x))

            while q:
                cur_y, cur_x = q.popleft()
                visited[cur_y][cur_x] = 1

                for i in range(4):
                    new_y = cur_y + dy[i]
                    new_x = cur_x + dx[i]
                    if 0 <= new_x < M and 0 <= new_y < N:
                        if m[new_y][new_x] == 1 and visited[new_y][new_x] == 0:
                            q.append((new_y, new_x))
                            visited[new_y][new_x] = 1

        for y in range(N):
            for x in range(M):
                if m[y][x] == 1 and visited[y][x] == 0:
                    bfs(y, x)
                    answer += 1

        answer_list.append(answer)

    for answer in answer_list:
        print(answer)
