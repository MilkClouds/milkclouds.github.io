---
layout: post
title: 'Google OR-Tools 소개'
author: milkclouds
comments: true
date: 2019-06-03 22:39
tags: []

---


### 개요  
지식인에서 정해진 정점을 무조건 지나는 최단거리 알고리즘에 대한 답변을 했었다. 그러다가 팀프로젝트에서 OR-Tools로 해보려다가 안 되서 찾아보고 있다는 말을 듣고 나도 ortools를 찾아봤는데 찾아보니 꽤 굉장해서 포스트로 남겨두려고 한다.


### OR-Tools  
[Google OR-Tools](https://developers.google.com/optimization/)
구글 OR-Tools는 combinatorial optimization, 조합론적 최적화에 쓰이는 툴이다. Linear Programming(LP), Flow 문제(Max Flow, MCMF), Integer Programming, vehicle rounting(특별한 예로 TSP) 등을 정말 간단한 설정과 입력만으로 풀어준다.  
대부분 최적화 문제에는 objective, 목표와 constraints, 제한 조건이 있다. objective function, 즉 목표 함수와 제한 조건을 적당히 넣어주면 답을 찾아준다.

### Install  
[Pypi ortools](https://pypi.org/project/ortools/)에서 확인할 수 있다. 아래 명령어로 pip을 이용해 간편하게 설치 가능하다.
```
pip install ortools
```

### Examples  
아래는 Linear Programming 모듈, GLOP을 이용해 `0<=x<=1` and `0<=y<=2`에서 `x+y`의 최댓값을 찾아낸다.
constraints는 x,y의 범위이고 목표 함수는 x+y, 최댓값이다.
```python
from __future__ import print_function
from ortools.linear_solver import pywraplp

def main():
  solver = pywraplp.Solver('SolveSimpleSystem',
                           pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
  # Create the variables x and y.
  x = solver.NumVar(0, 1, 'x')
  y = solver.NumVar(0, 2, 'y')
  # Create the objective function, x + y.
  objective = solver.Objective()
  objective.SetCoefficient(x, 1)
  objective.SetCoefficient(y, 1)
  objective.SetMaximization()
  # Call the solver and display the results.
  solver.Solve()
  print('Solution:')
  print('x = ', x.solution_value())
  print('y = ', y.solution_value())

if __name__ == '__main__':
  main()
```

아래 그림을 보자. 3x+4y를 최대화하는 x,y를 찾을 것이고, 제한 조건은 그림과 같다.
![IMG](https://developers.google.com/optimization/images/lp/feasible_region.png)
```python
"""Linear optimization example"""

from __future__ import print_function
from ortools.linear_solver import pywraplp

def main():
  # Instantiate a Glop solver, naming it LinearExample.
  solver = pywraplp.Solver('LinearExample',
                           pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# Create the two variables and let them take on any value.
  x = solver.NumVar(-solver.infinity(), solver.infinity(), 'x')
  y = solver.NumVar(-solver.infinity(), solver.infinity(), 'y')

  # Constraint 1: x + 2y <= 14.
  constraint1 = solver.Constraint(-solver.infinity(), 14)
  constraint1.SetCoefficient(x, 1)
  constraint1.SetCoefficient(y, 2)

  # Constraint 2: 3x - y >= 0.
  constraint2 = solver.Constraint(0, solver.infinity())
  constraint2.SetCoefficient(x, 3)
  constraint2.SetCoefficient(y, -1)

  # Constraint 3: x - y <= 2.
  constraint3 = solver.Constraint(-solver.infinity(), 2)
  constraint3.SetCoefficient(x, 1)
  constraint3.SetCoefficient(y, -1)

  # Objective function: 3x + 4y.
  objective = solver.Objective()
  objective.SetCoefficient(x, 3)
  objective.SetCoefficient(y, 4)
  objective.SetMaximization()

  # Solve the system.
  solver.Solve()
  opt_solution = 3 * x.solution_value() + 4 * y.solution_value()
  print('Number of variables =', solver.NumVariables())
  print('Number of constraints =', solver.NumConstraints())
  # The value of each variable in the solution.
  print('Solution:')
  print('x = ', x.solution_value())
  print('y = ', y.solution_value())
  # The objective value of the solution.
  print('Optimal objective value =', opt_solution)
if __name__ == '__main__':
  main()
```


아래는 Max Flow 예시이다.
```python
"""From Taha 'Introduction to Operations Research', example 6.4-2."""

from __future__ import print_function
from ortools.graph import pywrapgraph

def main():
  """MaxFlow simple interface example."""

  # Define three parallel arrays: start_nodes, end_nodes, and the capacities
  # between each pair. For instance, the arc from node 0 to node 1 has a
  # capacity of 20.

  start_nodes = [0, 0, 0, 1, 1, 2, 2, 3, 3]
  end_nodes = [1, 2, 3, 2, 4, 3, 4, 2, 4]
  capacities = [20, 30, 10, 40, 30, 10, 20, 5, 20]

  # Instantiate a SimpleMaxFlow solver.
  max_flow = pywrapgraph.SimpleMaxFlow()
  # Add each arc.
  for i in range(0, len(start_nodes)):
    max_flow.AddArcWithCapacity(start_nodes[i], end_nodes[i], capacities[i])

  # Find the maximum flow between node 0 and node 4.
  if max_flow.Solve(0, 4) == max_flow.OPTIMAL:
    print('Max flow:', max_flow.OptimalFlow())
    print('')
    print('  Arc    Flow / Capacity')
    for i in range(max_flow.NumArcs()):
      print('%1s -> %1s   %3s  / %3s' % (
          max_flow.Tail(i),
          max_flow.Head(i),
          max_flow.Flow(i),
          max_flow.Capacity(i)))
    print('Source side min-cut:', max_flow.GetSourceSideMinCut())
    print('Sink side min-cut:', max_flow.GetSinkSideMinCut())
  else:
    print('There was an issue with the max flow input.')

if __name__ == '__main__':
  main()
```

### 맺음말  
정말 신기하고 흥미로운데 지금 나한테 딱히 뭔가 구체적으로 쓸 만한 곳은 없는 것 같다. 나중에 유용하게 쓸 지도 모르겠다.