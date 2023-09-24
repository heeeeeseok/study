from collections import deque


if __name__ == '__main__':
    answer = 0
    n = int(input())
    connected_count = int(input())

    visited = [0 for _ in range(n + 1)]
    linked_node = [[] for _ in range(n + 1)]
    q = deque()

    for _ in range(connected_count):
        a, b = map(int, input().split())
        linked_node[a].append(b)
        linked_node[b].append(a)

    def bfs():
        answer = 0
        q.append(1)
        visited[1] = 1

        while q:
            cur_node = q.popleft()
            for node in linked_node[cur_node]:
                if visited[node] == 0:
                    q.append(node)
                    visited[node] = 1
                    answer += 1

        return answer


    visited[1] = 1
    answer = bfs()
    print(answer)
