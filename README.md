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

## day 4
1. for를 통한 loop (for variable in list/tuple/stirng...)
2. import로 module 전체 import, from module import function으로 부분 import
3. from module import function as nickname으로 이름 붙여주기
4. requests를 import하고 requests.get(url)을 변수에 담으면 status code 출력됨
5. 4번에서 담은 변수에 .text를 통해 html 코드 전체를 볼 수 있음

## day 5
1. bs4를 이용한 html 파싱 (requests.get(URL),  BeautifulSoup(result.text, "html.parser"), result.find("div", {"class":"pagination"})) ...
2. .find_all('a')로 특정 class에 속한 모든 link를 다 받아올 수 있음
3. link를 이동하면서 URL에 나타나는 query의 특징을 보고 requests.get(f"{URL}&start={page*LIMIT}")과 같이 해당 page가 존재하는지 check

## day 6
1. x = html.find("div", {"class":"recJobLoc"})는 해당 class의 div를 찾아 x에 할당해주는 것과 같음(bs4를 사용 가능!)
2. bs4에서 find는 맨 앞의 하나만, find_all은 모두 찾아 리스트화
3. ["data-rc-loc"]와 같은 지시자는 해당 html 객체에서 data-rc-loc과 같은 속성값을 가진 값을 반환하라는 것
4. company.string같이 .string으로 객체 내부의 값을 얻을 수 있음 