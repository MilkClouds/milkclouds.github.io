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

###### 1. 기본

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


###### 2. 체  

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

###### 2. Fenwick Tree

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
