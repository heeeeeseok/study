def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    dp = [[float('inf') for _ in range(52)] for _ in range(len(onboard))]

    temperature += 10
    t1 += 10
    t2 += 10

    if t1 <= temperature <= t2:
        return 0

    dp[0][temperature] = 0

    for i in range(1, len(onboard)):
        start = 0
        end = 0
        if onboard[i] == 1:
            start = t1
            end = t2
        else:
            start = min(temperature, t1)
            end = max(temperature, t2)

        for j in range(start, end + 1):
            # 실외 온도 보다 높을 때
            if j > temperature:
                dp[i][j] = min(dp[i - 1][j - 1] + a, dp[i - 1][j] + b, dp[i - 1][j + 1])
            # 실외 온도 보다 낮을 때
            elif j < temperature:
                dp[i][j] = min(dp[i - 1][j + 1] + a, dp[i - 1][j] + b, dp[i - 1][j - 1])
            # 실외 온도와 같을 때
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1], dp[i - 1][j - 1])

    return min(dp[-1])
