---
layout: post
title: 'Fenwick Tree'
author: MilkClouds
comments: true
date: 2019-02-05 23:48
tags: [algorithm]

---

참고: [백준 블로그](https://www.acmicpc.net/blog/view/21)


### 개요

펜윅 트리는 Binary Indexed Tree, BIT라고도 한다.

1. 구간 `[left, right]`의 합
2. i 번째 수의 값 변경

1,2 쿼리 모두 `O(logn)`에 실행한다.

BIT는 구현이 굉장히 쉬운 편이라 개인적으로 좋아하는 편이다.


### 펜윅 트리의 개념

개념은 [백준 블로그](https://www.acmicpc.net/blog/view/21)를 참고하자.  
나중에 개념 설명을 업데이트 할 수도?

### sum 함수

펜윅 트리는 C++로 작성하는 편이 뭔가 보기 좋아서 C++로 쓰겠다.

```c++
long long sum(int i){
	long long ret=0;
	for(;i;i^=i&-i)ret+=tree[i];
	return ret;
}
```

### update 함수

```c++
void update(int i,int x){
	for(;i<=N;i+=i&-i)tree[i]+=x;
}
```


### 예제 및 문제 풀이

[BOJ 2042번](https://www.acmicpc.net/problem/2042)의 BIT를 이용한 풀이이다.
```c++
#include <iostream>
using namespace std;

const int MAX=1e6+1;
typedef long long ll;
int N,M,K,t,a,b;
ll c,tree[MAX],A[MAX];
ll sum(int i){
	ll ret=0;
	for(;i;i^=i&-i)ret+=tree[i];
	return ret;
}
void update(int i,int x){
	for(;i<=N;i+=i&-i)tree[i]+=x;
}
int main(){
	ios_base::sync_with_stdio(0);cin.tie(0);
	cin>>N>>M>>K;
	for(int i=1;i<=N;i++){cin>>t;A[i]=t;update(i,t);}
	for(int i=0;i<M+K;i++){
		cin>>a>>b>>c;
		if(a&1){update(b,c-A[b]);A[b]=c;}
		else{cout<<sum(c)-sum(b-1)<<"\n";}
	}
}
```
