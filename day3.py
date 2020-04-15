# Function and Condition

## Code Challenge (calculator)
def except_not_num(x, y=1):
  if(type(x)==int or type(x)==float):
    if(type(y)==int or type(y)==float):
      return False
    else:
      return True
  else:
    print("Don't input number which is not integer or float!")
    print(f"Invalid values are changed to integer type ({type(x)},{type(y)})")
    return True

def plus(x, y):
  if except_not_num(x, y):
    return int(x)+int(y)
  return x+y

def minus(x, y):
  if except_not_num(x, y):
    return int(x)-int(y)
  return x-y

def product(x, y):
  if except_not_num(x, y):
    return int(x)*int(y)
  return x*y

def divide(x, y):
  if except_not_num(x, y):
    return int(x)/int(y)
  return x/y

def remainder(x, y):
  if except_not_num(x, y):
    return int(x)%int(y)
  return x%y

def negation(x):
  if except_not_num(x):
    return -int(x)
  return -1*x

def power(x, y):
  if except_not_num(x, y):
    return int(x)**int(y)
  return x**y

print(plus(1.7,2))
print(minus(3,5))
print(product(2.2,"4"))
print(divide(7,3))
print(remainder(11,4))
print(negation(3))
print(power(3,6))
print(product(4,"6"))
print(remainder("12","5"))
print(negation("7"))

print("====================")

## Conditional part

### type check
def check_plus(a, b):
  if type(b) is int or type(b) is float:
    return a+b
  else:
    None


### if,elif,else
def age_check(age):
  print(f"you are {age}")
  if age < 18:
    print("you cant drink")
  elif age == 18:
    print("you are new to this!")
  elif age > 20 and age < 25:
    print("you are still kind of young!")
  else :
    print("enjoy your drink")

age_check(22)