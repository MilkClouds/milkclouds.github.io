---
layout: post
title: 'Codeforces Round #582 (Div. 3)'
author: MilkClouds
comments: true
date: 2019-08-31 22:13
tags: [problem-solving]

---

## Codeforces Round #582 (Div.3)  

[라운드 582 Div3](http://codeforces.com/contest/1213)  


### A. Chips Moving  
홀수 칩 개수를 odd라고 하면 답은 `min(odd,n-odd)`다. `O(n)`  

아래 소스는 입력 범위 보고 그냥 빨리 풀려고 무식하게 구현한 소스다.

```cpp
#include<bits/stdc++.h>
using namespace std;
 
int n,x[105];
 
int solve(int target){
    int ret=0;
    for(int i=0;i<n;i++){
        ret+=abs(x[i]-x[target])&1;
    }
    return ret;
}
int main(){
    cin>>n;
    for(int i=0;i<n;i++)cin>>x[i];
    int m=1e9;
    for(int i=0;i<n;i++)m=min(m,solve(i));
    cout<<m;
}
```


### B. Bad Prices  
문제 읽다가 스토리가 이해가 안 되서 그냥 입력 출력에 필요한 부분만 읽고 풀었다. 수열이 주어졌을 때, `i` 위치의 정수 `a[i]`가 있으면 `i<j, a[j]<a[i]`인 j가 존재하는 i의 개수를 세면 된다.  

```cpp
#include<bits/stdc++.h>
using namespace std;
const int MAX=1e6+5;
int T,n,a[MAX],b[MAX];
 
int main(){
    cin>>T;
    while(T--){
        cin>>n;
        int ans=0;
        for(int i=0;i<n;i++)cin>>a[i];
        b[n]=1e9;
        for(int i=n-1;~i;i--)b[i]=min(b[i+1],a[i]);
        for(int i=0;i<n;i++)ans+=a[i]>b[i];
        cout<<ans<<'\n';
    }
}
```

### C. Book Reading  
문제를 보고 A4용지에 쓱쓱 수식으로 써보다가 사이클이 있을 것 같아서 그대로 풀었다. 소스 참고  

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll Q,n,m;
int main(){
    cin>>Q;
    while(Q--){
        cin>>n>>m;
        ll t=n/m,ans=0,tenpack=0;
        for(int i=1;i<10;i++)tenpack+=(i*m)%10;
        for(int i=1;i<=t%10;i++)ans+=(i*m)%10;
        ans+=tenpack*(t/10);
        cout<<ans<<"\n";
    }
}
```

### D. Equalizing by Division  
어차피 어렵지도 않았던 거 Easy는 별로 중요하지 않고 Hard 기준으로 풀었었다.  

대회 때 `while(l<=M)`부분을 `while(r<=M)`이라고 써놔서 틀렸다. 에디토리얼 풀이는 뭔가 다른데 이미 풀었으니 굳이 읽어보고 싶지는 않다.  

```cpp
#include<bits/stdc++.h>
using namespace std;
const int MAX=2e5+5;
int n,k,t,cnt[MAX],M,m=1e9,pSum_[MAX];
inline int pSum(int x){
    return x<=M?pSum_[x]:pSum_[M];
}
void solve(int x){
    int ret=0,cost=0,st=0,l=x,r=x;
    while(l<=M){
        t=pSum(r)-pSum(l-1);
        if(ret+t>=k){
            m=min(m,cost+(k-ret)*st);
            return;
        }
        ret+=t;
        cost+=t*st;
        l<<=1;r=(r<<1)+1;st++;
    }
    if(ret>=k)m=min(m,cost);
    return;
}
int main(){
//  freopen("test.in", "r", stdin);
    ios_base::sync_with_stdio(0);cin.tie(0);
    cin>>n>>k;
    for(int i=0;i<n;i++){
        cin>>t;
        M=max(M,t);
        cnt[t]++;
        if(cnt[t]>=k){cout<<0;return 0;}
    }
    for(int i=1;i<=M;i++)pSum_[i]=pSum_[i-1]+cnt[i];
    for(int i=1;i<=M;i++)solve(i);
    cout<<m<<endl;
}
```

### E. Two Small Strings   
1. 길이 3짜리 사이클 반복  
2. a,b,c 순서 섞은 다음 각각 n개씩 반복 (aabbcc, bbccaa 같이)  

2개의 케이스만 따지면 풀린다.   

```cpp
#include <bits/stdc++.h>
using namespace std;
 
int n,a[3],ban[3][3];
string s,t;
int main()
{
    cin>>n>>s>>t;
    ban[s[0]-'a'][s[1]-'a']=1;
    ban[t[0]-'a'][t[1]-'a']=1;
    a[0]=0;a[1]=1;a[2]=2;
    do{
        bool flag=0;
        for(int i=0;i<3-(n==1);i++){
            if(ban[a[i]][a[(i+1)%3]]){flag=1;break;}
        }
        if(flag)continue;
        cout<<"YES\n";
        while(n--){
            for(int i=0;i<3;i++)printf("%c",a[i]+'a');
        }
        return 0;
    }while(next_permutation(a,a+3));
    a[0]=0;a[1]=1;a[2]=2;
    do{
        if(ban[a[0]][a[1]]||ban[a[1]][a[2]])continue;
        cout<<"YES\n";
        for(int i=0;i<3;i++){
            for(int j=0;j<n;j++)printf("%c",a[i]+'a');
        }
        return 0;
    }while(next_permutation(a,a+3));
    cout<<"NO";
    return 0;
}
```

### F. Unstable String Sort  
제출자 수가 G보다 적은 것을 보고 문제를 읽지도 않고 걸렀었다.  
어려울 줄 알았는데 쉽다. `lp=max(lp,t.v);` 이거를 `lp=t.v`라 써놓고 40분 동안 고민했지만 혼자 풀긴 했다.

```cpp
#include<bits/stdc++.h>
using namespace std;
const int MAX=2e5+5;
int n,k,p[MAX],q[MAX],rev_q[MAX],lp,cnt,save[MAX],cnt2;
struct itv{
    int u,v;
    itv(int u,int v):u(u),v(v){}
    itv():itv(0,0){}
    bool operator < (const itv& o) const{
        return u^o.u?u>o.u:v<o.v;
    }
};
priority_queue<itv> pq;
int main(){
//  freopen("test.in", "r", stdin);
    ios_base::sync_with_stdio(0);cin.tie(0);
    cin>>n>>k;
    for(int i=0;i<n;i++)cin>>p[i],p[i]--;
    for(int i=0;i<n;i++){
        cin>>q[i],q[i]--;
        rev_q[q[i]]=i;
    }
    for(int i=0;i<n;i++){
        int u=i,v=rev_q[p[i]];
        if(u>v)swap(u,v);
        pq.push({u,v});
    }
    while(!pq.empty()){
        itv t=pq.top();
        while(!pq.empty()&&pq.top().u==t.u)pq.pop();
        if(lp<t.u)cnt++;
        else t.u=lp+1;
        for(int i=t.u;i<=t.v;i++)save[p[i]]=cnt;
        lp=max(lp,t.v);
    }
    if(++cnt<k){cout<<"NO";return 0;}
    cout<<"YES\n";
    for(int i=0;i<n;i++){char c=min(save[i],25)+'a';
        cout<<c;
    }
}
```



### G. Path Queries  
대회 때 딱 보고 정렬 정렬하고 오프라인 쿼리로 처리하는 것까지 감이 오고 시간이 다 되서 대회가 끝났다.  

간선 가중치와 쿼리 가중치를 오름차순 정렬한다. 그리고 컴포넌트들을 Disjoint Set을 이용하여 하나씩 붙여 나가면서 붙기 전 컴포넌트의 사이즈가 s1,s2면 `res+=(s1+s2)*(s1+s2-1)/2-s1*(s1-1)/2-s2*(s2-1)/2`를 해준다.   

문제 참 잘 만든 것 같다.  

```cpp
#include<bits/stdc++.h>
#define x first
#define y second
#define all(x) x.begin(),x.end()
using namespace std;
const int MAX=2e5+5;
struct edge{
    int u,v,w;
    edge(int u,int v,int w):u(u),v(v),w(w){}
    edge():edge(0,0,0){}
    bool operator <(const edge& o) const{
        return w>o.w;
    }
};
typedef pair<int,int> pii;
int n,m,u,v,w,par[MAX],sz[MAX];
long long res,s1,s2,ans[MAX];
vector<pii > q;
priority_queue<edge> pq;
void init(){
    for(int i=1;i<=n;i++)par[i]=i,sz[i]=1;
}
int find(int u){return u==par[u]?u:par[u]=find(par[u]);}
bool merge(int u,int v){
    u=find(u);v=find(v);
    if(u==v)return 0;
    if(sz[u]>sz[v])swap(u,v);
    par[u]=v;
    s1=sz[u];s2=sz[v];
    sz[v]+=sz[u];
    return 1;
}
int main(){
//  freopen("test.in", "r", stdin);
    ios_base::sync_with_stdio(0);cin.tie(0);
    cin>>n>>m;
    init();
    for(int i=1;i<n;i++){
        cin>>u>>v>>w;
        pq.push({u,v,w});
    }
    for(int i=0;i<m;i++){
        cin>>w;
        q.push_back({w,i});
    }
    sort(all(q),[](const pii a,const pii b){return a.x<b.x;});
    for(int i=0;i<m;i++){
        while(!pq.empty()&&pq.top().w<=q[i].x){
            edge e=pq.top();pq.pop();
            e.u=find(e.u);e.v=find(e.v);
            if(merge(e.u,e.v))
                res+=(s1+s2)*(s1+s2-1)/2-s1*(s1-1)/2-s2*(s2-1)/2;
        }
        ans[q[i].y]=res;
    }
    for(int i=0;i<m;i++)cout<<ans[i]<<" ";
}
```

## 완료  

![All Solve](/files/codeforces_582_div3.PNG)
