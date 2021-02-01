---
layout: post
title: 'USACO 2019 December Contest'
author: MilkClouds
comments: true
date: 2021-02-01 21:25
tags: [problem-solving]

---

## [USACO 2019 December Contest](https://www.acmicpc.net/category/471)    
고등학생일 당시 대회에 참가했었는데, 브론즈, 실버까지 풀고 골드부터는 좀 고민하다 시간 없어서 못 풀었었다. 이 포스트에는 골드 풀이까지 수록한다.    


### Bronze

#### 1. Cow Gymnastics
백준 레이팅은 Bronze 1로 잡혀있는데 브1치고 소스코드가 좀 복잡한데..? 풀이는 푼 지 오래되서 기억 안 난다.  

```cpp
# pragma GCC optimize ("O3")
# pragma GCC optimize ("Ofast")
# pragma GCC optimize ("unroll-loops")
#include <bits/stdc++.h>
#define rep(a,b,c) for(int a=b;a<c;a++)
#define rep2(a,b,c) for(ll a=b;a>c;a--)
#define pb push_back
#define x first
#define y second
#define all(x) x.begin(), x.end()
using namespace std;
using ll=long long;
using ti=tuple<ll,ll,ll>;
using pi=pair<ll,ll>;

ll K, N, A[11][21], rev[11][21], no[21][21], ans;

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin >> K >> N;
    rep(i, 0, K){
        rep(j, 0, N){
            cin >> A[i][j];
            rev[i][A[i][j] - 1] = j;
        }
        rep(a, 0, N){
            rep(b, a + 1, N){
                if(no[a][b])continue;
                if((rev[i][a] < rev[i][b]) ^ (rev[0][a] < rev[0][b])) no[a][b] = 1;
            }
        }
    }
    rep(a, 0, N){
        rep(b, a + 1, N){
            ans += !no[a][b];
        }
    }
    cout << ans << endl;
}
```

#### 2. Where Am I?

```cpp
# pragma GCC optimize ("O3")
# pragma GCC optimize ("Ofast")
# pragma GCC optimize ("unroll-loops")
#include <bits/stdc++.h>
#define rep(a,b,c) for(int a=b;a<c;a++)
#define rep2(a,b,c) for(ll a=b;a>c;a--)
#define pb push_back
#define x first
#define y second
#define all(x) x.begin(), x.end()
using namespace std;
using ll=long long;
using ti=tuple<ll,ll,ll>;
using pi=pair<ll,ll>;

ll N;
string S;

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin >> N >> S;
    rep(length, 1, N + 1){
        bool flag2 = 0;
        rep(i, 0, N - length + 1){
            rep(j, i + 1, N - length + 1){
                bool flag = 0;
                rep(k, 0, length) {
                    if(S[i + k] != S[j + k]){
                        flag = 1;
                        break;
                    }
                }
                if(flag == 0) {
                    flag2 = 1;
                    break;
                }
            }
            if(flag2) break;
        }
        if(!flag2){
            cout << length << endl;
            return 0;
        }
    }
}
```

### 3. Livestock Lineup  

```cpp
# pragma GCC optimize ("O3")
# pragma GCC optimize ("Ofast")
# pragma GCC optimize ("unroll-loops")
#include <bits/stdc++.h>
#define rep(a,b,c) for(int a=b;a<c;a++)
#define rep2(a,b,c) for(ll a=b;a>c;a--)
#define pb push_back
#define x first
#define y second
#define all(x) x.begin(), x.end()
using namespace std;
using ll=long long;
using ti=tuple<ll,ll,ll>;
using pi=pair<ll,ll>;

ll N;
string u, v, dummy, cand = "ZZZZZZZZZZZZZZZZZZZZZZZZZZ";
priority_queue<string, vector<string>, greater<string> > pq;
unordered_map<string, vector<string> > adj;
unordered_map<string, bool> visit;
unordered_map<string, ll> degree;

void BFS(string root){
    priority_queue<string> pq;
    pq.push(root); visit[root] = 1;
    while(!pq.empty()){
        string u = pq.top(); pq.pop();
        cout << u << "\n";
        for(string v : adj[u]){
            if(visit[v])continue;
            visit[v] = 1;
            pq.push(v);
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin >> N;
    rep(i, 0, N){
        cin >> u;
        rep(_, 0, 4) cin >> dummy;
        cin >> v;
        adj[u].pb(v);
        adj[v].pb(u);
        degree[u]++; degree[v]++;
    }
    for(string s : {"Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"
}) if(degree[s] < 2) pq.push(s);
        // cand = min(cand, it -> first);
    // pq.push(cand);
    while(!pq.empty()){
        u = pq.top(); pq.pop();
        if(visit[u]) continue;
        BFS(u);
    }
}
```


### Silver

#### 1. MooBuzz  

```cpp
# pragma GCC optimize ("O3")
# pragma GCC optimize ("Ofast")
# pragma GCC optimize ("unroll-loops")
#include <bits/stdc++.h>
#define rep(a,b,c) for(int a=b;a<c;a++)
#define rep2(a,b,c) for(ll a=b;a>c;a--)
#define pb push_back
#define x first
#define y second
#define all(x) x.begin(), x.end()
using namespace std;
using ll=long long;
using ti=tuple<ll,ll,ll>;
using pi=pair<ll,ll>;

ll N;

ll f(ll x){
    return x - (x / 3 + x / 5) + x / 15;
}

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin >> N;
    ll lo = 1, hi = 1e12;
    while(lo < hi){
        ll m = lo + hi >> 1;
        if(f(m) < N) lo = m + 1;
        else hi = m;
    }
    cout << lo << endl;
}
```

#### 2. Meetings

```cpp
# pragma GCC optimize ("O3")
# pragma GCC optimize ("Ofast")
# pragma GCC optimize ("unroll-loops")
#include <bits/stdc++.h>
#define rep(a,b,c) for(int a=b;a<c;a++)
#define rep2(a,b,c) for(ll a=b;a>c;a--)
#define pb push_back
#define x first
#define y second
#define all(x) x.begin(), x.end()
using namespace std;
using ll=long long;
using ti=tuple<ll,ll,ll>;
using pi=pair<ll,ll>;

const int MAX = 5e4;

ll N, L, W[MAX], X[MAX], D[MAX], tot, ans, cur, to_right[MAX], to_left[MAX], rsz, lsz;
vector<pi> Weights;
map<ll, vector<pi> > events;

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin >> N >> L;
    rep(i, 0, N){
        cin >> W[i] >> X[i] >> D[i]; tot += W[i];
        Weights.pb({X[i], W[i]});

        if(D[i] == 1) events[L - X[i]].pb({i, 1});
        else events[X[i]].pb({i, -1});

        if(D[i] == 1) to_right[rsz++] = X[i];
        else to_left[lsz++] = X[i];
    }
    sort(to_left, to_left + lsz);
    sort(to_right, to_right + rsz);
    sort(Weights.begin(), Weights.end());
    ll lo = 0, hi = N - 1;
    for(auto it = events.begin(); it != events.end(); it++){
        auto& v = it -> second;
        rep(i, 0, v.size()){
            if(v[i].y == 1)
                cur += Weights[hi--].y;
            else 
                cur += Weights[lo++].y;
        }
        if(cur >= tot / 2 + (tot % 2)){
            ll time = it -> first;
            rep(i, 0, rsz){
                ans += upper_bound(to_left, to_left + lsz, to_right[i] + time * 2) - lower_bound(to_left, to_left + lsz, to_right[i]);
            }
            cout << ans << endl;
            return 0;
        }
    }
}
```

#### 3. Milk Visits  

```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a=b;a<c;a++)
#define rep2(a,b,c) for(ll a=b;a>c;a--)
#define pb push_back
#define x first
#define y second
#define all(x) x.begin(), x.end()
using namespace std;
using ll=long long;
using ti=tuple<ll,ll,ll>;
using pi=pair<ll,ll>;

const int MAX = 1e5 + 5;

struct AB{
    ll x,y;
    AB operator + (AB o){
        return {x + o.x, y + o.y};
    }
    AB operator - (AB o){
        return {x - o.x, y - o.y};
    }
};

ll N, M, u, v, depth[MAX], par[MAX][18];
string S;
vector<ll> adj[MAX];
char c;

AB dp[MAX];
void dfs(ll u, ll prev){
    par[u][0] = prev;
    depth[u] = depth[prev] + 1;
    if(S[u-1]=='G') dp[u].x++;
    else dp[u].y++;
    for(auto v: adj[u]){
        if(v == prev) continue;
        dp[v] = dp[v] + dp[u];
        dfs(v, u);
    }
}
int LCA(int u,int v){
    if(depth[u]^depth[v]){
        if(depth[u]>depth[v])swap(u,v); //v가 깊게
        int t=depth[v]-depth[u];
        rep(k,0,18){
            if(t&(1<<k)){
                v=par[v][k];
            }
        }
    }
    if(u==v)return u;
    rep(k,0,18){
        if(par[u][17-k]^par[v][17-k]){
            u=par[u][17-k];
            v=par[v][17-k];
        }
    }
    return par[u][0];
}
int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin >> N >> M >> S;
    rep(i, 0, N - 1){
        cin >> u >> v;
        adj[u].pb(v); adj[v].pb(u);
    }
    dfs(1, 0);
    rep(k, 1, 18) rep(u, 1, N + 1) par[u][k] = par[par[u][k - 1]][k - 1];
    rep(_, 0, M){
        cin >> u >> v >> c;
        ll p = LCA(u, v);
        AB t;
        if(p == 0) t = dp[u] + dp[v] - dp[1];
        else t = dp[u] + dp[v] - dp[par[p][0]] - dp[p];

        if(c=='G') cout << (t.x>0);
        else cout << (t.y>0);
    }
}
```


### Gold  

#### 1. Milk Pumping  
푼 지가 오래되서 풀이가 기억이 안 난다. 솔루션을 보고 풀었었나?  


```cpp
# pragma GCC optimize ("O3")
# pragma GCC optimize ("Ofast")
# pragma GCC optimize ("unroll-loops")
#include <bits/stdc++.h>
#define rep(a,b,c) for(int a=b;a<c;a++)
#define rep2(a,b,c) for(ll a=b;a>c;a--)
#define pb push_back
#define x first
#define y second
#define all(x) x.begin(), x.end()
using namespace std;
using ll=long long;
using ti=tuple<ll,ll,ll>;
using pi=pair<ll,ll>;
const int MAX = 1e3 + 1;
const ll INF = 1e12;

struct Edge {
    ll u, v, c, f;
    Edge(): Edge(0,0,0,0){}
    Edge(ll u, ll v, ll c, ll f): u(u), v(v), c(c), f(f){}
} Edges[MAX];
ll N, M, u, v, c, f;
double ans;
vector<Edge> adj[MAX];

ll get_minimum_cost(ll S, ll E, ll limit){
    vector<ll> dist(N, INF);
    vector<bool> vis(N, 0);
    priority_queue<pi> pq;
    dist[S] = 0;
    pq.push({0, S});
    while(!pq.empty()){
        ll u;
        do {
            u = pq.top().y;
            pq.pop();
        } while (!pq.empty() && vis[u]);
        if(vis[u]) break;
        vis[u] = 1;
        for(auto &e : adj[u]){
            if(e.f < limit) continue;
            if(dist[e.v] > dist[u] + e.c){
                dist[e.v] = dist[u] + e.c;
                pq.push({-dist[e.v], e.v});
            }
        }
    }
    return dist[E];
}

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin >> N >> M;
    rep(i, 0, M) {
        cin >> u >> v >> c >> f; u--; v--;
        Edges[i] = {u, v, c, f};
        adj[u].pb({u, v, c, f});
        adj[v].pb({v, u, c, f});
    }
    rep(i, 0, M){
        u = Edges[i].u; v = Edges[i].v; c = Edges[i].c; f = Edges[i].f;
        ans = max(ans, 1.0 * f / (get_minimum_cost(0, u, f) + c + get_minimum_cost(v, N - 1, f)));
        swap(u, v);
        ans = max(ans, 1.0 * f / (get_minimum_cost(0, u, f) + c + get_minimum_cost(v, N - 1, f)));
    }
    cout << (ll) (ans * 1000000) << endl;
}
```

#### 2. Milk Visits  
이건 확실히 솔루션 보고 풀었던 기억이 난다.  

```cpp
/*
ID: milkclouds
LANG: C++
TASK: milkvisits
*/

# pragma GCC optimize ("O3")
# pragma GCC optimize ("Ofast")
# pragma GCC optimize ("unroll-loops")
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a=b;a<c;a++)
#define rep2(a,b,c) for(ll a=b;a>c;a--)
#define pb push_back
#define x first
#define y second
#define all(x) x.begin(), x.end()
using namespace std;
using ll=long long;
using ti=tuple<ll,ll,ll>;
using pi=pair<ll,ll>;
const ll MAX = 1e5 + 1;

ll N, M, T[MAX], u, v, c, ok[MAX], cnt;
vector<ll> adj[MAX], todo[MAX];
pi dfsn[MAX];
ti query[MAX];

void dfs(ll u, ll par){
    dfsn[u].x = cnt++;
    for(auto v: adj[u]) if(par ^ v) dfs(v, u);
    dfsn[u].y = cnt - 1;
}
vector<ll> ord;
vector<pi> S[MAX];
bool anc(ll a, ll b){
    return dfsn[a].x <= dfsn[b].x && dfsn[b].y <= dfsn[a].y;
}
void dfs2(ll u, ll par){
    S[T[u]].pb({u, ord.size() + 0}); ord.pb(u);
    for(auto i: todo[u]){
        ll a, b, c;
        tie(a, b, c) = query[i];
        if(!S[c].empty()){
            pi y = S[c].back();
            if(y.x == u) ok[i] = 1;
            else {
                ll Y = ord[y.y + 1];
                if(!anc(Y, a + b - u)) ok[i] = 1;
            }
        }
    }
    for(auto v: adj[u]) if(par ^ v) dfs2(v, u);
    S[T[u]].pop_back(); ord.pop_back();
}

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin >> N >> M;
    rep(i, 1, N + 1) cin >> T[i];
    rep(_, 1, N){
        cin >> u >> v;
        adj[u].pb(v); adj[v].pb(u);
    }
    dfs(1, 0);
    rep(i, 0, M){
        cin >> u >> v >> c;
        query[i] = make_tuple(u, v, c);
        todo[u].pb(i); todo[v].pb(i);
    }
    dfs2(1, 0);
    rep(i, 0, M) {
        cout << ok[i];
    }
}
```


#### 3. Moortal Cowmbat  

Floyd-Warshall Algorithm으로 먼저 dist값을 깔끔하기 만들어준다.  
이후 `dp[i][j] = (i번째까지 작업했을 때 최소 cost, 단 마지막 글자는 j)`로 설정한다. (마지막에서 최소 K개 문자는 j임을 내포)  

그럼 `dp[i][j] = dp[i - 1][j] + cost1`로, 글자 j가 이어지는 상황에 대한 점화식을 세운 후에, `dp[i][j] = min(dp[i][j], dp[i - K][j2] + cost2)`로 식을 세워서 글자 j가 이어지지 않는 상황에 대한 점화식을 세운다. 이렇게 최솟값을 구하면 된다.    


```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a = b; a < c; a++)
#define rep2(a,b,c) for(ll a = c - 1; a >=b; a--)
#define all(x) (x).begin(), (x).end()
#define pb push_back

using namespace std;
typedef long long ll;
typedef pair<ll, ll> pl;

const int MAXM = 26, MAXN = 1e5 + 1;
const ll INF = 1e15;

int N, M, K;
ll a[MAXM][MAXM], ans = INF, trans[MAXN][MAXM], sum[MAXN][MAXM], dp[MAXN][MAXM];
string S;


int main() {
    cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(false);
    cin >> N >> M >> K >> S;
    rep(i, 0, M) rep(j, 0, M) cin >> a[i][j];
    rep(m, 0, M) rep(i, 0, M) rep(j, 0, M) a[i][j] = min(a[i][j], a[i][m] + a[m][j]);
    rep(i, 0, N) rep(j, 0, M) trans[i][j] = a[S[i] - 'a'][j];
    rep(i, 0, N) rep(j, 0, M) sum[i + 1][j] = sum[i][j] + trans[i][j];
    rep(i, 0, K) rep(j, 0, M) dp[i][j] = INF;
    rep(i, 0, M) dp[K - 1][i] = sum[K - 1 + 1][i];
    rep(i, K, N) {
        rep(j, 0, M) {
            dp[i][j] = dp[i - 1][j] + trans[i][j];
            rep(j2, 0, M) {
                dp[i][j] = min(dp[i][j], dp[i - K][j2] + sum[i + 1][j] - sum[i - K + 1][j]);
            }
        }
    }
    rep(i, 0, M) ans = min(ans, dp[N - 1][i]);
    cout << ans;
}
```