---
layout: post
title: '[BOJ 12152] Less Money, More Problems'
author: milkclouds
comments: true
date: 2019-05-18 21:15
tags: [boj, problem-solving, c++]

---

## 문제
[https://www.acmicpc.net/problem/12152](https://www.acmicpc.net/problem/12152)  
Google Code Jam 2015 > Round 1C C2번

## 사용 알고리즘  
그리디로 볼 수 있을 듯하다   


## 시간 복잡도  
생략 


## 설명  
부끄럽게도 풀이법을 제대로 생각해내지 못해서 힌트를 듣고 풀었었다. 구글 코드잼 문제였는데 알고 보면 쉬운 꽤나 좋은 문제 같다.

만들 수 있는 최대의 금액을 계산하고, 그 금액+1을 만들 수 있나 없나 점검한다.
못 만들면 그 금액 동전을 만들고, 만들 수 있으면 넘어간다.

### 소스  

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll=long long;

ll T,TC,C,D,V,a,N,ans;

int main(){
    cin>>T;
    for(int TC=1;TC<=T;TC++){
        cin>>C>>D>>V;
        queue<int> Q;
        for(int i=0;i<D;i++){
            cin>>a;
            Q.push(a);
        }
        N=0;ans=0;
        while(N<V){
            ll X=N+1;
            if(!Q.empty() && Q.front()<=X)X=Q.front(),Q.pop();else ans++;
            N+=X*C;
        }
        printf("Case #%d: %d\n",TC,ans);
    }
}
```