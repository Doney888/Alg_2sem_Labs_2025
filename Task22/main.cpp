#include <bits/stdc++.h>

using namespace std;

struct Cell {
    int white, black;

    Cell() = default;

    Cell(int a, int b): white(a), black(b) {};

};

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<Cell>> arr(n, vector<Cell>(m));
    arr[0][0].black = 1;
    arr[0][0].white = 1;

    for (int i = 1; i < m; i++) {
        arr[0][i].black = arr[0][i - 1].black + arr[0][i - 1].white;
        arr[0][i].white = arr[0][i].white;
    }

    for (int i = 1; i < n; i++) {
        arr[i][0].black = arr[i - 1][0].black + arr[i - 1][0].white;
        arr[i][0].black = arr[i][0].white;
    }

    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            arr[i][j].black
        }
    }
}