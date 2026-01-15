#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define all(x) (x).begin(), (x).end()

static inline void fast_io() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
}
static void reptition(string s){
  int l = 0, maxSize = 0, n = (int)s.size();

  for(int r = 0; r < n; ++r){
    if (s[l] != s[r]){
      l = r;
    } else {
      maxSize = max(maxSize,r-l+1);
    }
  }
  cout << maxSize << "\n";
}

static void solve_one() {
  string s;
  cin >> s;
  reptition(s);
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

