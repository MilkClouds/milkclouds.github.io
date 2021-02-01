---
layout: post
title: 'Educational Codeforces Round #103 (Div. 2)'
author: MilkClouds
comments: true
date: 2021-02-01 01:26
tags: [problem-solving]

---

## Educational Codeforces Round #103 (Div. 2)  

[에듀 라운드 103 Div2](https://codeforces.com/contest/1476)  


### A. K-divisible Sum 
k가 작다면 적당히 n보다 크도록 만들어 준 후에, `k/n`의 올림값을 구하는 문제이다.

```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a = b; a < c; a++)
#define pb push_back
 
using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
 
ll t, n, k;
int main(){
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    cin >> t;
    while(t--){
        cin >> n >> k;
        k *= n/k + (n%k!=0);
        cout << k/n + (k%n!=0) << "\n";
    }
}
```


### B. Inflation 
i번째 숫자를 처리중일 때(1-indexed), S[i-1]를 최대한 조금 늘리고 a[i]는 늘리지 않아야 한다.  

그 S[i-1]을 늘리는 건 a[1], a[2], ... a[i-1]중 어느 숫자를 늘려도 상관 없기 때문에 다 a[1]이 늘어나는 것으로 처리해도 된다. 늘어날 양은 오직 S[i-1]라는 숫자와 a[i]에만 의존한다. 따라서 조건을 만족하기 위해 S[i-1]가 늘어나야 하는 숫자 중 최댓값을 출력하면 된다.    

솔직히 나도 설명 써놓고 뭔 소린지 좀 이해가 안 가는데 감대로 풀면 이렇다. 그리디의 일종으로 생각하면 된다.     
  

```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a = b; a < c; a++)
#define pb push_back
 
using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
const int MAX = 102;
 
ll t, n, k, p[MAX], S[MAX], add[MAX], ans;
int main(){
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    cin >> t;
    while(t--){
        cin >> n >> k;
        ans = 0;
        fill(S, S + n, 0);
        rep(i, 0, n) cin >> p[i];
        rep(i, 0, n) S[i + 1] = S[i] + p[i];
        rep(i, 0, n - 1) ans = max(ans, p[n - i - 1] * 100 / k + (p[n - i - 1] * 100 % k != 0) - S[n - i - 1]);
        cout << ans << "\n";
    }
}
```

### C. Longest Simple Cycle   
다루는 사이클은 심플한데 푸는 과정은 짜증났다. 단순 반복문 사용 문제인데 딱 한 줄 구현을 살짝 잘못해서 맞왜틀 30분 반복하다 겨우 맞췄다. 이런 단순 구현 문제는 한 줄 실수하면 참 짜증난다..    

```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a = b; a < c; a++)
#define rep2(a,b,c) for(ll a = c - 1; a >= b; a--)
#define pb push_back
 
using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
const int MAX = 1e5 + 3;
 
ll t, n, c[MAX], b[MAX], a[MAX], last, ans, tmp;
int main(){
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    cin >> t;
    while(t--){
        cin >> n;
        ans = 0;
        rep(i, 0, n) cin >> c[i];
        rep(i, 0, n) cin >> a[i];
        rep(i, 0, n) {cin >> b[i]; if(b[i] < a[i]) swap(b[i], a[i]);}
        last = n; tmp = c[n - 1];
        rep2(i, 0, n - 1) {
            ans = max(ans, b[i + 1] - a[i + 1] + 1 + tmp);
            tmp += c[i] - (b[i + 1] - a[i + 1] - 1);
            tmp = max(tmp, c[i]);
            if(a[i + 1] == b[i + 1]) {last = i; tmp = c[i];}
        }
        cout << ans << "\n";
    }
}
```

### D. Journey  
BFS 문제다. DFS로 풀려다 안되는 것 같아서 BFS로 구현했다. 중간에 +2백만은 그냥 abs 함수 씌우면 되는데 뭔가 신선한 게 필요해서 그냥 음수에 +2백만했다.  

```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a = b; a < c; a++)
#define rep2(a,b,c) for(ll a = c - 1; a >= b; a--)
#define pb push_back
 
using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
const int MAX = 3e5 + 3;
 
string s;
int n, ans[MAX];
 
int BFS(int b){
    int cnt = 0;
    vector<bool> vis(n + 1, 0);
    vector<int> save;
    queue<int> Q;
    Q.push(b); vis[b] = 1; cnt++; save.pb(b);
    while(!Q.empty()){
        int u = Q.front(); Q.pop();
        if(( (s[u] == 'R') ^ ((u - b+2000000) % 2) ) && u<n && !vis[u+1]){
            vis[u + 1] = 1;
            Q.push(u + 1); cnt++; save.pb(u+1);
        }
        if(u > 0 && ( (s[u - 1] == 'L') ^ ((u - b+2000000) % 2) ) && !vis[u-1]){
            vis[u - 1] = 1;
            Q.push(u - 1); cnt++; save.pb(u-1);
        }
    }
    for(auto i:save) if(vis[i] && (i-b+2000000)%2==0) ans[i] = cnt;
    return cnt;
}
 
 
void solve(){
    cin >> n >> s;
    fill(ans,ans+n+1, 0);
    rep(i, 0, n + 1) if(!ans[i]) BFS(i);
    rep(i, 0, n + 1) cout << ans[i] << " " ;
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

### E. Pattern Matching   
맵에 패턴 저장해놓고, k가 4까지밖에 안되는 점을 이용해보자. 그럼 string들은 2^4가지 조합으로 글자 4군데 어딘가에 블라인드(`_`)를 씌울 수도 있고 안 씌울 수도 있다. 이러한 2^4 조합 중 패턴이랑 똑같은 조합을 맵을 통해 찾는다. 그리고 mt가 무조건 이 조건을 만족하는 조합보다 먼저 나오므로, 선후관계를 설정하고, 위상정렬한다. 사이클이 있으면 버린다.  

이거 문제 발문이 좀 심각하게 이상해서(특히 mt 나오는 부분) 시간 내에 못 풀었다. 문제를 읽고 이해를 잘 못해서... 에디토리얼 보니 외국인들도 발문 이상하다고 하는 걸 보니 나만 느낀 게 아닌가보다. 문제는 좋은데 발문이 참...     

```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a = b; a < c; a++)
#define pb push_back
 
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pi;
const int MAX = 1e5 + 3;
 
ll N, M, K, mt, deg[MAX];
string s, tmp, S[MAX];
map<string, ll> m;
vector<ll> adj[MAX], ans;
 
bool op(string pat, string str){
    rep(i, 0, K){
        if(str[i] == pat[i] || pat[i] == '_') continue;
        return 0;
    }
    return 1;
}
 
ll Topological_Sort(){
    queue<ll> Q;
    ll cnt = 0;
    rep(i, 1, N + 1){
        if(deg[i] == 0) Q.push(i);
    }
    while(!Q.empty()){
        ll u = Q.front(); Q.pop(); cnt++;
        ans.pb(u);
        for(auto v: adj[u]){
            deg[v]--;
            if(deg[v] == 0){
                Q.push(v);
            }
        }
    }
    if(cnt < N) return 0;
    return 1;
}
 
int main(){
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    cin >> N >> M >> K;
    rep(i, 1, N + 1) {
        cin >> s;
        S[i] = s;
        m[s] = i;
    }
    rep(i, 0, M){
        cin >> s >> mt;
        if(!op(S[mt], s)) {cout << "NO\n"; return 0;}
        rep(k, 0, 1 << K){
            ll j = 0, i = k;
            tmp = s;
            while(i){
                if(i%2){
                    tmp[j] = '_';
                }
                j++;i/=2;
            }
            if(m[tmp] == 0 || m[tmp] == mt) continue;
            adj[mt].pb(m[tmp]);
            deg[m[tmp]]++;
        }
    }
    if(Topological_Sort() == 0) {cout << "NO\n"; return 0;}
    cout << "YES\n";
    for(auto i:ans)cout << i << " " ;
}
```

### F. Lanterns  
해설 보고 겨우 풀었다. 세그트리는 어차피 뭐 한두번 구현해본 것도 아니고 구현 귀찮아서 해설 소스 가져왔다.  

이 정도면 정올 2,3번은 되지 않을까?   

```cpp  
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a = b; a < c; a++)
#define rep2(a,b,c) for(ll a = c - 1; a >=b; a--)
#define all(x) (x).begin(), (x).end()
#define pb push_back

using namespace std;
typedef long long ll;
typedef pair<ll, ll> pi;

const ll MAX = 3e5 + 3, INF = 1e9;

ll N, p[MAX], dp[MAX], l[MAX], r[MAX], ans[MAX];

struct segTree
{
    ll n;
    bool mx;
    vector<ll> t;

    void fix(ll v)
    {
        t[v] = (mx ? max(t[v * 2 + 1], t[v * 2 + 2]) : min(t[v * 2 + 1], t[v * 2 + 2]));
    }

    void build(ll v, ll l, ll r)
    {
        if (l == r - 1)
            t[v] = (mx ? -INF : INF);
        else
        {
            ll m = (l + r) / 2;
            build(v * 2 + 1, l, m);
            build(v * 2 + 2, m, r);
            fix(v);
        }
    }

    void upd(ll v, ll l, ll r, ll pos, ll val)
    {
        if (l == r - 1)
            t[v] = (mx ? max(t[v], val) : min(t[v], val));
        else
        {
            ll m = (l + r) / 2;
            if (pos < m)
                upd(v * 2 + 1, l, m, pos, val);
            else
                upd(v * 2 + 2, m, r, pos, val);
            fix(v);
        }
    }

    ll get(ll v, ll l, ll r, ll L, ll R)
    {
        if (L >= R)
            return (mx ? -INF : INF);
        if (l == L && r == R)
            return t[v];
        ll m = (l + r) / 2;
        ll lf = get(v * 2 + 1, l, m, L, min(R, m));
        ll rg = get(v * 2 + 2, m, r, max(m, L), R);
        return (mx ? max(lf, rg) : min(lf, rg));
    }

    void upd(ll pos, ll val)
    {
        upd(0, 0, n, pos, val);
    }

    ll get(ll L, ll R)
    {
        return get(0, 0, n, L, R);
    }

    void build()
    {
        return build(0, 0, n);
    }

    segTree() {};
    segTree(ll n, bool mx) : n(n), mx(mx)
    {
        t.resize(4 * n);
    }
};


void solve() {
    cin >> N;
    rep(i, 0, N) cin >> p[i + 1];
    fill(dp, dp + N + 1, -INF);
    fill(ans, ans + N + 1, -2);
    segTree minTree(N + 1, false), maxTree(N + 1, true);
    minTree.build(); maxTree.build();
    minTree.upd(0, 0);
    dp[0] = 0;
    rep(i, 1, N + 1) {
        l[i] = max((ll)1, i - p[i]);
        r[i] = min(N, i + p[i]);
        maxTree.upd(i, r[i]);
    }
    rep(i, 1, N + 1) {
        ll m = minTree.get(l[i] - 1, N + 1);
        if (m != INF) {
            ll nval = max(i - 1, maxTree.get(m + 1, i - 1 + 1));
            if (nval > dp[i]) {
                dp[i] = nval;
                ans[i] = m;
            }
        }
        if (dp[i - 1] >= i && max(dp[i - 1], r[i]) > dp[i]) {
            dp[i] = max(dp[i - 1], r[i]);
            ans[i] = -1;
        }
        if (dp[i - 1] > dp[i]) dp[i] = dp[i - 1];
        minTree.upd(dp[i], i);
    }
    if (dp[N] != N) { cout << "NO\n"; return; }
    cout << "YES\n";
    ll chk = N + 1;
    string s;
    rep2(i, 1, N + 1) {
        if (chk < i) { s += "R"; continue; }
        if (ans[i] <0) s += "R";
        if (ans[i]>=0) {
            s += "L";
            chk = ans[i];
        }
    }
    reverse(all(s));
    cout << s << "\n";
}

int main() {
    cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(false);
    ll TC;
    cin >> TC;
    while (TC--) solve();
}
``