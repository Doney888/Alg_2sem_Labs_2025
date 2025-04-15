def main():
    with open ("input.txt", "r") as f:
        n = int(f.readline())
        costs = [int(i) for i in f.readlines()]

    if n == 0:
        print(0)
        print(0, 0)
        return

    INF = 10 ** 9
    max_coupons = n
    dp = [[INF] * (max_coupons + 2) for _ in range(n + 1)]
    dp[0][0] = 0

    prev = [[None] * (max_coupons + 2) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = costs[i - 1]
        for c_prev in range(max_coupons + 1):
            if dp[i - 1][c_prev] == INF:
                continue

            # Не использовать купон
            new_cost = dp[i - 1][c_prev] + cost
            new_c = c_prev + (1 if cost > 100 else 0)
            if new_c > max_coupons:
                new_c = max_coupons
            if new_cost < dp[i][new_c]:
                dp[i][new_c] = new_cost
                prev[i][new_c] = (c_prev, False)

            # Использовать купон
            if c_prev >= 1:
                new_cost = dp[i - 1][c_prev]
                new_c = c_prev - 1
                if new_cost < dp[i][new_c]:
                    dp[i][new_c] = new_cost
                    prev[i][new_c] = (c_prev, True)

    min_total = INF
    best_c = 0
    for c in range(max_coupons + 1):
        if dp[n][c] < min_total:
            min_total = dp[n][c]
            best_c = c
        elif dp[n][c] == min_total and c > best_c:
            best_c = c

    K1 = best_c
    current_day = n
    current_c = best_c
    used_days = []

    while current_day > 0:
        if prev[current_day][current_c] is None:
            break
        c_prev, used = prev[current_day][current_c]
        if used:
            used_days.append(current_day)
        current_day -= 1
        current_c = c_prev

    K2 = len(used_days)
    used_days.sort()

    with open('output.txt', 'w') as f:
        f.write(f"{min_total}\n")
        f.write(f"{K1} {K2}\n")
        for day in used_days:
            f.write(f"{day}\n")


if __name__ == "__main__":
    main()