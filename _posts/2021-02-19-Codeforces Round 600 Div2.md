---
layout: post
title: 'Codeforces Round #600 (Div. 2)'
author: MilkClouds
comments: true
date: 2021-02-19 19:20
tags: [problem-solving]

---

## Codeforces Round \#600 (Div.2)  

[라운드 600 Div2](https://codeforces.com/contest/1253)  


### A. Simple Push
공식 풀이가 더 간단하다.  

```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a = b; a < c; a++)
#define rep2(a,b,c) for(ll a = c - 1; a >=b; a--)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define x first
#define y second
using namespace std;
using ll = long long;
using tl = tuple<ll, ll, ll>;
using pl = pair<ll, ll>;
using pi = pair<int, int>;
using ld = long double;

const int MAX = 1e5 + 5;
int TC, N, a[MAX], b[MAX];
void solve() {
	cin >> N;
	set<int> S;
	int END = 0;
	rep(i, 0, N)cin >> a[i];
	rep(i, 0, N)cin >> b[i];
	rep(i, 0, N)if (a[i] ^ b[i]) {
		if (a[i] > b[i] || END) {
			cout << "NO\n"; return;
		}
		S.insert(b[i] - a[i]);
	}
	else if (!S.empty()) END = 1;
	cout << (S.size() <= 1 ? "YES" : "NO") << "\n";
}


int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(false);
	cin >> TC;
	while (TC--)solve();
}
```


### B. Silly Mistake   
공식 풀이가 더 간단하다.  

```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a = b; a < c; a++)
#define rep2(a,b,c) for(ll a = c - 1; a >=b; a--)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define x first
#define y second
using namespace std;
using ll = long long;
using tl = tuple<ll, ll, ll>;
using pl = pair<ll, ll>;
using pi = pair<int, int>;
using ld = long double;

const int MAX = 1e5 + 3;
int N, A[MAX], last = -1;
vector<int> ans;
set<int> M, vis;

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(false);
	cin >> N;
	rep(i, 0, N)cin >> A[i];
	rep(i, 0, N) {
		if (A[i] > 0) {
			if (M.find(A[i]) != M.end() || vis.find(A[i]) != vis.end()) {
				cout << -1;
				return 0;
			}
			M.insert(A[i]);
			vis.insert(A[i]);
		}
		else {
			A[i] *= -1;
			if (M.find(A[i]) == M.end() || vis.find(A[i]) == vis.end()) {
				cout << -1;
				return 0;
			}
			M.erase(A[i]);
		}
		if (M.empty()) {
			vis.clear();
			ans.push_back(i - last);
			last = i;
		}
	}
	if (!M.empty()) {
		cout << -1;
		return 0;
	}
	cout << ans.size() << "\n";
	for (auto i : ans) cout << i << " ";
}
```

### C. Sweets Eating  


```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(ll a = b; a < c; a++)
#define rep2(a,b,c) for(ll a = c - 1; a >=b; a--)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define x first
#define y second
using namespace std;
using ll = long long;
using tl = tuple<ll, ll, ll>;
using pl = pair<ll, ll>;
using pi = pair<int, int>;
using ld = long double;

const int MAX = 2e5 + 3;
int N, M, A[MAX];
ll cur;
vector<ll> B;

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(false);
	cin >> N >> M;
	B.assign(M, 0);
	rep(i, 0, N)cin >> A[i];
	sort(A, A + N);
	rep(k, 0, N) {
		B[k % M] += A[k];
		cur += B[k % M];
		cout << cur << " ";
	}
}
```

### D. Harmonious Graph  
쓸데없이 긴데, dsu 미리 구현해둔 걸 그대로 가져다 써서 그렇다. DSU 없이 DFS만으로도 풀 수 있다.    

```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(int a = b; a < c; a++)
#define rep2(a,b,c) for(ll a = c - 1; a >=b; a--)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define x first
#define y second
using namespace std;
using ll = long long;
using tl = tuple<ll, ll, ll>;
using pl = pair<ll, ll>;
using pi = pair<int, int>;
using ld = long double;

const int INF = 1e9;

struct dsu {
	// if u is root : par[u] = -(size of tree)
	// else: par[u] = parent of u
public:
	dsu() : n(0) {}
	explicit dsu(int n) :n(n), par(n, -1), M(n, 0), m(n, 0) {
		rep(i, 0, n) M[i] = m[i] = i;
	}
	int merge(int u, int v) {
		assert(0 <= u && u < n);
		assert(0 <= v && v < n);
		u = find(u); v = find(v);
		if (u == v) return u;
		if (-par[u] < -par[v]) swap(u, v);
		par[u] += par[v];
		M[u] = max(M[u], M[v]);
		m[u] = min(m[u], m[v]);
		par[v] = u;
		return u;
	}
	int find(int u) {
		assert(0 <= u && u < n);
		if (par[u] < 0) return u;
		return par[u] = find(par[u]);
	}
	bool same(int u, int v) {
		assert(0 <= u && u < n);
		assert(0 <= v && v < n);
		return find(u) == find(v);
	}
	int size(int u) {
		assert(0 <= u && u < n);
		return -par[find(u)];
	}
	int getMax(int u) {
		assert(0 <= u && u < n);
		return M[find(u)];
	}
	int getMin(int u) {
		assert(0 <= u && u < n);
		return m[find(u)];
	}
	vector<vector<int> > groups() {
		vector<int> roots(n), groups(n);
		for (int i = 0; i < n; i++) {
			roots[i] = find(i);
			groups[roots[i]]++;
		}
		vector<vector<int> > result(n);
		for (int i = 0; i < n; i++) {
			result[i].reserve(groups[i]);
		}
		for (int i = 0; i < n; i++) {
			result[roots[i]].push_back(i);
		}
		result.erase(
			remove_if(result.begin(), result.end(), [&](const vector<int>& v) { return v.empty(); })
		);
		return result;
	}
private:
	int n;
	vector<int> par, M, m;
};

int N, M, u, v, cur = 1;
ll ans;

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(false);
	cin >> N >> M;
	dsu DSU = dsu(N + 1);
	rep(i, 0, M) {
		cin >> u >> v;
		DSU.merge(u, v);
	}
	rep(i, 1, N + 1) {
		while (DSU.getMax(i) - DSU.getMin(i) + 1 > DSU.size(i)) {
			cur = max(cur + 1, i + 1);
			if (DSU.same(i, cur)) continue;
			DSU.merge(i, cur);
			ans++;
		}
	}
	cout << ans;
}
```

### E. Antenna Coverage   
DP라는 걸 알았지만 구체적으로 어떻게 풀어야 할 지 감을 못 잡아서 못 풀었던 문제다. x=M에 안테나를 하나 두고 DP 쓰면 되는 걸 어떻게 발상을 해내야 되는걸까?   

```cpp
#include <bits/stdc++.h>
#define rep(a,b,c) for(int a = b; a < c; a++)
#define rep2(a,b,c) for(ll a = c - 1; a >=b; a--)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define x first
#define y second
using namespace std;
using ll = long long;
using tl = tuple<ll, ll, ll>;
using pl = pair<ll, ll>;
using pi = pair<int, int>;
using ld = long double;

const int INF = 1e9, MAX = 81;
int N, M, X[MAX], S[MAX], dp[100005];
pi A[MAX];



int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(false);
	cin >> N >> M;
	rep(i, 0, N) cin >> A[i].x >> A[i].y;
	sort(A, A + N);
	rep(i, 0, N) { X[i] = A[i].x; S[i] = A[i].y; }
	dp[M] = 0;
	rep2(i, 0, M) {
		dp[i] = M - i;
		rep(ant, 0, N) {
			int l = X[ant] - S[ant], r = X[ant] + S[ant];
			if (l <= i + 1 && i + 1 <= r)dp[i] = min(dp[i], dp[i + 1]);
			else if (i + 1 < l) {
				int tmp = l - i - 1;
				dp[i] = min(dp[i], dp[min(M, r + tmp)] + tmp);
			}
		}
	}
	cout << dp[0];
}
```

### F. Cheap Robot  
상당히 신박한 문제이다. 문제 파악을 잘 하면 풀 수 있으나, 구현이 많이 간단하지는 않다.  
