
### TEST
```python3
INF=10**9
N=int(input())
dist=[]
for _ in range(N):
    dist.append(list(map(int,input().split())))
for I in range(N):
    for J in range(N):
        if dist[I][J]==0: dist[I][J]=INF
```