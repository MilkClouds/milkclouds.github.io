
### TEST
```python3
import sys;input=sys.stdin.readline;sys.setrecursionlimit(999999)
M,N=map(int,input().split())
adj=[]
for _ in range(M):
	adj.append(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
visit=[[False]*N for _ in range(M)]
def dfs(x,y):
	if visit[x][y]:return 0
	if x==M-1: return 1
	visit[x][y]=1
	for k in range(4):
		nx=x+dx[k]
		ny=y+dy[k]
		if 0<=nx<M and 0<=ny<N and adj[nx][ny]=='0':
			if dfs(nx,ny):
				return 1
	return 0
for i in range(N):
	if adj[0][i]=='0':
		if dfs(0,i):
			print("YES")
			break
else:
	print("NO")
```