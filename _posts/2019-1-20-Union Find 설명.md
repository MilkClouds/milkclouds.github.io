---
layout: post
title: 'Union Find 설명'
author: milkclouds
comments: true
date: 2019-01-20 17:38
tags: [c++, disjoint-set, union-find, algorithm]

---


## 설명

원소 a,b가 있을 때 두 원소가 같은 집합에 속해 있는지 확인하기 위해 쓰는 자료구조를 Union Find라고 합니다. 보통 2가지 연산을 기본적으로 구현합니다.

Union(merge)
: 두 집합을 합쳐서 하나로 만든다.

Find  
: 어떤 원소가 어떤 집합에 속하는 지 알기 위해 루트 노드를 찾아낸다.


## 문제

[BOJ 1717번](https://www.acmicpc.net/problem/1717)  
가장 기본적인 서로소 집합 문제입니다.

[BOJ 4195번](https://www.acmicpc.net/problem/4195)

[BOJ 2464번](https://www.acmicpc.net/problem/2463)  
KOI 지역본선 2011 고등부 4번으로, 풀기 전엔 어려운데 풀고 나면 쉬워보이는 문제..

[BOJ 1922번](https://www.acmicpc.net/problem/1922)  
최소 스패닝 트리 문제로, 서로소 집합을 사용하는 크루스컬 알고리즘으로 풉니다.  

### 예제  

[BOJ 1717번](https://www.acmicpc.net/problem/1717) 풀이를 예제로 넣겠습니다.
보통 Disjoint Set은 트리 비슷하게 만드는데, 2가지 최적화를 적용합니다.

경로 압축
: Find 연산을 시행했을 때 시행 결과를 저장해 두어 다시 Find 연산을 시행할 때 시간을 줄입니다.

트리 편향 방지(Official 표현은 아닙니다.)
: 트리가 한 쪽으로 치우치면 Find 연산이 `O(n)`에 가까워져 버리므로 균형잡힌 트리를 만들기 위해 시행합니다. 예제에서는 트리와 트리를 합칠 때 짧은 트리를 긴 트리의 노드로 넣어서 해결합니다. 또는 안정성은 떨어질지라도 랜덤 연산으로 구현할 수도 있긴 합니다.

```c++
#include <iostream>

using namespace std;

int n,m,cmd,a,b;
int parent[1000001];
int ranks[1000001];

void init(int n){while(n--){parent[n]=n;ranks[n]=1;}}

int find(int u){
	if(u==parent[u])return u;
	return parent[u]=find(parent[u]);
}

void merge(int u,int v){
	u=find(u);v=find(v);
	if(u==v)return;
	if(ranks[u]>ranks[v])swap(u,v);
	parent[u]=v;
	if(ranks[u]==ranks[v])ranks[v]++;
}

int main(){
	cin.tie(0);ios_base::sync_with_stdio(0);
	cin>>n>>m;
	init(n+1);
	while(m--){
		cin>>cmd>>a>>b;
		if(cmd)
			cout<<(find(a)==find(b)?"YES":"NO")<<"\n";
		else
			merge(a,b);
	}
}
```