---
layout: post
title: 'C++ STL - multimap'
author: milkclouds
comments: true
date: 2019-01-30 15:27
tags: [C++, STL]

---


## 설명

`multimap`은 연관 컨테이너(Associative container) 중 하나로, map과 비슷하지만 key값이 중복 가능하다.


### 멤버 함수

+ mm.begin()
+ mm.end()
+ mm.rbegin()
+ mm.rend()
+ mm.clear()
+ mm.count(key)
+ mm.empty()
+ mm.insert(pair<>)
+ mm.erase(start,end)
+ mm.find(key)
+ mm2.swap(mm1)
+ mm.value_comp()
+ mm.key_comp()
+ mm.size()
+ mm.upper_bound(key): upper bound Iterator 반환
+ mm.lower_bound(key): lower bound Iterator 반환
+ mm.equal_range(key): `[first, second)` 반복자를 가진 pair 반환



### 예제  

[BOJ 12791번](https://www.acmicpc.net/problem/12791)  
파이썬과 크게 다른 점은 없는데 묘하게 엄청 귀찮다. 그냥 문제가 귀찮다..  
multimap에 insert할 자료를 만들 때는 문제에서 `예제 답안 2`를 긁어와서 정규식 `(\d+) (\w.+)` -> `m.insert({$1,"$2"});` 으로 replace를 사용했다.
```c++
#include <bits/stdc++.h>
using namespace std;

multimap<int,string> m;
int main(){
	m.insert({1967,"DavidBowie"});
	m.insert({1969,"SpaceOddity"});
	m.insert({1970,"TheManWhoSoldTheWorld"});
	m.insert({1971,"HunkyDory"});
	m.insert({1972,"TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars"});
	m.insert({1973,"AladdinSane"});
	m.insert({1973,"PinUps"});
	m.insert({1974,"DiamondDogs"});
	m.insert({1975,"YoungAmericans"});
	m.insert({1976,"StationToStation"});
	m.insert({1977,"Low"});
	m.insert({1977,"Heroes"});
	m.insert({1979,"Lodger"});
	m.insert({1980,"ScaryMonstersAndSuperCreeps"});
	m.insert({1983,"LetsDance"});
	m.insert({1984,"Tonight"});
	m.insert({1987,"NeverLetMeDown"});
	m.insert({1993,"BlackTieWhiteNoise"});
	m.insert({1995,"1.Outside"});
	m.insert({1997,"Earthling"});
	m.insert({1999,"Hours"});
	m.insert({2002,"Heathen"});
	m.insert({2003,"Reality"});
	m.insert({2013,"TheNextDay"});
	m.insert({2016,"BlackStar"});
	int n;
	cin>>n;
	while(n--){
		int a,b,cnt=0;
		cin>>a>>b;
		for(int i=a;i<=b;i++){
			for(auto iter=m.equal_range(i).first; iter->first==i;iter++){cnt++;}
		}
		cout<<cnt<<"\n";
		for(int i=a;i<=b;i++){
			for(auto iter=m.equal_range(i).first; iter->first==i;iter++){cout<<i<<" "<<iter->second<<"\n";}
		}
	}
}
```