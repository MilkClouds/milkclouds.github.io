---
layout: post
title: 'Kadane Algorithm'
author: milkclouds
comments: true
date: 2019-02-01 0:10
tags: [algorithm]

---


## 설명

일종의 슬라이딩 윈도우 기법으로 `O(N)`에 Maximum SubArray Sum을 구한다.
수열의 연속 부분합 중 최대를 찾는다.

1. 앞에서부터 수를 더하면서 sum 변수에 매번 값을 저장한다.
2. sum<0 -> sum=0
3. ans=max(ans,sum)


#### 각주

원래 알고 있던 알고리즘인데 알고리즘 이름이 있는 줄은 몰랐다. 카나데로 읽었지만 카데인이었다...