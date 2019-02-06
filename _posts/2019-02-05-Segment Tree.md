---
layout: post
title: 'Segment Tree'
author: milkclouds
comments: true
date: 2019-02-05 23:29
tags: [algorithm]

---


### 개요

참고: [백준 블로그](https://www.acmicpc.net/blog/view/9)

1. 구간 `[left, right]`의 합
2. i 번째 수의 값 변경

Prefix Sum의 경우  
- 1번 쿼리는 `O(1)`   
- 2번 쿼리는 `O(n)`

Segment Tree의 경우  
- 1번 쿼리는 `O(lgn)`  
- 2번 쿼리는 `O(lgn)`


값의 변경(2번)이 잦은 경우 Prefix Sum은 사용할 수 없고, 여러가지 다른 구조를 사용하게 된다. 펜윅 트리나 세그먼트 트리가 대표적인데 세그먼트 트리에 대해 먼저 쓰려고 한다.  
세그먼트 트리도 여러가지 쿼리를 처리하면서, 쿼리에 따라서 구현 구조가 달라지겠지만 구간 합에 대한 세그먼트 트리로 글을 쓰려 한다.


### 세그먼트 트리

세그먼트 트리는 자식이 없는 리프 노드와 리프 노드가 아닌 노드로 나뉜다.

- 리프 노드: 배열의 수 자체를 저장
- 다른 노드: 왼쪽 자식과 오른쪽 자식의 합을 저장

어떤 노드의 번호가 `x`일때, 자식의 번호는 `2x`, `2x+1`이 된다. (처음은 1부터 시작하도록 하면 편하다.)  


![Segment Tree 1](/files/seg1.png)  
위 그림은 리프 노드가 아닌 노드가 저장하고 있는 리프 노드의 합의 범위를 나타낸 그림이다. 각 노드의 번호를 나타내면 다음과 같다.

![Segment Tree 2](/files/seg2.png)


### init

세그먼트 트리를 저장할 `tree` 배열의 크기를 정해보자.  
트리가 저장할 리프 노드의 개수 N이 2의 제곱꼴인 경우에 Full Binary Tree로 높이는 `lgN`, 노드 개수는 `2N-1`이 된다.  

N이 2의 제곱꼴이 아닌 경우에 높이는 `lgN`의 올림이고, 총 배열의 크기는 `2^(H+1)-1`이 된다.

간단하게 정하려면 배열의 크기를 `4N`으로 하면 된다. 메모리는 더 소모하지만 간편하다.


init 함수는 구간을 `[start,end)`라 했을 때[^1]  괄호 안의 수는 (node,start,end) 순서라고 가정했을 때 아래와 같다.  
1. `(1, 0, N)`에서 시작   
2. `node`가 리프 노드일 때, 즉 `start+1==end`일 때(기저 사례) `tree[node]`를 설정하고 값을 반환  
3. `node`가 리프 노드가 아닐 때 `(2x,start,mid)`, `(2x+1,mid,end)`의 함수값 2개를 더하여 `tree[node]`에 저장, 그리고 반환  


Python으로 구현하면 아래와 같다.
```python
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
        self.init(1,0,N)

 Seg1=SegTree(5,[1,35,2,3,16])
 ```

### sum (구간 합)  
`[start,end)` 범위의 합을 구하고자 할 때, 현재 노드가 `(node,left,right)`이면 경우는 다음의 3가지이다.  

1. `[left,right)` 가 `[start,end)`에 완전히 포함되는 경우  
2. `[left,right)` 와 `[start,end)`의 교집합이 없는 경우  
3. `[left,right)` 와 `[start,end)`가 부분만 포함되는 경우  

1번의 경우 함수는 `tree[node]`를 반환한다.    
2번의 경우 함수는 `0`을 반환한다.    
3번의 경우 `[left,mid)`, `[mid,right)`을 범위로 다시 합을 구해 더하고, 그 값을 반환한다.  

Python으로 구현하면 아래와 같다.  
```python
    def sum(self,node,left,right,start,end):
        if start<=left and right<=end:
            return self.tree[node]
        if right<=start or end<=left:
            return 0
        mid=(left+right)//2
        return self.sum(node*2,left,mid,start,end)+self.sum(node*2+1,mid,right,start,end)

```


### update (값 변경)

`target`번째 값을 `value`만큼 더하려면 2가지 경우가 있다.  
1. `[left,right)` 안에 `target`번째가 속한 경우  
2. 아닌 경우  

1번 경우에 `tree[node]+=value`을 실행하고, node가 리프 노드가 아니라면 `[left,mid)`, `[mid,right)` 범위로 다시 함수를 실행한다.  
2번 경우에 아무것도 하지 않는다.  


Python으로 구현하면 아래와 같다.  
```python
    def update(self,node,left,right,target,value):
        if left<=target<right:
            self.tree[node]+=value
            if left+1==right: return
            mid=(left+right)//2
            self.update(node*2,left,mid,target,value)
            self.update(node*2+1,mid,right,target,value)
```



### 전체 예제

[BOJ 2042번](https://www.acmicpc.net/problem/2042)의 풀이 겸 예제 소스이다.  

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
        self.init(1,0,N)

    def sum(self,node,left,right,start,end):
        if start<=left and right<=end:
            return self.tree[node]
        if right<=start or end<=left:
            return 0
        mid=(left+right)//2
        return self.sum(node*2,left,mid,start,end)+self.sum(node*2+1,mid,right,start,end)

    def update(self,node,left,right,target,value):
        if left<=target<right:
            self.tree[node]+=value
            if left+1==right: return
            mid=(left+right)//2
            self.update(node*2,left,mid,target,value)
            self.update(node*2+1,mid,right,target,value)


Seg1=SegTree(N,A)

for _ in range(M+K):
    a,b,c=map(int,input().split())
    b-=1
    if a==2:
        c-=1
        print(Seg1.sum(1,0,N,b,c+1))
    else:
        Seg1.update(1,0,N,b,c-Seg1.A[b])
        Seg1.A[b]=c
```

### 문제  
[BOJ 2042번: 구간 합 구하기](https://www.acmicpc.net/problem/2042)  
[BOJ 10868번: 최솟값](https://www.acmicpc.net/problem/10868)  
[BOJ 2357번: 최솟값과 최댓값](https://www.acmicpc.net/problem/2357)  


##### 각주  
국제 표준화 기구에 따르면 밑이 2인 이진 로그는 `lb(x)`, 밑이 10인 로그는 `lg(x)`라 표기하라고 권고한다고 한다.  
이 글에 쓰인 `lg`는 모두 `lb`인 셈.





[^1]: start는 포함 end는 미포함