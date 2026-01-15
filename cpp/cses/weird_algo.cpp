#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define all(x) (x).begin(), (x).end()

static inline void fast_io() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
}

static void weird_algo(ll n){
  while (n){
    cout << n << " ";
    if (n == 1) return;
    if (n % 2 == 0) n /= 2;
    else n = (n * 3) + 1;
  }
  
}

static void solve_one() {
  ll n; cin >> n;
  weird_algo(n);
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

