---
layout: post
title: '파이썬 함수 학습'
author: yooshini
comments: true
date: 2019-01-18 22:18
tags: [python, basic]

---


# 파이썬 기초학습 함수


## 요약
파이썬이 실행되는 원리, 함수, 재귀함수에 대해 배웠다.

## 내용
- 파이썬 실행 구조는 인터프리터이다. 소스 수정이 간편하지만, 실행 속도가 느리다는 단점이 있다.

- 함수
	- 반환 값이 없는 함수
	- 인자가 없는 함수
	- 인자, 반환 값이 있는 함수
	반환 키워드는 `return`이라 한다.


```python
def add(a, b):
    if a < b:
        return b
    else:
        return a
   
print(add(5,6))
```

- 재귀 함수
	- 함수 중에, 자기 자신을 호출하는 함수를 통틀어 재귀 함수라 한다.
	- for-loop보다 가독성이 좋고 구조가 명확하게 짤 수 있는 경우가 많다.
	- 파이썬에서, RecursionError으로 무한 루프를 방지해준다.

```python
def factorial(n):
	if n==1:return 1
	return factorial(n-1)*n

print(factorial(5))
```


#### 강의자 MilkClouds 각주
귀찮다.
