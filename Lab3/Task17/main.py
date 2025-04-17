import fileinput
import sys

def main():
    with open("input.txt", "r") as input:
        n, m = map(int, input.readline().split())

        INF = float('inf')
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for _ in range(m):
            x, y = map(int, input.readline().split())
            x -= 1
            y -= 1
            dist[x][y] = 0
            if dist[y][x] > 1:
                dist[y][x] = 1

    for k in range(n):
        dist_k = dist[k]
        for i in range(n):
            if dist[i][k] < INF:
                dist_i = dist[i]
                dist_ik = dist[i][k]
                for j in range(n):
                    if dist_k[j] < INF and dist_i[j] > dist_ik + dist_k[j]:
                        dist_i[j] = dist_ik + dist_k[j]

    max_k = 0
    for row in dist:
        current_max = max(row)
        if current_max > max_k:
            max_k = current_max
    with open("output.txt", "w") as output: output.write(str(max_k))


if __name__ == '__main__':
    main()