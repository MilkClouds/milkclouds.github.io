---
layout: post
title: '파이썬 함수 학습'
author: yooshini
comments: true
date: 2019-01-18 10:18
tags: [python, basic]

---


# 파이썬 기초학습
## 요약
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