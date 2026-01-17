#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define all(x) (x).begin(), (x).end()

static inline void fast_io() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
}

static void solve_one() {
  int n; cin >> n;

  ll l = 0;
  ll cost = 0;
  // 3 2 5 1 7
  // 0 1 0 4 0
  for (int i =0; i < n; i++){
    ll x; cin >> x;
    if (x > l) l = x;
    else cost += l-x;
  }
  cout << cost << '\n';
  
}

int main() {
    fast_io();

    solve_one();
    

    // int T; cin >> T;
    // while (T--) solve_one();
    

    // int n;
    // while (cin >> n && n != 0){
    //  solve_one(n);
    // }

    return 0;
}

