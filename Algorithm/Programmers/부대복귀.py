from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    nodes = [[] for _ in range(n)]
    distance = [-1 for _ in range(n)]
    distance[destination - 1] = 0
    visited = [False] * n
    q = deque()

    for road in roads:
        nodes[road[0] - 1].append(road[1] - 1)
        nodes[road[1] - 1].append(road[0] - 1)

    q.append([destination - 1, 0])
    while q:
        cur_node, cur_length = q.popleft()
        if visited[cur_node]:
            continue

        visited[cur_node] = True
        distance[cur_node] = cur_length
        for node in nodes[cur_node]:
            q.append([node, cur_length + 1])

    for source in sources:
        answer.append(distance[source - 1])

    return answer
