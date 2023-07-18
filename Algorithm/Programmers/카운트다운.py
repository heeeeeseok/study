def solution(target):
    dp = [[] for _ in range(100000 + 1)]

    for i in range(1, 21):
        dp[i] = [1, 1]
        dp[i * 2] = [1, 0]
        dp[i * 3] = [1, 0]

    dp[50] = [1, 1]

    for i in range(21, target + 1):
        if dp[i]:
            continue

        min_dart = float('inf')
        max_sb = float('-inf')
        for j in range(1, 21):
            # 싱글
            cur_dart, cur_sb = [dp[i - j][0] + 1, dp[i - j][1] + 1]
            if cur_dart < min_dart or (cur_dart == min_dart and cur_sb > max_sb):
                min_dart = cur_dart
                max_sb = cur_sb

            # 더블
            if i - 2*j > 0:
                cur_dart, cur_sb = [dp[i - 2*j][0] + 1, dp[i - 2*j][1] + 0]
                if cur_dart < min_dart or (cur_dart == min_dart and cur_sb > max_sb):
                    min_dart = cur_dart
                    max_sb = cur_sb

            # 트리플
            if i - 3*j > 0:
                cur_dart, cur_sb = [dp[i - 3*j][0] + 1, dp[i - 3*j][1] + 0]
                if cur_dart < min_dart or (cur_dart == min_dart and cur_sb > max_sb):
                    min_dart = cur_dart
                    max_sb = cur_sb

        # 불
        if i > 50:
            cur_dart, cur_sb = [dp[i - 50][0] + 1, dp[i - 50][1] + 1]
            if cur_dart < min_dart or (cur_dart == min_dart and cur_sb > max_sb):
                min_dart = cur_dart
                max_sb = cur_sb

        dp[i] = [min_dart, max_sb]

    return dp[target]
