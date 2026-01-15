#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define all(x) (x).begin(), (x).end()

static inline void fast_io() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
}
static void missing_num(ll n){
  ll t;
  ll x = 0;
  for(ll i = 1; i <= n; i++) x ^= i;
  
  for(ll i = 0; i < n-1;i++){
    cin >> t;
    x ^= t;
  }
  cout << x << "\n";
}

static void solve_one() {
  ll n; cin >> n;
  missing_num(n);
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

