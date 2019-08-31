---
layout: post
title: 'Codeforces Round #582 (Div. 3)'
author: milkclouds
comments: true
date: 2019-08-31 22:13
tags: [problem-solving]

---

## Codeforces Round #582 (Div.3)  

23:35에 대회 시작  
23:40에 A 제출, AC  
23:47에 B 제출, AC  
23:54에 C 제출, AC   
그 후 D 여러번 해보다 대체 왜 안되지??? 하다가 멘붕오고 E도 좀 보다가 실패  


대회 끝나고 D에 한 줄 바꾸고 제출했더니 D1,D2 전부 AC  
E는 문제 접근 잘 해놓고 경우 분류 잘못해서 실패하고 대회 끝나고 좀 고쳐서 AC  


D,E 맞추면 민트 끝, 어쩌면 블루로 갈 수 있었지 않았을까?;;; 완전히 삽질했다..

### A. Chips Moving  
별 거 없다. 그냥 칩을 `i->j`로 이동하는 비용이 `abs(i-j)&1`인데 모든 칩을 하나의 위치로 이동하는 데 드는 최소 비용을 구하라는 거다. 입력도 작으니까 주어진 모든 임의의 칩에 대해 그 칩의 위치로 칩을 모았을때 드는 총 비용을 구하고 그 중 최솟값을 구하면 된다. `O(n^2)`  

난 이렇게 뇌없이 대강 풀고 넘겼는데 홀수 칩 개수를 odd라고 하면 답은 `min(odd,n-odd)`다. `O(n)`

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

하하 대회 때 `while(l<=M)`부분을 `while(r<=M)`이라고 써놔서 틀렸다. 시간 복잡도는 `O(nlogn)`로 예상했고 한 줄 고치니 예상대로 하드 버전까지 바로 풀렸다. `solve(x)`는 x가 커질수록 시행횟수도 작아지니 `O(nlogn)` 중에서도 빠를 것 같다. 대회 에디토리얼에서는 뭔가 다르게 풀어뒀는데 어차피 어떻게 풀어도 풀리는 문제를 내가 삽질한거라...

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
2개의 케이스만 따지면 풀린다. 에디토리얼을 보니 "해보니까 위 2개 케이스로 전부 커버가 되더라"식으로 적혀있어서 저게 뭔 에디토리얼인가 싶긴 한데 아무튼 이걸 눈치채고도 2번 케이스를 2개 문자열 s,t에 같은 문자가 같은 위치에 나올 때만 적용시켜서 틀렸다. 예를 들면 s=ab, t=ac나 s=ba, t=ca 같은 때만.. 그거 말고도 뭔가 세부 구현 잘못했던 게 있는 것 같긴 하다. 대회 끝나고 새로 제출할 때 전부 갈아엎고 제출해서 모르겠지만.  

뭐 그래도 D번보다는 억울하진 않다. 애초에 D번에서 멘붕오고 시간 부족했었어서..

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
제출자 수가 G보다 적은 것을 보고 문제를 읽지도 않고 걸렀었다. 하하..
어려울 줄 알았는데 쉽다. 에디토리얼 안 보고 풀었다. `lp=max(lp,t.v);` 이거를 `lp=t.v`라 써놓고 40분 동안 혼자 고민했지만 혼자 풀긴 했다.

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
대회 때 딱 보고 정렬 정렬하고 오프라인 쿼리로 처리하는 것까지 감이 왔다. 그리고 대회가 끝났다.  

... 어쨌든 대회 끝나고 보니 G번치고 어렵지 않은건지 Div3가 원래 쉬운건지 모르겠지만, 간선 가중치와 쿼리 가중치를 오름차순 정렬한다. 그리고 컴포넌트들을 Disjoint Set을 이용하여 하나씩 붙여 나가면서 붙기 전 컴포넌트의 사이즈가 s1,s2면 `res+=(s1+s2)*(s1+s2-1)/2-s1*(s1-1)/2-s2*(s2-1)/2`를 해준다.  

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

## 와 다풀었다  

![All Solve](/files/codeforces_582_div3.PNG)


## 후기  
A,B,C는 말할 것도 없고 D,E는 D에서 삽질만 안했으면 대회 시간 내에도 풀 수 있었고 F,G는 혼자 풀 수는 있는데 대회 시간 내에 못 푸는 정도인 것 같다. (F는 에디토리얼 안 보고 풀었고 G는 보고 풀었다. G는 안 보고도 풀 수 있었을 것 같은데 보고 푼 게 좀 아쉽다.)
F,G는 2시간 가지고는 어쩔 수 없다 쳐도 D,E는 진짜 아쉽다. 언젠가 Div3 정도는 다 맞출 수 있겠지..