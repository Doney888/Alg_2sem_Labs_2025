def solve(n, m):
    if m == 1: return 1 << n;
    MAX_MASK = 1 << n
    dp = [1 for i in range(MAX_MASK)]
    for _ in range(1, m):
        tmp = [0 for i in range(MAX_MASK)]
        for prev_mask in range(MAX_MASK):
            for mask in range(MAX_MASK):
                if (isCorrectMask(prev_mask, mask, n)): tmp[mask] += dp[prev_mask];
        dp = tmp
    return sum(dp)
def isCorrectMask(mask1, mask2, n):
    for i in range (n - 1):
        bit00 = (mask1 >> i) & 1
        bit01 = (mask1 >> (i + 1)) & 1
        bit10 = (mask2 >> i) & 1
        bit11 = (mask2 >> (i + 1)) & 1
        if bit00 == bit01 == bit10 == bit11: return False;
    return True

f = open("input.txt", "r")
n, m = map(int, f.readline().split())
f.close()

if n > m: n,m = m,n

f = open("output.txt", "w")
f.write(str(solve(n, m)))
f.close()