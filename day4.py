# Loop and Module

## for (when for is started, x and qwer is made)
print("=====================")

days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for x in days:
  if x is "Wed":
    break
  else:
    print(x)

for qwer in [1,3,5,6]:
  print(qwer)

for q in "minwoo":
  print(q)

print("=====================")

## Default Module

### import math (total import)
### partial import
from math import ceil, fabs
### import and making name
from math import fsum as sexy_sum

print(ceil(1.2))
print(fabs(-2.4))
print(sexy_sum([1,2,3,4,6,7,8]))

###import from another file
from day4_module import plus, minus
print(plus(2,7))
print(minus(7,5))

print("=====================")

## Web Scrapper

### Requests (package)
import requests

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

print(indeed_result) #status code
print(indeed_result.text) #html code

### Beautifulsoup4
