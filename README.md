# python_challenge
nomad coder python challenge!

## day 1
1. Variable (type : integer, string, boolean, float, nonetype)
2. Sequence type (mutable sequence : list "[]", immutable sequence : tuple "()")
    mutable -> 수정 가능. immutable ->  수정 불가
3. Dictionary ("{'key' : value}")
4. Function (Built-in Functions -> len, type, int...)

## day 2
1. Python function
    * indentation
    * return
    * positional argument
    * keyword argument

2. list and function
  list는 function의 argument로 넘긴 후 함수 내부에서 값을 변경하면 외부에 있는 list에도 적용된다.

  **외부 함수에 영향을 미치지 않기 위한 방법**
  
    1. 직접 function에서 새로운 list를 만들어 argument list의 값을 집어넣기
    2. import copy를 한 후 copy.deepcopy를 통해 argument list를 새로운 list에 깊은 복사

## day 3
1. if, elif, else를 이용한 조건문 생성(indentation으로 내용이 구성됨)
2. Function(arg1 = "abc", arg2=None) 등으로 기본 값을 주어 오류 방지 가능
3. type(arg1) == int(,str,float 등) 으로 인자 type check 
4. 단, None은 if(arg1 == None) 등으로 check해야함 (none은 type()함수 쓰지 않아도 됨)
5. print(f"abcd{arg1}") 과 같은 형태로 변수 출력하면 편하다.
