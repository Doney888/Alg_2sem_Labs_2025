def main():
    with open("input.txt", "r") as f:
        n, k = map(int, f.readline().split())
        s = f.readline().strip()

    ans = n
    dp = [[0, 0] for i in range (n)]
    for i in range(n):
        for j in range(i - 1, -1, -1):
            tmp = (s[i] != s[j]) + (dp[j + 1][i % 2] * (i - j > 1))
            if tmp <= k: ans += 1;
            dp[j][(i + 1)%2] = tmp

    with open("output.txt", "w") as f:
        f.write(str(ans))
main()