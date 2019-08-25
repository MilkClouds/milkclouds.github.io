---
layout: post
title: 'Codeforces Round #580 (Div. 2)'
author: milkclouds
comments: true
date: 2019-08-20 21:00
tags: [problem-solving]

---

## Codeforces Round #580 (Div.2)  

[라운드 580](http://codeforces.com/contest/1206)에 참가했었다. PS를 한참 안 하다가 NYPC를 저번주에 풀고 도로 PS에 대한 관심이 생겼는데 A,B,C 세 문제밖에 풀지 못했다.  

[라운드 580 에디토리얼](https://codeforces.com/blog/entry/69158)을 참고로 남은 문제를 보고 있다.  



### A. Choose Two Numbers  
에디토리얼을 보니 최댓값끼리 더해서 `O(n+m)`으로 빠르게 돌리는 풀이가 있지만 애초에 입력 크기가 작아서 생각 없이 브루트 포싱 돌려도 된다. 두 풀이 모두 짜는 데 그렇게 오래 걸리진 않지만 최댓값끼리 더하는 게 그 때 생각이 안나서 빠르게 브루트포싱 돌리고 넘어갔다.

```cpp
#include <bits/stdc++.h>
using namespace std;
 
int n,m,a[205],b[205];
unordered_map<int,bool> mm;
int main(){
    cin>>n;
    for(int i=0;i<n;i++){cin>>a[i];mm[a[i]]=1;}
    cin>>m;
    for(int i=0;i<m;i++){cin>>b[i];mm[b[i]]=1;}
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(mm[a[i]+b[j]]==0){
                cout<<a[i]<<" "<<b[j];
                return 0;
            }
        }
    }
}
```

### B. Make Product Equal One  
음수는 -1로 만들어주되 -1이 홀수개면 가장 절댓값이 작은 수를 1로 보낸다. 그런데 -1이 홀수개인데 0이 있으면 0을 -1로 보내줄 수 있다. 이를 실수 없이 잘 짜면 된다.


```python
import sys
 
n=int(input())
a=[*map(int,input().split())]
chk=[];chk2=[];zero=0
for i in a:
    if i<0:
        chk.append(i)
    elif i>0:
        chk2.append(i)
    else:
        zero+=1
 
t=0
if len(chk)%2==0 or (len(chk)%2==1 and zero):
    t=-len(chk)-sum(chk)
else:
    t=-len(chk)-sum(chk)+2
 
print(sum(chk2)-len(chk2)+t+zero)
```

### C. Almost Equal  
예제를 보니 왠지 짝수가 입력으로 들어오면 NO일 것 같았다. 브루트포싱을 빠르게 짜서 N=6까지 돌려보고 그런 것 같아서 N=1,3,5일때 처음으로 만족되는 수의 패턴?을 보고 별 생각 없이 소스를 짰다. 수학적 생각은 아무것도 안 하고 얼른 다음 꺼 풀려고 그랬었는데 지금 생각해보면 맞은 게 용하긴 하다.

```python
n=int(input())
if n%2==0:
    print("NO")
    exit()
print("YES")
t=1
dt=[3,1]
for i in range(n):
    print(t,end=' ')
    t+=dt[i%2]
 
t=2
dt=[1,3]
for i in range(n):
    print(t,end=' ')
    t+=dt[i%2]
```

야매 말고 진짜 풀이는, 수식으로 복잡하진 않는데 이 블로그에 수식을 넣기가 귀찮아서 생략한다. 에디토리얼 보자.  



### D. Shortest Cycle  

비트 1,2,3,...60까지를 대상으로 생각해보자. 같은 비트가 3개 이상의 수에 있으면 그냥 3 출력하고 종료하면 된다. 그 경우가 아니라면 같은 비트가 최대 2개 수에 있다는 건데 그럼 각각의 수가 공통 비트를 하나라도 가지고 있으면 하나의 간선으로 이어주자.  

그리고 이어져 있는 두 수 u,v에 대해서, u<->v를 직접 이어주는 간선을 제거한 후 dist(u,v)를 구했는데 그게 존재하면 dist(u,v)+1이 사이클의 길이가 된다. 다만 같은 비트가 최대 2개 수에 있으면 N의 최댓값이 120이하로 줄어들므로 플로이드-워셜을 돌리면서 아래 소스처럼 찾아도 된다. 다른 소스 중에는 모든 u<->v간선에 대해 u<->v를 직접 이어주는 간선을 제거하고 BFS로 dist(u,v)를 찾는 것도 있었다.   

3 출력하는 경우가 아닐 때 N이 120 이하가 맞는지는 확실하지 않다. 아무튼 줄어드는 건 맞는데.

```cpp
#include <bits/stdc++.h>
using namespace std;
const int MAX=1e5+5,INF=1e9;
typedef long long ll;
ll N,a[MAX],A[MAX],p,mp[200][200],dis[200][200];

ll floyd(){
    ll ret=INF;
    for(int k=1;k<=N;k++){
        for(int i=1;i<k;++i)
            for(int j=i+1;j<k;j++)
                ret=min(ret,dis[i][j]+mp[i][k]+mp[k][j]);
        for(int i=1;i<=N;i++)for(int j=1;j<=N;j++)
            dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j]);
    }
    return ret;
}

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);
    cin>>N;
    for(int i=0;i<N;i++){
        cin>>a[i];
        for(ll j=0;j<63;j++)
            if(a[i]&((ll)1<<j))A[j]++;
    }
    for(int i=0;i<63;i++)if(A[i]>2){cout<<3;return 0;}
    for(int i=0;i<N;i++)if(a[i])A[++p]=a[i];
    N=p;
    for(int i=1;i<=N;i++)for(int j=1;j<=N;j++){
        if((A[i]&A[j])&&(i^j))mp[i][j]=dis[i][j]=1;
        else mp[i][j]=dis[i][j]=INF;
    }
    ll ret=floyd();
    cout<<(ret>N?-1:ret);
}
```

### E. Palindromic Paths  

문제 풀이는 에디토리얼을 보고 이해했다. 떠올리지는 절대 못할 것 같은데 풀이를 읽어보는건 쉽다.  
근데 읽어보고 구현해봤는데 어.. 역시나 안 된다. 가장 간단한 케이스는 되는데 어딘가를 잘못해서 안 된다. Test #3부터 실패하는데 지금은 시간이 없으니 나중에라도 고쳐봐야겠다. Interactive 문제는 손으로 입력 넣어보면서 디버깅하기도 좀 힘들다. 채점 프로그램을 만들거나 이미 있는 걸 쓰면 좋을텐데... 어떻게 만들지? 일단 삽질한 소스코드라도 올려둬야겠다.  

```cpp
#include <bits/stdc++.h>
using namespace std;
int table[51][51],N,memo[51][51],dp[51][51][51][51];
int query(int a,int b,int c,int d){
    if(dp[a][b][c][d])return dp[a][b][c][d]-1;
    int t;
    cout<<"? "<<a<<" "<<b<<" "<<c<<" "<<d<<'\n';
    cout.flush();
    cin>>t;
    dp[a][b][c][d]=t+1;
    return t;
}
void pprint(){
    for(int i=1;i<=N;i++){
        for(int j=1;j<=N;j++)
            cout<<table[i][j]<<"";
        cout<<'\n';
    }
}
struct coord{
    int x,y;
    coord(int x,int y):x(x),y(y){}
    coord():coord(1,1){}
    coord operator + (const int amt){
        int p=x,q=y;
        if(p+amt>N){
            q+=p+amt-N;p=N;
        }
        else p+=amt;
        return coord(p,q);
    }
    coord operator - (const int amt){
        int p=x,q=y;
        if(q-amt<1){
            p-=amt-q+1;q=1;
        }
        else q-=amt;
        return coord(p,q);
    }
    bool start(){return x<1;}
    bool end(){return y>N;}
} pos;
int f(coord& pos,int amt){
    coord t=pos+amt;
    return memo[t.x][t.y];
}
void insert(coord pos,int value){
    table[pos.x][pos.y]=value;
}
int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);
    cin>>N;
    for(int i=1;i<=N;i++)for(int j=1;j<=N;j++)table[i][j]=-1;
    table[1][1]=1; table[50][50]=0;
    // fill even table
    for(int i=1;i<=N;i++){
        for(int j=((i&1)^1)+1;j+2<=N;j+=2){
            table[i][j+2]=table[i][j]^query(i,j,i,j+2)^1;
        }
        if(i&1){
            if(i+1<=N)table[i+1][2]=table[i][1]^query(i,1,i+1,2)^1;
            if(i+2<=N)table[i+2][1]=table[i][1]^query(i,1,i+2,1)^1;
        }
    }
    for(int i=1;i<=N;i++)for(int j=1;j<=N;j++)if(~table[i][j])memo[i][j]=table[i][j];
    //memo odd table
    for(int i=1;i<=N;i++){
        for(int j=(i&1)+1;j+2<=N;j+=2)
            memo[i][j+2]=memo[i][j]^query(i,j,i,j+2)^1;
        if(i&1){
            if(i+1<=N){
                memo[i+1][3]=memo[i][2]^query(i,2,i+1,3)^1;
                memo[i+1][1]=memo[i+1][3]^query(i+1,1,i+1,3)^1;
            }
            if(i+2<=N)
                memo[i+2][2]=memo[i][2]^query(i,2,i+2,2)^1;
        }
    }
    // find a^b^c^d=0 for road from 1,1 to N,N
    pos.x=1;pos.y=1;
    while(!(pos+3).end()){
//      cout<<pos.x<<" "<<pos.y<<endl;
        if((f(pos,0)^f(pos,1)^f(pos,2)^f(pos,3))==0){
            if((pos.x+pos.y)&1){
                insert(pos,f(pos,3));
                insert(pos+2,f(pos,1));
            }
            else{
                insert(pos+1,f(pos,2));
                insert(pos+3,f(pos,0));
            }
            if(((pos.x+pos.y)&1)==0)pos=pos+1;
            coord t=pos;
            while(!(t-2).start()){
                int p=(t-2).x, q=(t-2).y;
                insert(t-2,f(t,0)^query(p,q,t.x,t.y)^1);
                t=t-2;
            }
            t=pos;
            while(!(t+2).end()){
                int p=(t+2).x, q=(t+2).y;
                insert(t+2,f(t,0)^query(t.x,t.y,p,q)^1);
                t=t+2;
            }
            break;
        }
        pos=pos+1;
    }
    for(int i=2;i<=N;i+=2){
        for(int j=(i&1)+1;j+2<=N;j+=2)
            table[i][j+2]=table[i][j]^query(i,j,i,j+2)^1;
    }
    for(int i=1;i<=N;i+=2){
        if(i+1<=N)
            table[i][2]=table[i+1][3]^query(i,2,i+1,3)^1;
        else
            table[i][2]=table[i-1][1]^query(i-1,1,i,2)^1;
        for(int j=2;j+2<=N;j+=2){
            table[i][j+2]=table[i][j]^query(i,j,i,j+2)^1;
        }
    }
    cout<<"!\n";
    pprint();
}
```


E,F는 꼭 제출해서 AC 받아보고 싶긴 하다. 근데 언제쯤 가능할련지.