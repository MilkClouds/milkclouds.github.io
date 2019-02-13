---
layout: post
title: '플로이드 워셜 알고리즘 (Floyd-Warshall Algorithm)'
author: milkclouds
comments: true
date: 2019-02-12 23:47
tags: [algorithm]

---


### 개요  
그래프에서 최단 거리를 구하는 알고리즘 중 하나로 벨만 포드나 다익스트라와 다른 특징들이 많다.
1. 모든 노드 쌍에 대한 최단 거리를 구한다.  
2. 음의 가중치가 있어도 사용 가능하다.  
3. 시간 복잡도가 `O(V^3)`이므로 간선이 많고 정점이 적은 그래프에 적합하다. (밀집 그래프, `Dense Graph`라고 한다.)
4. 유향, 무향 그래프 모두 사용 가능하다.  
5. 다만 음수 가중치 사이클이 있다면 정상 작동하지 않을 수도 있다.


### 설명  
기본적으로, 시작 지점과 중간 지점과 끝 지점이 있을 때, 시작 지점에서 중간 지점까지의 최단 거리와 중간 지점에서 끝 지점까지 최단 거리는 시작 지점에서 끝 지점까지의 최단 거리라는 생각에서 시작한다.  
이 알고리즘의 정당성이라든지, 관련된 증명이라던지는 이것보다 복잡할 것 같지만 구현 소스 자체를 보면 굉장히 간단하다. 여러모로 굉장한 알고리즘이다.  

구현은 3중 for문으로 구현하되, 중간 지점을 처음 for문으로 설정하면 된다.  
구현은 아래 소스를 참고하자.   

```cpp
for(m=1; m<=N; m++)
    for(s=1; s<=N; s++)
      for(e=1; e<=N; e++)
         d[s][e]=d[s][e] > d[s][m] + d[m][e] ? d[s][m]+d[m][e] : d[s][e];
```

### 문제  
[BOJ 11404번: 플로이드](https://www.acmicpc.net/problem/11404)  

### 예제

[BOJ 11404번: 플로이드](https://www.acmicpc.net/problem/11404)의 답안 소스겸 예제이다.  
```python
import sys
input=sys.stdin.readline

INF=1<<20
v=int(input())
e=int(input())
g=[[INF]*v for _ in range(v)]

for _ in range(e):
    a,b,c=map(lambda x:int(x)-1,input().split())
    g[a][b]=min(g[a][b],c+1)

for m in range(v):
    for s in range(v):
        for e in range(v):
            g[s][e]=min(g[s][e],g[s][m]+g[m][e])
for i in range(v):
    g[i][i]=INF
for i in g:
    for j in i:
        print(j if j!=INF else 0,end=' ')
    print()
```