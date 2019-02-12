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


### 설명  
설명은 나중에 업데이트  

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