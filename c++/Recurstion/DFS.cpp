#include<iostream>
#include<vector>

using namespace std;

const int N = 1e5;

vector<vector<int>> adj(N);
vector<bool> visited(N);

void dfs(int n) {
    if (visited[n]) return;
    visited[n] = true;
    for (auto &x : adj[n]) {
        dfs(x);
    }
}

int main() {

    return 0;
}
