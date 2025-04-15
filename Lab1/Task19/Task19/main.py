def ans(split, i, j):
    if i == j:
        return "A"
    k = split[i][j]
    return f"({ans(split, i, k)}{ans(split, k + 1, j)})"

def main():
    with open("input.txt", "r") as f:
        n = int(f.readline())
        a = []
        b = []
        for i in range(n):
            tmp_a, tmp_b = map(int, f.readline().split())
            a.append(tmp_a)
            b.append(tmp_b)

    dp = [[10 ** 9] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + a[i] * b[k] * b[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    print(split)
    with open("output.txt", "w") as f:
        f.write(ans(split, 0, n - 1))


if __name__ == '__main__':
    main()