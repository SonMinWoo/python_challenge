# 0. variable type 

## 1. number
a_number = 3
print(a_number)
print(type(a_number))

## 2. string
a_string = "hi"
print(a_string)
print(type(a_string))

## 3. boolean
a_bool = False #! differnet from "False", 1st character is uppercase
print(a_bool)
print(type(a_bool))

## 4. float
a_float = 3.12
print(a_float)
print(type(a_float))

## 5. None
a_none = None
print(a_none)
print(type(a_none))

### very_long_variable -> snake case

# 1. Sequence type(list / tuple)

## list
days = ["Mon","Tue","Wed","Thur","Fri"]
print(days)
print("Mon" in days)
print(days[1:-2])

## list is mutable sequence
days.append("Sat")
print(days)

## tuple !immutable
days = ("Mon","Tue","Wed","Thur","Fri")
print(type(days))

# 2. Dictionary

minwoo = {
  "name": "Minwoo",
  "age" : 23,
  "korean": True,
  "fav_food": ["Pizza","Soda"]
}
print(minwoo)
minwoo["handsome"] = True
print(minwoo)

#3. Function

## print(), type() -> built-in function (default)
print(len("asdwqdqwdqwe"))
age = "12453"
print(type(age))
n_age = int(age)
print(type(n_age))