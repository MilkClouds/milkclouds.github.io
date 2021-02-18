---
layout: page
title: About
permalink: /about/
image: /files/covers/blog.jpg
sitemap: yes
tags: [about]
---

## 정보

* 서울고등학교 - 졸업
* 서울대학교 물리천문학부 물리학전공 - 재학중   
* [GitHub](https://github.com/milkclouds)  
* [BOJ](https://www.acmicpc.net/user/milkclouds)  
* [Code Forces](http://codeforces.com/profile/)  

## Contact
* milkclouds@snu.ac.kr



##### PS 양식  

###### Python 입출력  

```python
import sys
input = sys.stdin.readline
```

```python
import sys
for line in sys.stdin:
	pass
```


###### cpp 기본

```cpp
# pragma GCC optimize ("O3")
# pragma GCC optimize ("Ofast")
# pragma GCC optimize ("unroll-loops")
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



int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(false);

}
```

###### 팩토리얼, 팩토리얼 인버스, 거듭제곱, 조합 계산  

```cpp
struct combinatorics {
	combinatorics() : combinatorics(0) {}
	combinatorics(long long N, int MOD = MOD1) : MOD(MOD), fac(N + 1), fac_inv(N + 1), inv(N + 1) {
		fac[0] = fac[1] = 1;
		rep(i, 2, N + 1) fac[i] = fac[i - 1] * i % MOD;
		fac_inv[N] = pow(fac[N], MOD - 2);
		rep2(i, 0, N) fac_inv[i] = fac_inv[i + 1] * (i + 1) % MOD;
		rep(i, 1, N + 1)inv[i] = fac[i] * fac_inv[i - 1] % MOD;
	}
	long long pow(long long a, long long b) {
		long long ret = 1;
		while (b) {
			if (b & 1) ret *= a;
			a *= a;
			a %= MOD;
			ret %= MOD;
			b >>= 1;
		}
		return ret;
	}
	long long C(long long n, long long r) {
		return fac[n] * fac_inv[r] % MOD * fac_inv[n - r] % MOD;
	}
	vector<long long> fac, fac_inv, inv;
	int MOD;
	const static int MOD1 = 998244353;
	const static int MOD2 = 1e9 + 9;
};
```


###### DSU  

```cpp
struct dsu {
	// if u is root : par[u] = -(size of tree)
	// else: par[u] = parent of u
public:
	dsu() : n(0) {}
	explicit dsu(int n):n(n), par(n, -1){}
	int merge(int u, int v){
		assert(0 <= u && u < n);
		assert(0 <= v && v < n);
		u = find(u); v = find(v);
		if (u == v) return u;
		if (-par[u] < -par[v]) swap(u, v);
		par[u] += par[v];
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
	vector<int> par;
};
```


###### 체  

```cpp
vector<ll> pn;
bool arr[MAX];

void erato() {
	pn.push_back(2);
	rep(i, 3, MAX) {
		if (arr[i]) continue;
		pn.push_back(i);
		for (ll j = i * i; j < MAX; j += i) arr[j] = 1;
	}
}
```

###### Fenwick Tree

사용 전 트리 크기인 MAX와 배열 크기인 N 조심  

```cpp
struct FenwickTree {
	ll tree[MAX];
	ll query(int i) {
		ll ret = 0;
		for (; i; i ^= i & -i)ret += tree[i];
		return ret;
	}
	void update(int i, int x) {
		for (; i <= N; i += i & -i)tree[i] += x;
	}
} tree;
```




###### FFT, FFT 이용한 이산 합성곱

```cpp
void fft(vector<cpx> &f, cpx w) {
	int n = f.size();
	if (n == 1) return;
	vector<cpx> even(n >> 1), odd(n >> 1);
	for (int i = 0; i < n; i++) { (i & 1 ? odd : even)[i / 2] = f[i]; }
	fft(even, w * w); fft(odd, w * w);
	cpx wp(1, 0);
	for (int i = 0; i < n / 2; i++) {
		f[i] = even[i] + wp * odd[i];
		f[i + n / 2] = even[i] - wp * odd[i];
		wp *= w;
	}
}
vector<cpx> mul_fft(vector<cpx> a, vector<cpx> b) {
	int n = 1;
	while (n <= a.size() || n <= b.size()) n <<= 1;
	n <<= 1;
	a.resize(n); b.resize(n); vector<cpx> c(n);
	cpx w(cos(2 * PI / n), sin(2 * PI / n));
	fft(a, w); fft(b, w);
	for (int i = 0; i < n; i++) c[i] = a[i] * b[i];
	fft(c, cpx(w.real(), -w.imag()));
	for (int i = 0; i < n; i++) {
		c[i] /= cpx(n, 0);
		c[i] = cpx(round(c[i].real()), round(c[i].imag()));
	}
	return c;
}
```
