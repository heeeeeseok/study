def solution(alp, cop, problems):
    max_req_alp = -1
    max_req_cop = -1

    for problem in problems:
        if problem[0] > max_req_alp:
            max_req_alp = problem[0]
        if problem[1] > max_req_cop:
            max_req_cop = problem[1]
        if problem[2] == 0 and problem[3] == 0:
            problems.pop(problem)

    # 이미 조건을 충족한 경우
    if alp >= max_req_alp and cop >= max_req_cop:
        return 0

    if alp > max_req_alp:
        alp = max_req_alp
    if cop > max_req_cop:
        cop = max_req_cop

    dp = [[float('inf') for _ in range(max_req_cop + 1)] for _ in range(max_req_alp + 1)]
    dp[alp][cop] = 0

    for cur_alp in range(alp, max_req_alp + 1):
        for cur_cop in range(cop, max_req_cop + 1):
            if cur_alp < max_req_alp:
                dp[cur_alp][cur_cop] = min(dp[cur_alp][cur_cop], dp[cur_alp - 1][cur_cop] + 1)
            if cur_cop < max_req_cop:
                dp[cur_alp][cur_cop] = min(dp[cur_alp][cur_cop], dp[cur_alp][cur_cop - 1] + 1)

            for problem in problems:
                if cur_alp >= problem[0] and cur_cop >= problem[1]:
                    next_alp = min(max_req_alp, cur_alp + problem[2])
                    next_cop = min(max_req_cop, cur_cop + problem[3])
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[cur_alp][cur_cop] + problem[4])

    return dp[max_req_alp][max_req_cop]
