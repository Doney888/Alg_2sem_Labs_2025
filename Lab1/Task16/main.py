def main():
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        dist = []
        for _ in range(n):
            dist.append(list(map(int, f.readline().split())))

    if n == 0:
        with open('output.txt', 'w') as f:
            f.write('0\n')
        return

    INF = 10 ** 9
    full_mask = (1 << n) - 1

    dp = [[INF] * n for _ in range(1 << n)]
    prev = [[-1] * n for _ in range(1 << n)]

    for u in range(n):
        dp[1 << u][u] = 0

    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)) or dp[mask][u] == INF:
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue
                new_mask = mask | (1 << v)
                new_cost = dp[mask][u] + dist[u][v]
                if new_cost < dp[new_mask][v]:
                    dp[new_mask][v] = new_cost
                    prev[new_mask][v] = u

    min_length = INF
    best_u = -1
    for u in range(n):
        if dp[full_mask][u] < min_length:
            min_length = dp[full_mask][u]
            best_u = u

    path = []
    current_mask = full_mask
    current_city = best_u
    while True:
        path.append(current_city + 1)
        p = prev[current_mask][current_city]
        if p == -1:
            break
        current_mask ^= (1 << current_city)
        current_city = p

    path.reverse()

    with open('output.txt', 'w') as f:
        f.write(f"{min_length}\n")
        f.write(' '.join(map(str, path)) + '\n')


if __name__ == "__main__":
    main()