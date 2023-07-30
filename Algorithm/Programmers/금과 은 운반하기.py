def solution(a, b, g, s, w, t):
    start = 0
    end = (a + b) * 2 * max(t)

    def is_possible(time):
        total = 0
        gold = 0
        silver = 0
        for i in range(len(g)):
            max_count = 0
            max_count += time // (t[i] * 2)
            if time % (t[i] * 2) >= t[i]:
                max_count += 1

            max_weight = min(max_count * w[i], g[i] + s[i])
            total += max_weight
            gold += min(max_weight, g[i])
            silver += min(max_weight, s[i])

        if total >= a + b and gold >= a and silver >= b:
            return True

        return False

    while start + 1 < end:
        mid = (start + end) // 2
        if is_possible(mid):
            end = mid
        else:
            start = mid

    return end
