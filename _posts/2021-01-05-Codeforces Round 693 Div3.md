---
layout: post
title: 'Codeforces Round #693 (Div. 3)'
author: milkclouds
comments: true
date: 2021-01-05 01:47
tags: [problem-solving]

---

## Codeforces Round #693 (Div.3)  

[라운드 693 Div3](https://codeforces.com/contest/1472)  


### A. Cards for Friends  


```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a = b; a < c; a++)
#define pb push_back
 
using namespace std;
typedef long long ll;
 
ll TC, w, h, n;
 
int main(){
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    cin >> TC;
    while(TC--){
        cin >> w >> h >> n;
        ll a = 1, b = 1;
        while(w % 2 == 0){w /= 2; a *= 2;}
        w = h;
        while(w % 2 == 0){w /= 2; b *= 2;}
        cout << (a*b >= n ? "YES" : "NO") << "\n";
    }
}
```


### B. Fair Division  
  

```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a = b; a < c; a++)
#define pb push_back
 
using namespace std;
typedef long long ll;
 
ll TC, n, a[101], x, y;
 
int main(){
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    cin >> TC;
    while(TC--){
        cin >> n;
        x = y = 0;
        rep(i, 0, n) {cin >> a[i]; (a[i] == 1 ? x : y)++;}
        if((x & 1) || (x == 0 && (y & 1))) {cout << "NO\n"; continue;}
        cout << "YES\n";
    }
}
```

### C. Long Jumps  
  

```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a = b; a < c; a++)
#define pb push_back
 
using namespace std;
typedef long long ll;
const int MAX = 2e5 + 1;
 
ll TC, n, a[MAX], dp[MAX], ans;
 
int main(){
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    cin >> TC;
    while(TC--){
        cin >> n;
        ans = 0;
        rep(i, 0, n) {cin >> a[i]; dp[i] = a[i];}
        rep(i, 0, n) {
            if(a[i] + i >= n) continue;
            dp[a[i] + i] = max(dp[a[i] + i], dp[i] + a[a[i] + i]);
        }
        rep(i, 0, n) ans = max(dp[i], ans);
        cout << ans << "\n";
    }
}
```

### D. Even-Odd Game  
  

```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a = b; a < c; a++)
#define pb push_back
 
using namespace std;
typedef long long ll;
const int MAX = 2e5 + 1;
 
ll TC, n, a[MAX], A, B;
 
int main(){
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    cin >> TC;
    while(TC--){
        cin >> n;
        rep(i, 0, n) cin >> a[i];
        sort(a, a + n, greater<ll>());
        A = B = 0;
        rep(i, 0, n){
            ((i & 1) ? B : A) += ((i % 2) ^ (a[i] & 1)) ? 0 : a[i];
        }
        if(A > B) cout << "Alice\n";
        else if (A < B) cout << "Bob\n";
        else cout << "Tie\n";
    }
}
```

### E. Correct Placement   
  

```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a = b; a < c; a++)
#define pb push_back
 
using namespace std;
typedef long long ll;
const int MAX = 2e5 + 1;
 
struct P {
    ll i, w, h;
    P(){P(0,0,0);}
    P(ll i, ll w, ll h):i(i),w(w),h(h){}
    bool operator <(P o) {
        if(w != o.w) return w < o.w;
        return h < o.h;
    }
} A[MAX];
 
ll TC, N, w[MAX], h[MAX], ans[MAX];
vector<pair<ll, ll> > v;
pair<ll ,ll> min_ele[MAX];
 
int main(){
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    cin >> TC;
    while(TC--){
        cin >> N;
        rep(i, 0, N) {
            cin >> w[i] >> h[i];
            if(w[i] < h[i]) swap(w[i], h[i]);
            A[i] = P(i, w[i], h[i]);
        }
        sort(A, A + N);
        v.clear(); v.pb({A[0].w, A[0].i});
        rep(i, 1, N) if(A[i].w != A[i - 1].w) v.pb({A[i].w, A[i].i});
        min_ele[0] = {h[v[0].second], v[0].second};
        rep(i, 1, v.size()){
            if(min_ele[i - 1].first > h[v[i].second]) min_ele[i] = {h[v[i].second], v[i].second};
            else min_ele[i] = min_ele[i - 1];
        }
        fill(ans, ans + N , -1);
        rep(i, 0, N){
            auto pos = lower_bound(v.begin(), v.end(), pair<ll, ll>({w[i], 0}));
            if(pos == v.begin()) continue;
            pos--;
            if(min_ele[pos - v.begin()].first >= h[i]) continue;
            ans[i] = min_ele[pos - v.begin()].second + 1;
        }
        rep(i, 0, N) cout << ans[i] << " ";
        cout << "\n";
    }
}
```

### F. New Year's Puzzle  
난 구현 문제가 싫다. 소스가 더러워져서.. 사소한 곳에서 실수해서 한참 고민했다.  

```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a = b; a < c; a++)
#define pb push_back
 
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pii;
const int MAX = 2e5 + 3;
 
vector<pii> v;
ll TC, N, M, r[MAX], c[MAX], last, chk, flag, s, fin;
 
int main(){
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    cin >> TC;
    while(TC--){ v.clear();
        cin >> N >> M; N++;
        rep(i, 0, M) {cin >> r[i] >> c[i]; v.pb({c[i], r[i]});}     
        v.pb({N, 1}); v.pb({N, 2});
        sort(v.begin(), v.end());
        fin = s = flag = chk = last = 0;
        rep(i, 0, M + 2){
            if(flag) {flag = 0; continue;}
            if(i < M + 1 && v[i + 1].first == v[i].first) {flag = 1; if(chk){fin = 1;break;} continue;}
            if(!chk) {chk = 1; last = v[i].first; s = v[i].second; continue;}
            if((v[i].first - last) % 2){
                if(s == v[i].second) chk = 0; 
                else{fin = 1; break;}
            }
            else {
                if(s != v[i].second) chk = 0;
                else {fin = 1; break;}
            }
            last = v[i].first; s = v[i].second;
        }
        if(fin) cout <<"NO\n";
        else cout << "YES\n";
    }
}
```



### G. Moving to the Capital   
벡터 구현이 좀 더럽다. 그냥 로컬변수로 둘 걸.   


```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a = b; a < c; a++)
#define pb push_back
 
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pii;
const int MAX = 2e5 + 1, INF = 1e9;

vector<int> adj[MAX], dp[2], d;
vector<bool> vis;

int dfs(int u, int flag){
    if(dp[flag][u] ^ INF) return dp[flag][u];
    int ret = d[u];
    for(auto v: adj[u]){
        if(!flag){
            if(d[v] <= d[u]) ret = min(ret, dfs(v, 1));
            else ret = min(ret, dfs(v, 0));
        } else if (d[v] > d[u]) ret = min(ret, dfs(v, 1));
    }
    return dp[flag][u] = ret;
}

void solve(){
    int n, m, u, v;
    cin >> n >> m;
    rep(i, 0, n) adj[i].clear();
    d.clear();vis.clear();dp[0].clear();dp[1].clear();
    d.resize(n, INF);
    vis.resize(n, 0);
    dp[0].resize(n, INF); dp[1].resize(n, INF);
    rep(i, 0, m){
        cin >> u >> v; u--; v--;
        adj[u].pb(v);
    }
    queue<int> Q;
    Q.push(0); d[0] = 0; vis[0] = 0;
    while(!Q.empty()){
        int u = Q.front(); Q.pop();
        for(auto v: adj[u]){
            if(vis[v]) continue;
            d[v] = min(d[v], d[u] + 1);
            vis[v] = 1;
            Q.push(v);
        }
    }
    rep(i, 0, n) cout << dfs(i, 0) << " " ;
    cout << "\n";
}

int main(){
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    int TC;
    cin >> TC;
    while(TC--){
        solve();
    }
}
```

## 완료  
