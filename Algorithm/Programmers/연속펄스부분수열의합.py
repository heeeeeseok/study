def dp(arr):
    cache = [None] * len(arr)
    # 1.
    cache[0] = arr[0]

    # 2.
    for i in range(1, len(arr)):
        cache[i] = max(0, cache[i-1]) + arr[i]

    return max(cache)


def solution(sequence):
    parse_sequence1 = []
    parse_sequence2 = []

    operand = -1
    for num in sequence:
        parse_sequence1.append(num * operand)
        operand *= -1

    operand = 1
    for num in sequence:
        parse_sequence2.append(num * operand)
        operand *= -1

    return max(dp(parse_sequence1), dp(parse_sequence2))
