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
  if (n == 1) {
    cout << "1\n";
    return;
  }
  if (n < 4) {
    cout << "NO SOLUTION\n";
    return;
  }

  for(int i = 2; i <= n; i+=2) cout << i << " ";
  for(int i = 1; i <= n; i+=2) cout << i << " ";

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

