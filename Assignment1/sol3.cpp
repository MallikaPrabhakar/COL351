#include <bits/stdc++.h>

using namespace std;

vector<unordered_set<int>> adj;

set<pair<int, int>> people;

void deletePerson(int u) {  // O(degree(u) * log(n))
    for (auto &v : adj[u]) {
        people.erase({adj[v].size(), v});
        adj[v].erase(u);
        people.insert({adj[v].size(), v});
    }
    people.erase({adj[u].size(), u});
}

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    adj.assign(n, unordered_set<int>());
    for (int i = 0, u, v; i < m; ++i) {
        cin >> u >> v;
        adj[u].insert(v);
        adj[v].insert(u);
    }
    
    for (int i = 0; i < n; ++i) // O(n * log(n))
        people.insert({adj[i].size(), i});

    bool done = false;
    while (!done) { // O(sum(T(deletePerson)))
        done = true;
        auto i = *people.begin();
        if (i.first < k)
            done = 0, deletePerson(i.second);
        i = *people.rbegin();
        if (int(people.size() - i.first) - 1 < k)
            done = 0, deletePerson(i.second);
    }

    for (auto &u : people)
        cout << u.second << ' ';
    cout << '\n';
}
