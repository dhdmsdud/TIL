# 변수

> variable



### 숫자

- x=1, y=2, z=3
  - 더하기, 빼기, 곱하기, 제곱, mod(z를 y로 나눠서 남은 값)

```python
print(x+y)
print(z-x)
print(x*z)
print(z**y)
print(z%y)
```

### 문자열

- ", ' 둘중 무엇을 써도 출력 가능
- 줄이 넘어가는 문자열을 출력할땐 """<쓰고싶은문장>"""
- **숫자와 문자를 같이 출력할땐 서로 같은 모양으로 만들어줘야 가능**!!

```python
x=4 / y="4"
print(srt(x)+y)
print(x+int(y)
```

### Boolean

- true / flase 구분
- `if`로 시작	
  - if not, else, elif, and(모두 true), or(하나라도 true)

```python
x=3
if x>5:
    print("hello")
elif x==3:
    print("hola")
    else:
    print("hi")
```

### 함수(function)

- 반복되는 코드를 그룹화

- `def 그룹명 ():`

  ```python
  def dsum(a,b):
      result=a+b
      return result
  ```

- 함수 마지막은`return result`로 끝냄