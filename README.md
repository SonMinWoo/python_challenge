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

## day 8
1. csv 포맷으로 저장하기
2. file = open("jobs.csv", mode="w")과 같이 파일 생성. mode에서 "w"옵션은 '파일 새로 쓰기'를 뜻함(초기화)
3. writer = csv.writer(file)로 위 파일에 쓰는 writer 생성
4. writer.writerow(["title", "company", "location", "link"])와 같이 row 단위로 파일에 쓴다.
5. writer.writerow(list(job.values()))와 같이 dictionary 내부 값을 쓸 수 있다. 단, list형식으로 writerow에 값을 줘야 한다.
6. 위에서 Dictionary의 value들은 dictionary.values()와 같이 얻을 수 있다.

## day 9
1. 크롤링 중 get_text()로 조건을 추가할 수 있다.(기존 .string보다 명료한듯) ex) get_text(strip=True)
2. find_all("a",recursive=False)로 계속해서 해당하는 tag들을 찾아 내려가는 것을 방지할 수 있다.
3. .strip("-"), .strip("\n") .strip(" \r") 등으로 불필요한 문자들 제거 가능
4. app = Flask("AppName")과 같이 정의해 flask 객체를 생성하고 app.run()으로 flask 서버 실행
5. @app.route("/")밑에 바로 def funcName(): return "hello"라고 적는 것으로 경로 설정 가능 (@반드시 app.route밑에 function이 와서 해당 경로를 처리해줘야됨)
6. return render_template("index.html")과 같이 templates 파일 내 html파일 보여주기 가능(flask는 무조건 templates 내로 경로를 잡음))
7. render_template("report.html", searchingBy=word)와 같이 python 변수를 html에 제공할 수 있음
8. html파일에선 {{variable}}로 위에서 받은 변수 사용 가능
9. {% for a in list %}와 같이 python 명령어 실행 가능. 단, {% endfor %}과 같이 종료 명시해줘야됨

## day 10
1. {% if var == "abc"%}와 같이 if문도 사용 가능. 단, {% endif %}로 종료해줘야하며, 'is' 가 아닌 ==로 써야 문자열 비교가 먹히는 듯하다.
2. request에는 기본적으로 json 파싱 함수가 있어 requests.get(url).json()으로 Python dictionary화가 가능하다.
3. 입력에 의한 취약점을 막기 위해 {{var|safe}}라는 |safe 필터가 존재한다.

## day 11
1. python dictionary list value 기준 sort : sorted(list명, key=lambda (list 내부 item들의 임시 이름): ((list 내부 item들의 임시 이름)["정렬하고자 하는 dictionary의 key"]), reverse=True(default는 오름차순, reverse=True는 내림차순 정렬))
2. flask request : request.args.to_dict()으로 받은 parameter들을 dict화 시킬 수 있다.
3. dict에서 dict.key()로 dict의 key list를 받을 수 있다.
4. requests에서 header를 추가하여(requests.get(url, headers=header명)) scrapping 차단 사이트를 우회할 수 있다. (ex : reddit -> headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'} 추가)

## day 12
1. @app.route("/add", methods=["post"])와 같이 methods=[]에 request 방식을 지정해 줄 수 있다. (default는 get)
2. request.form["input name"]으로 form 내 input 값들을 받아올 수 있다.
3. flask 패키지 내의 redirect를 import 한 후 redirect("url")로 사용할 수 있다.