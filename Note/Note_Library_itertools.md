라이브러리 노트
==========
# [ itertools ]
파이썬 공식 문서 : [Python - itertools](https://docs.python.org/3/library/itertools.html, "python docs - itertools")

### 1. combinations (조합)
#### (1) 내용
- iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다.
- combinations는 클래스이므로, 객체 초기화 이후에 그대로 사용할 땐 리스트 자료형으로 변환한다.
#### (2) 형태
- combinations(iterable, r)
#### (3) 예제
- 리스트에서 원소 개수가 2개인 조합 뽑기, 반환값을 리스트로 변환 후 출력
  ```python
  from itertools import combinations

  data = ['A', 'B', 'C']
  result = list(combinations(data, 2))

  print(result)

  # 출력 결과
  '''
  [('A', 'B'), ('A', 'C'), ('B', 'C')]
  '''
  ```
- 문자열에서 원소 개수가 2개인 조합 뽑기, 반환값을 차례로 출력
  ```python
  from itertools import combinations

  data = "ABC"

  for i in combinations(data, 2):
    print(i)

  # 출력 결과
  '''
  ('A', 'B')
  ('A', 'C')
  ('B', 'C')
  '''
  ```

### 2. combinations_with_replacement (중복조합)
#### (1) 내용
- iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다.
- 원소를 중복해서 뽑는다.
- combinations_with_replacement는 클래스이므로, 객체 초기화 이후에 그대로 사용할 땐 리스트 자료형으로 변환한다.
#### (2) 형태
- combinations_with_replacement(iterable, r)
#### (3) 예제
- 리스트에서 원소 개수가 2개인 조합 뽑기, 중복 가능, 반환값을 리스트로 변환 후 출력
  ```python
  from itertools import combinations_with_replacement
  
  data = ['A', 'B', 'C']
  result = list(combinations_with_replacement(data, 2))

  print(result)
  
  # 출력 결과
  '''
  [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
  '''
  ```
- 문자열에서 원소 개수가 2개인 조합 뽑기, 중복 가능, 반환값을 차례로 출력
  ```python
  from itertools import combinations_with_replacement
  
  data = "ABC"
  
  for i in combinations_with_replacement(data, 2):
    print(i)

  print(result)
  
  # 출력 결과
  '''
  ('A', 'A')
  ('A', 'B')
  ('A', 'C')
  ('B', 'B')
  ('B', 'C')
  ('C', 'C')
  '''
  ```

### 3. permutations (순열)
#### (1) 내용
- iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산한다.
- permutations는 클래스이므로, 객체 초기화 이후에 그대로 사용할 땐 리스트 자료형으로 변환한다.
#### (2) 형태
- permutations(iterable,r=None)
- r을 지정하지 않거나 r=None으로 하면 최대 길이의 순열이 반환된다.
#### (3) 예제
- 리스트에서 원소를 3개 뽑아 순서대로 줄세우기, 반환값을 리스트로 변환 후 출력
  ```python  
  from itertools import permutations
  
  data = ['A', 'B', 'C']
  result = list(permutations(data, 3))

  print(result)
  
  # 출력 결과
  '''
  [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
  '''
  ```
- 문자열에서 원소를 최대로 뽑아 순서대로 줄세우기, 반환값을 차례로 출력
  ```python
  from itertools import permutations

  data = "ABC"

  for i in permutations(data):
    print(i)

  # 출력결과
  '''
  ('A', 'B', 'C')
  ('A', 'C', 'B')
  ('B', 'A', 'C')
  ('B', 'C', 'A')
  ('C', 'A', 'B')
  ('C', 'B', 'A')
  '''
  ```

### 4. product (중복순열)
#### (1) 내용
- iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산한다.
- 원소를 중복해서 뽑는다.
- 중첩된 for문과 구조가 동일하다.
- product는 클래스이므로, 객체 초기화 이후에 그대로 사용할 땐 리스트 자료형으로 변환한다.
#### (2) 형태
- product(*iterables, repeat=1)
- iterable 객체를 1개, repeat=2 이상으로 입력하면 중복순열로 활용할 수 있다.
- iterable 객체를 2개 이상, repeat=1 이상으로 입력하면 여러 iterable 객체를 짝지어 나열할 수 있다.
#### (3) 예제
- 리스트에서 원소를 2개 뽑아 순서대로 줄세우기, 중복 가능, 반환값을 리스트로 변환 후 출력
  ```python
  from itertools import product

  data = ['A', 'B', 'C']
  result = list(product(data, repeat=2))

  print(result)
  
  # 출력 결과
  '''
  [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
  '''
  ```
- 문자열에서 원소를 3개 뽑아 순서대로 줄세우기, 중복 가능, 반환값을 차례로 출력
  ```python
  from itertools import product
  
  data = "AB"
  
  for i in product(data, repeat=3): # product(data, data, data, repeat=1)과 동일한 출력
    print(i)

  # 출력 결과
  '''
  ('A', 'A', 'A')
  ('A', 'A', 'B')
  ('A', 'B', 'A')
  ('A', 'B', 'B')
  ('B', 'A', 'A')
  ('B', 'A', 'B')
  ('B', 'B', 'A')
  ('B', 'B', 'B')
  '''
  ```
- 2개의 리스트에서 원소를 1개씩 뽑아 순서대로 줄세우기 (데카르트곱)
  ```python
  from itertools import product

  data1 = ['A', 'B']
  data2 = ['1', '2']

  for i in product(data1, data2, repeat=1): # data1과 data2의 모든 쌍을 지어 반환
    print(i)

  # 출력 결과
  '''
  ('A', '1')
  ('A', '2')
  ('B', '1')
  ('B', '2')
  '''
  ```
