---
layout: post
title: 'Lazy Propagation'
author: milkclouds
comments: true
date: 2019-02-05 13:38
tags: [algorithm]

---

참고: [백준 블로그](https://www.acmicpc.net/blog/view/26)

### 설명

Lazy Propagation은 보통 Segment Tree에 적용되는 기술로, 값의 업데이트를 미뤄서 연산을 절약한다는 개념이다.

범위 `[i,j]`의 값을 `diff`만큼 더할 때, 원래의 Segment Tree는 `O(NlogN)`이 걸리지만 Lazy Propagation을 적용하면 `O(logN)`이 걸린다.



![Lazy Propagation 1](/files/lazy1.png)  

파란색의 3~4와 5~7은 update 함수 실행 당시에 더 이상 업데이트를 수행하지 않고, lazy 배열에 값을 저장해둔다. 파란 노드 위는 update 함수 실행 당시에 업데이트 하고, 파란 노드 아래는 나중에 필요할 때 업데이트 하는 것이다.


### init 함수

init은 lazy 배열을 초기화 하는 것 외에는 다른 건 없다.


### propagation 함수

`lazy[node]`가 존재할 때, `tree[node]`를 업데이트 하고, `node`가 리프 노드가 아니라면 바로 아래 `node*2`번째와 `node*2+1`번째 노드에 전파하는 함수 propagation을 만든다.

```python
    def propagation(self,node,start,end):
        if self.lazy[node]==0: return
        self.tree[node]+=self.lazy[node]*(end-start)
        if start+1!=end:
            self.lazy[node*2]+=self.lazy[node]
            self.lazy[node*2+1]+=self.lazy[node]
        self.lazy[node]=0
```

### update 함수

update 함수는 가장 처음 propagation을 실행하고,  
1. 바꿔야 하는 범위에 현재 범위 `[left,right)`가 완전히 속해 있다면 `tree[node]`를 업데이트 하고, `node`가 리프 노드가 아니라면 `lazy[node*2]`와 `lazy[node*2+1]`에 lazy를 전파한다. 그리고 종료한다.  
2. 바꿔야 하는 범위와 현재 범위의 교집합이 없으면 종료한다.
3. `[left,mid)`, `[mid,right)` 범위 대상으로 update를 실행한다.
4. `node`의 자식 노드 2개의 합을 `tree[node]`로 설정한다.

```python
    def update(self,node,left,right,start,end,value):
        self.propagation(node,left,right)
        if start<=left and right<=end:
            self.tree[node]+=(right-left)*value
            if left+1!=right:
                self.lazy[node*2]+=value
                self.lazy[node*2+1]+=value
            return
        if right<=start or end<=left:
            return
        mid=(left+right)//2
        self.update(node*2,left,mid,start,end,value)
        self.update(node*2+1,mid,right,start,end,value)
        self.tree[node] = self.tree[node*2] + self.tree[node*2+1]
```

### sum 함수

propagation 함수를 처음 실행 하는 것 외에는 보통의 Segment Tree와 같다.  


### 예제 및 문제 풀이

[BOJ 10999번](https://www.acmicpc.net/problem/10999)의 풀이이다.
```python
import sys;input=sys.stdin.readline

N,M,K=map(int,input().split())
A=[int(input()) for _ in range(N)]

class SegTree:
    def init(self,node,left,right):
        if left+1==right:
            self.tree[node]=self.A[left]
        else:
            mid=(left+right)//2
            self.tree[node]=self.init(node*2,left,mid)+self.init(node*2+1,mid,right)
        return self.tree[node]

    def __init__(self,N,A):
        self.A=A
        self.tree=[0]*4*N
        self.lazy=[0]*4*N
        self.init(1,0,N)

    def sum(self,node,left,right,start,end):
        self.propagation(node,left,right)
        if start<=left and right<=end:
            return self.tree[node]
        if right<=start or end<=left:
            return 0
        mid=(left+right)//2
        return self.sum(node*2,left,mid,start,end)+self.sum(node*2+1,mid,right,start,end)

    def propagation(self,node,start,end):
        if self.lazy[node]==0: return
        self.tree[node]+=self.lazy[node]*(end-start)
        if start+1!=end:
            self.lazy[node*2]+=self.lazy[node]
            self.lazy[node*2+1]+=self.lazy[node]
        self.lazy[node]=0

    def update(self,node,left,right,start,end,value):
        self.propagation(node,left,right)
        if start<=left and right<=end:
            self.tree[node]+=(right-left)*value
            if left+1!=right:
                self.lazy[node*2]+=value
                self.lazy[node*2+1]+=value
            return
        if right<=start or end<=left:
            return
        mid=(left+right)//2
        self.update(node*2,left,mid,start,end,value)
        self.update(node*2+1,mid,right,start,end,value)
        self.tree[node] = self.tree[node*2] + self.tree[node*2+1]


Seg1=SegTree(N,A)

for _ in range(M+K):
    it=map(int,input().split())
    if next(it)==2:
        b,c=it
        print(Seg1.sum(1,0,N,b-1,c))
    else:
        b,c,d=it
        Seg1.update(1,0,N,b-1,c,d)
```