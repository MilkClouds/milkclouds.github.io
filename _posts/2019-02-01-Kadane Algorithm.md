---
layout: post
title: 'Kadane Algorithm'
author: MilkClouds
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


## 문제  
우연히 찾았는데, 놀랍게도 KOI에 관련 문제가 있었다. 1996 KOI 중등부 1번 문제, [BOJ 2670번: 연속부분최대곱](https://www.acmicpc.net/problem/2670)을 Kadane Algorithm을 변형하여 사용할 수 있다.  
기존의 Kadane Algorithm에서 덧셈 연산을 곱셈으로 바꿔주고 1보다 작을때 1로 만들어주면 된다.

  
## 예제 소스  
[BOJ 2670번: 연속부분최대곱](https://www.acmicpc.net/problem/2670)의 정답 소스이다.

```c++
#include <iostream>
using namespace std;

int N;
double t=1,MAX,a;

int main(){
	cin>>N;
	while(N--){
		cin>>a;
		t*=a;
		MAX=max(MAX,t);
		if(t<1)t=1;
	}
    cout.precision(3);
	cout<<fixed<<MAX;
}
```



#### 각주

원래 알고 있던 알고리즘인데 알고리즘 이름이 있는 줄은 몰랐다. 카나데로 읽었지만 카데인이었다...