# Python function
## python function use indentation(tab)
## function body is structed by tab
def say_hello():
  print("hello")
  print("bye")

say_hello()

print()

## function argument
def say_hello(who):
  print("hello", who)
say_hello("Minwoo")

## argument default value
def plus(a, b=0):
  print(a + b)
plus(2,5)
plus(3)

print()

## function return
def p_minus(a, b):
  print(a - b)

def r_minus(a, b):
  return a - b
  print("qwer", True) #it is not excuted

p_result = p_minus(5, 3)
r_result = r_minus(5, 3)

print(p_result, r_result)

print()

## Positional Argument / Keyword Argument
def say_bye(a, b):
  return f"{a}: bye to {b}"
### positional 
print(say_bye("minwoo", "abc"))
### keyword
print(say_bye(b="minwoo",a="abc"))