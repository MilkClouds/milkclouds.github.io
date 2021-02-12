---
layout: post
title: 'Slope Trick - 함수 개형을 이용한 최적화'
author: MilkClouds
comments: true
date: 2021-02-12 18:36
tags: [boj, problem-solving]

---

알고리즘에 대한 설명은 아래 링크에 있다.
[한글 설명](https://howtoliveworldnice.tistory.com/477)  
[영어 설명 코드포스](http://codeforces.com/blog/entry/47821)  




##### 문제풀이 소스  


BOJ 13324 BOJ 수열 2  
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
using tl = tuple<ll, ll, ll, ll>;
using pl = pair<ll, ll>;
using pi = pair<int, int>;
using ld = long double;

const int MAX = 1e6;
ll N, A[MAX], B[MAX];
priority_queue<ll> pq;

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(false);
	cin >> N;
	rep(i, 0, N) {
		cin >> A[i]; A[i] -= i;
	}
	rep(i, 0, N) {
		pq.push(A[i]); pq.push(A[i]); pq.pop();
		B[i] = pq.top();
	}
	rep2(i, 1, N) B[i - 1] = min(B[i - 1], B[i]);
	rep(i, 0, N) cout << B[i] + i << "\n";
}
```




[BOJ 문제집](https://www.acmicpc.net/workbook/view/4273)    

[Slope Trick 태그문제](https://www.acmicpc.net/problemset?sort=ac_desc&algo=157)
