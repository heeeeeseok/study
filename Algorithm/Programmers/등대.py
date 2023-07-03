def solution(n, lighthouse):
    # dp[node_index][is_selected] = select_count
    dp = [[0]*2 for _ in range(n)]
    visited = [0 for _ in range(n)]

    nodes = [[] for _ in range(n)]
    for node in lighthouse:
        nodes[node[0] - 1].append(node[1] - 1)
        nodes[node[1] - 1].append(node[0] - 1)

    def dfs(node):
        visited[node] = True
        sibling_list = []
        for sibling in nodes[node]:
            if not visited[sibling]:
                sibling_list.append(sibling)
                dfs(sibling)

        dp[node][1] = 1
        dp[node][0] = 0

        for sibling in sibling_list:
            dp[node][1] += min(dp[sibling])
            dp[node][0] += dp[sibling][1]
        return

    dfs(0)
    return min(dp[0])
