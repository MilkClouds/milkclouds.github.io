---
layout: post
title: 'Codeforces Round 583 Div1+Div2'
author: milkclouds
comments: true
date: 2019-09-07 22:30
tags: [problem-solving, c++]

---
 

## Codeforces Round #583 (Div.1+Div2)  

[Codeforces Round #583 (Div. 1 + Div. 2, based on Olympiad of Metropolises)](http://codeforces.com/contest/1214) 

F,G,H번은 Div1+Div2 라서 그런지 어려워 보이기도 하고 적정 레이팅이 높게 책정되어 있는 걸 보고 그냥 안 풀었다. 그래서 이 포스트에 풀이는 A부터 E번까지 있다.    


### A. Optimal Currency Exchange  

어렵게 내면 어려울 듯한 문제지만 A번이라 그런지 브루트 포싱으로 풀 수 있다.
한 화폐는 굳이 더 비싼 화폐 사지 않고 1짜리 사면 되고 다른 화폐는 5짜리 사도 아무 상관 없다. 그거 생각해서 구현하면 된다.

```cpp
#include <bits/stdc++.h>
using namespace std;
 
int n,d,e;
int main(){
	cin>>n>>d>>e;
	int ans=n;
	for(int i=0;i*5*e<=n;i++)
		ans=min(ans, (n-i*5*e)%d);
	cout<<ans;
}
```

### B. Badges  
부등식 좀 세워서 끄적거리면 풀 수 있다.

```cpp
#include <bits/stdc++.h>
using namespace std;
 
int b,g,n;
int main(){
	cin>>b>>g>>n;
	int l=max(0,n-g),r=min(n,b);
	cout<<r-l+1;
}
```


### C. Bad Sequence  
괄호 개수가 안 맞으면 뭘 해도 No를 출력하고, 괄호 개수는 맞는데 순서가 안 맞으면 `(`에 상쇄되지 않는 `)`가 2번 이상 나오면 No를 출력하면 된다. 1번 나오는 경우에는 그 괄호를 옮기든 해서 상쇄시킬 수 있다.

```cpp
#include<bits/stdc++.h>
using namespace std;
 
int n,t,cnt;
string s;
 
int main(){
	cin>>n>>s;
	for(int i=0;i<n;i++){
		t+=(s[i]=='(')-(s[i]==')');
		if(t<0)cnt=1;
		if(t==-2){cout<<"No";return 0;}
	}
	if(t){cout<<"No";return 0;}
	cout<<"Yes";
}
```

### D. Treasure Island  
C까지는 쉬웠는데.. D도 그렇게 어려운 건 아니고 0,1,2만 잘 구분하면 되는데 대회 때는 반례를 못 찾아서 실패했다. 처음 지점에서 끝 지점까지 갈 수 있는 길 위의 블럭을 유효하다고 하자. 유효한 블럭은 시작 지점에서 DFS 한번 돌려서 방문 지점 기록하고 끝 지점에서부터 DFS 한 번 돌려서 방문 지점을 기록할 때, 둘의 공통집합이라고 할 수 있다.  

유효한 블럭이 없으면 0을 출력한다. 시작 지점에서 같은 거리에 있으면서 유효 블럭이 하나인 경우가 하나라도 있으면 그 블럭만 막으면 되니까 1을 출력한다. 나머지 경우는 2를 출력한다.

```cpp
#include<bits/stdc++.h>
using namespace std;
 
int dx[]={0,1},dy[]={1,0};
int N,M,cnt[2000005],flag;
vector<vector<int> > chk;
string S[1000005];
 
void dfs(int x,int y){
	if(chk[x][y]&flag)return;
	chk[x][y]|=flag;
	if(chk[x][y]==3)cnt[x+y]++;
	for(int i=0;i<2;i++){
		int nx=x+dx[i], ny=y+dy[i];
		if(nx<0||ny<0||nx>=N||ny>=M)continue;
		if(S[nx][ny]=='#')continue;
		dfs(nx,ny);
	}
}
int main(){
	ios_base::sync_with_stdio(0);cin.tie(0);
	cin>>N>>M;
	for(int i=0;i<N;i++)chk.push_back(vector<int>(M));
	for(int i=0;i<N;i++)cin>>S[i];
	flag=1;dfs(0,0);
	dx[1]=-1;dy[0]=-1;
	flag=2;dfs(N-1,M-1);
	for(int i=0;i<N+M-1;i++){
		if(i==0||i==N+M-2)continue;
		if(cnt[i]==1){cout<<1;return 0;}
		if(cnt[i]==0){cout<<0;return 0;}
	}
	cout<<2;
}
```

### E. Petya and Construction Set  

Moreover, the following **important** conditions holds: the value of `d_{i}` is never greater than `n`  

이 문장이 핵심적인 힌트다. 그리고 처음부터 n을 현재 문제의 2n 크기로 주지 않고 n 크기로 주는 것도 힌트인 것 같다.  

일단 큰 거리를 요구하는 노드부터 순서대로 처리한다. 먼저 n 길이의 일직선 모양의 트리를 상상하자. 현재 1 위치에 2i-1번 노드를 배치한다고 하면, `d_{i}<n-1`이면 `d_{i}-1`번 노드의 자식으로 2i의 값을 가진 노드를 붙인다. `d_{i}=n-1`이면 일직선 모양의 트리 맨 끝, 즉 n+1 위치에 2i의 값을 가진 노드를 새로 만든다. 이걸 반복해 나가면 문제 없이 모든 노드를 배치할 수 있다.  

대회 끝나고 혼자 생각해보다 풀었는데 나쁘지 않은 문제인 것 같다.

```cpp
#include <bits/stdc++.h>
#define pb push_back
using namespace std;
 
typedef pair<int,int> pii;
typedef vector<int> vi;
int N,t,cur,len;
priority_queue<pii> pq;
vi root;
vector<vi> branch;
int main(){
	ios_base::sync_with_stdio(0);cin.tie(0);
	cin>>N;
	for(int i=1;i<=N;i++){
		cin>>t;
		pq.push({t,i});
	}
	len=N; for(int i=0;i<len;i++) branch.pb({});
	root.resize(len);
	while(!pq.empty()){
		int d=pq.top().first, i=pq.top().second; pq.pop();
		if(cur+d>=len){
			len++;
			root.pb(2*i-1);branch.pb({});
		}
		else{
			branch[cur+d-1].pb(2*i-1);
		}
		root[cur++]=2*i;
	}
	for(int i=0;i<len;i++){
		for(auto j:branch[i]) cout<<root[i]<<" "<<j<<"\n";
		if(i)cout<<root[i-1]<<" "<<root[i]<<"\n";
	}
}
```