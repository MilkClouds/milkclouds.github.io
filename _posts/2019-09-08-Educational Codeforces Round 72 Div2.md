---
layout: post
title: 'Educational Codeforces Round 72 Div2'
author: milkclouds
comments: true
date: 2019-09-08 22:57
tags: [problem-solving, c++]

---
 

## Educational Codeforces Round 72 Div2  

[Educational Codeforces Round 72 (Rated for Div. 2)](http://codeforces.com/contest/1217) 


### A. Creating a Character  
부등식 잘 세우면 풀린다.  

```cpp
#include <bits/stdc++.h>
using namespace std;
 
void solve(){
	int a,b,z,i;
	cin>>a>>b>>z;
	i=b-a+z<0?0:(b-a+z)/2+1;
	cout<<max(0,z-i+1)<<'\n';
}
int main()
{
	ios_base::sync_with_stdio(0);cin.tie(0);
	int Q;
	cin>>Q;
	while(Q--){
		solve();
	}
	return 0;
}
```

### B. Zmei Gorynich  
막타를 날릴 죽창 하나와 짤짤이를 할 죽창 하나만 선별해내면 된다.  

아래 소스에서는 쓸데없이 정렬을 했는데 그럴 필요 없이 최대 원소만 구하면 된다. 어차피 n 크기가 100이라 아무 상관 없긴 하다.

```cpp
#include <bits/stdc++.h>
#define x first
#define y second
#define pb push_back
#define all(x) x.begin(), x.end()
using namespace std;
 
typedef pair<int,int> pii;
int solve(){
	int n,x,d,h,cnt=0;
	cin>>n>>x;
	vector<pii> kill, deal;
	for(int i=0;i<n;i++){
		cin>>d>>h;
		kill.pb({d,i});
		deal.pb({d-h,i});
	}
	sort(all(kill), greater<pii>());
	sort(all(deal), greater<pii>());
	int t=max(0,(x-kill[0].x));
	if(t>0 && deal[0].x<=0)return -1;
	return 1+ t/deal[0].x + (t%deal[0].x>0);
}
int main()
{
	ios_base::sync_with_stdio(0);cin.tie(0);
	int Q;
	cin>>Q;
	while(Q--){
		cout<<solve()<<'\n';
	}
	return 0;
}
```

### C. The Number Of Good Substrings  

대회 때 왠지 될 것 같은데? 하고 이분 탐색으로 해봤더니 의외로 잘 됐다.  

일단 성질이 2가지 있다.  

1. Good Substring 들은 전부 적당량의 leading zeros로 시작한 다음에, 1로 시작하는 실질적 의미가 있는 이진수 부분이 나온다.  
2. Good Substring에서 이진수 부분이 1이 아닌 이상 가장 뒷 문자열 하나를 잘라도 적당히 leading zeros의 개수를 조절해주면 또 Good Substring이 나온다. 이진수 부분이 작아지면 필요한 leading zeros의 양도 줄어들기 때문이다. 예를 들어서 000110을 찾았으면 011도 찾을 수 있다.

일단 1이 나오는 부분을 모아서 기록한다. 그리고 `a[i]=s[i] 앞에 나오는 연속되는 0의 개수`를 미리 구해 놓는다. 그리고 s[i]==1일 때, a[i]를 고려해서 이진수 부분의 시작이 s[i]인 Good Substring의 최대 길이를 구한다. 즉, 이분 탐색의 상한선으로 정한다. 하한선은 i로 한다. 그리고 이분 탐색으로 Good Substring의 일부가 될 수 있는 가장 긴 길이의 s[i:j+1] 이진수를 구한다. 그럼 답에는 j-i+1을 더하면 된다.  

이분 탐색 도중에 `int(s[i:j+1],2)`로 무식하게 이진수->십진수 변환을 시켰는데 이분 탐색 범위도, 횟수도 작아서 그런지 233ms만에 돌아간다.

```python
import sys;input=sys.stdin.readline
from math import *
 
for _ in range(int(input())):
	s=input().rstrip()
	n=len(s)
	a=[0]*n
	ll=[]
	for i in range(1,n):
		a[i]=a[i-1]+1 if s[i-1]=='0' else 0
	for i in range(n):
		if s[i]=='1':
			ll.append(i)
	ans=0
	for i in ll:
		lo=i
		nn=1
		while (1<<nn-1)-nn<=a[i]:
			nn+=1
		hi=min(n, lo+nn+1)
		while lo+1<hi:
			mid=(lo+hi)//2
			if int(s[i:mid+1],2)-(mid-i+1)>a[i]:
				hi=mid
			else:
				lo=mid
		ans+=lo-i+1
	print(ans)
```

D,E,F는 나중에 풀이해야겠다.