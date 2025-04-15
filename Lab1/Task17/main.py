def main():
    with open("input.txt", "r") as f:
        n = int(f.readline())

    if n == 1:
        with open("output.txt", "w") as f:
            f.write("8")
        return

    dp = [[0] * 10 for _ in range(n)]
    dp[0] = [1] * 10
    MOD = 10 ** 9
    for i in range(1, n):
        dp[i][0] = (dp[i - 1][6] + dp[i - 1][4]) % MOD
        dp[i][1] = (dp[i - 1][6] + dp[i - 1][8] * (i != 1)) % MOD
        dp[i][2] = (dp[i - 1][7] + dp[i - 1][9]) % MOD
        dp[i][3] = (dp[i - 1][4] + dp[i - 1][8] * (i != 1)) % MOD
        dp[i][4] = (dp[i - 1][3] + dp[i - 1][9] + dp[i - 1][0] * (i != 1)) % MOD
        dp[i][5] = 0
        dp[i][6] = (dp[i - 1][1] + dp[i - 1][7] + dp[i - 1][0] * (i != 1)) % MOD
        dp[i][7] = (dp[i - 1][2] + dp[i - 1][6]) % MOD
        dp[i][8] = (dp[i - 1][1] + dp[i - 1][3]) % MOD
        dp[i][9] = (dp[i - 1][2] + dp[i - 1][4]) % MOD

    with open ("output.txt", "w") as f:
        f.write(str(sum(dp[n - 1])))

if __name__ == '__main__':
    main()