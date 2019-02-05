---
layout: post
title: 'Segment Tree'
author: milkclouds
comments: true
date: 2019-02-05 23:29
tags: [algorithm]

---


## 개요

https://www.acmicpc.net/blog/view/9

1. 구간 `[left, right]`의 합
2. i 번째 수의 값 변경

Prefix Sum  
- 1번 쿼리는 `O(1)`  
- 2번 쿼리는 `O(n)`

Segment Tree  
- 1번 쿼리는 `O(lgn)`  
- 2번 쿼리는 `O(lgn)`


값의 변경(2번)이 잦은 경우 Prefix Sum은 사용할 수 없고, 여러가지 다른 구조를 사용하게 된다.  

펜윅 트리나 세그먼트 트리가 대표적인데 세그먼트 트리에 대해 먼저 쓰려고 한다.


## 설명

세그먼트 트리는 자식이 없는 리프 노드와 리프 노드가 아닌 노드로 나뉜다.

- 리프 노드: 배열의 수 자체를 저장
- 다른 노드: 왼쪽 자식과 오른쪽 자식의 합을 저장

어떤 노드의 번호가 `x`일때, 자식의 번호는 `2x`, `2x+1`이 된다. (처음은 1부터 시작하도록 하면 편하다.)

!(/files/seg1.png)

Lazy Propagation과 마찬가지로 보충 예정
