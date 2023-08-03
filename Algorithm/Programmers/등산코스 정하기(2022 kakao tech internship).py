import queue

def solution(n, paths, gates, summits):
    nodes = [[] for _ in range(n + 1)]
    cache = [float('inf') for _ in range(n + 1)]
    gates = set(gates)
    summits = set(summits)
    min_intensity = float('inf')
    min_summit = -1
    q = queue.Queue()

    for [i, j, w] in paths:
        nodes[i].append([j, w])
        nodes[j].append([i, w])

    for gate in gates:
        q.put(gate)
        cache[gate] = 0
        while not q.empty():
            cur_node = q.get()
            if cur_node in summits:
                if min_intensity > cache[cur_node] or (min_intensity == cache[cur_node] and min_summit > cur_node):
                    min_intensity = cache[cur_node]
                    min_summit = cur_node
                continue

            for next_node, weight in nodes[cur_node]:
                if cache[next_node] > max(weight, cache[cur_node]):
                    cache[next_node] = max(weight, cache[cur_node])
                    q.put(next_node)

    return [min_summit, min_intensity]
