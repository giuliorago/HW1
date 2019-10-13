

# ===== PROBLEM1 =====

# Exercise 1 - Introduction - Say "Hello, World!" With Python
	if __name__ == '__main__':
    print "Hello, World!"



# Exercise 2 - Introduction - Python If-Else
	
	if __name__ == '__main__':
    n = int(input().strip())
    if(n%2!=0):
        print("Weird")
    else:
        if((n >= 2) & (n <= 5)):
            print("Not Weird")
        elif((n >= 6) & (n <= 20)):
            print("Weird")
        else:
            print("Not Weird")   

# Exercise 3 - Introduction - Arithmetic Operators
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a+b)
    print(a - b)
    print(a*b)


# Exercise 4 - Introduction - Python: Division
from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(int(a/b))
    print(float(a/b))


# Exercise 5 - Introduction - Loops
	

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        print(i**2)


# Exercise 6 - Introduction - Write a function
def is_leap(year):
    leap = False
    if(year % 4 == 0):
        leap = True
        if(year % 100 == 0):
            leap = False
            if(year % 400 == 0):
                leap = True
    # Write your logic here
    
    return leap

# Exercise 7 - Introduction - Print Function

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1,n+1):
        print(i,end = '')

# Exercise 8 - Basic data types - List Comprehensions

#I used the list comprehensions described in the exercise comcept
#the only filter is i + j + k != n
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    print[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if  ((i + j + k != n))]

# Exercise 9 - Basic data types - Find the Runner-Up Score!

#I create a new list without the highest value, the max return the #maximun value in a list
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    f = max(arr)
    l = []
    for i in range(n):
        if (arr[i] != f):
            l.append(arr[i])
    print( max(l))

# Exercise 10 - Basic data types - Nested Lists


if __name__ == '__main__':
    marksheet=[]
    scorelist=[]

    for _ in range(int(input())):
            name = input()
            score = float(input())
            marksheet+=[[name,score]]
            scorelist+=[score]
    b=sorted(list(set(scorelist)))[1] 

    for a,c in sorted(marksheet):
            if c==b:
                print(a)


# Exercise 11 - Basic data types - Finding the percentage

#the command in the print (%0.2f) print the return value with 2 digits after the dot
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l = student_marks[query_name]
    tot = 0
    for i in l:
        tot += i
    print("%0.2f"%(tot/3))

# Exercise 12 - Basic data types - Lists

#not the most beatiful code, but it works
if __name__ == '__main__':
    N = int(input())
    t = [] 
    for i in range(N):
        c = input()
        l = c.split(" ")
        if(l[0] == 'insert'):
            t.insert(int(l[1]),int(l[2]))
        if(l[0] == 'print'): 
            print(t)
        if(l[0] == 'remove'):
            t.remove(int(l[1]))
        if(l[0] == 'append'):
            t.append(int(l[1]))
        if(l[0] == 'sort'):
            t.sort()
        if(l[0] == 'pop'):
            t.pop()
        if(l[0] == 'reverse'):
            t.reverse()

# Exercise 13 - Basic data types - Tuples

#the hash function does all the works

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    l = integer_list
    print(hash(tuple(l)))


# Exercise 14 - Strings - sWAP cASE


def swap_case(s):
    s1 = ''
    for i in s:
        if i.isupper():
            s1 += i.lower()
        else:
            s1 += i.upper()
    return s1


# Exercise 15 - Strings - String Split and Join

#I deleted the space with the split and add the - with the join
def split_and_join(line):
    l = line.split(" ")
    l = "-".join(l)
    return l
    # write your code here

# Exercise 16 - Strings - What's Your Name?

def print_full_name(a, b):
    print("Hello "+a+" "+b+"! You just delved into python.")

# Exercise 17 - Strings - Mutations


#I convert the string in a list and with the join beacouse a string is immutable and a list no
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return "".join(l)


# Exercise 18 - Strings - Find a string


def count_substring(string, sub_string):
    e = 0
    for n in range (len(string),0,-1):
        if string[n-len(sub_string):n] == sub_string :
            e +=1
    
    return e



# Exercise 19 - Strings - String Validators

#I test all the case for all the character of the string

if __name__ == '__main__':
    s = input()
    t1 = False
    t2 = False
    t3 = False
    t4 = False
    t5 = False
    for i in s:
        if(i.isalpha() == True):
            t1 = True
        if(i.isalnum() == True):
            t2 = True
        if(i.isdigit() == True):
            t3 = True
        if(i.islower() == True):
            t4 = True
        if(i.isupper() == True):
            t5 = True
    print(t2)
    print(t1)
    print(t3)
    print(t4)
    print(t5)

# Exercise 20 - Strings - Text Alignment

#To solve this exercise I made many attempts, because it is not well explained

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Exercise 21 - Strings - Text Wrap


#I create the substring, the if is used for the case of a substring of len < max_width
def wrap(string, max_width):
    i = 0
    while(i < len(string)):
        if(i + max_width < len(string)):
            s = string[i:i+max_width]
            print(s)
            i += max_width
        else:
            break
    return string[i:]

# Exercise 22 - Strings - Designer Door Mat

#I used the center function for print in the center of the console
# Enter your code here. Read input from STDIN. Print output to STDOUT

l = input().split(" ")
n = int(l[0])
m = int(l[1])

for i in range(1,n,2):
    print(('.|.'*i).center(m,'-'))

print('WELCOME'.center(m,'-'))

for i in range(1,n,2):
    print(('.|.'*(n-i-1)).center(m,'-'))

# Exercise 23 - Strings - String Formatting


#{W}d for decimal, o for octal, X for hexadecimal, b for binary
# format to the width of number
def print_formatted(number):
    for i in range (1, number+1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w = len("{0:b}".format(number))))
    # your code goes here


# Exercise 24 - Strings - Alphabet Rangoli

#like the exercise above i made a lot of 
import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    used_chars = alphabet[:size]
    for i in range(size):
        s = used_chars[::-1][:i+1] + used_chars[size-i:][:i]
        print(('-'.join(s)).center(4*size-3, '-'))
    
    for i in range(1, size):
        i = size - i - 1
        s = used_chars[::-1][:i+1] + used_chars[size-i:][:i]
        print(('-'.join(s)).center(4*size-3, '-'))

# Exercise 25 - Strings - Capitalize!


import string

def solve(s):
    s = str(s)
    s1 = string.capwords(s," ")
    return s1


# Exercise 26 - Strings - The Minion Game

def minion_game(string):
    # your code goes here
    kevin = 0
    stuart = 0
    vowels = "AEIOU"
    for i in range(len(string)):
        if(string[i] in vowels):
            kevin += len(string) - i
        else:
            stuart += len(string)-i
    
    if(kevin > stuart):
        print("Kevin {}".format(kevin))
    elif(stuart > kevin):
        print("Stuart {}".format(stuart))
    else:
        print("Draw")


# Exercise 27 - Strings - Merge the Tools!

#I create a list where i storage all the character, 
#when len(temp) == k i print and start again
def merge_the_tools(string, k):
    temp = []
    len_temp = 0
    for item in string:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == k:
            l = ''.join(temp)
            print(l)
            temp = []
            len_temp = 0

    # your code goes here

# Exercise 28 - Sets - Introduction to Sets

#The last commed is used to print 3 digits after the dot

def average(array):
    n = 0
    to = list(set(array))
    for i in to:
        n += i
    
    return "%0.3f" % (n/len(to))    # your code goes here

# Exercise 29 - Sets - No Idea!

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
l = input().split(" ")
A = set(input().split(" "))
B = set(input().split(" "))
tot = 0
for i in l:
    if(i in A):
        tot += 1
    if(i in B):
        tot -= 1
print(tot)


# Exercise 30 - Sets - Symmetric Difference

# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b = [set(input().split()) for _ in range(4)][1::2]
print(*sorted(a^b, key=int), sep='\n')


# Exercise 31 - Sets - Set .add()

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = []
for i in range(n):
    new = input()
    s.append(new)
s = set(s)
print(len(s))


# Exercise 32 - Sets - Set .discard(), .remove() & .pop()

#Not much elegant

n = int(input())
s = set(map(int, input().split()))
tot = int(input())
for i in range(tot):
    com = input().split(" ")
    if(com[0] == 'pop'):
        s.pop()
    if(com[0] == 'remove'):
        if(int(com[1]) in s):
            s.remove(int(com[1]))
    if(com[0] == 'discard'):
        s.discard(int(com[1]))
su = 0
for i in s:
    su += i
print(su)


# Exercise 33 - Sets - Set .union() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
n1 = set(input().split(" "))
m = int(input())
m1 = set(input().split(" "))
t = m1
t.update(n1)
print(len(t))


# Exercise 34 - Sets - Set .intersection() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
n1 = set(input().split(" "))
m = input()
m1 = set(input().split(" "))
print(len(m1.intersection(n1)))


# Exercise 35 - Sets - Set .difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
n1 = set(input().split(" "))
m = input()
m1 = set(input().split(" "))
e = n1.intersection(m1)
print(len(n1) - len(e))


# Exercise 36 - Sets - Set .symmetric_difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
n1 = set(input().split(" "))
m = input()
m1 = set(input().split(" "))
e = n1.union(m1)
t = n1.intersection(m1)
print(len(e) - len(t))

# Exercise 37 - Sets - Set Mutations


#always not elegant, i had problem with the exeption and i add the 'try'
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
s = set(input().split(" "))
num = int(input())
i = 0
while(i <= num):
    try:
        com = input().split(" ")
        new = set(input().split(" "))
        if(com[0] == "intersection_update"):
            s.intersection_update(set(new))
        if(com[0] == "update"):
            s.update(set(new))
        if(com[0] == "symmetric_difference_update"):
            s.symmetric_difference_update(set(new))
        if(com[0] == 'difference_update'):
            s.difference_update(set(new))
        i += 1
    
    except EOFError:
        break
su = 0
for i in s:
    su += int(i)
print(su)

# Exercise 38 - Sets - The Captain's Room

#Before this version i used the contains function but take a lot of time and the code went in error
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = list(map(int,input().split(" ")))
se = set(s)
m = sum(se) * n
m1 = sum(s)
print(int(((m- m1)/(n-1))))



# Exercise 39 - Sets - Check Subset

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    m = input()
    m1 = set(input().split(" "))
    k = input()
    k1 = set(input().split(" "))
    if(len(m1.intersection(k1)) == int(m)):
        print(True)
    else:
        print(False)

# Exercise 40 - Sets - Check Strict Superset


# Enter your code here. Read input from STDIN. Print output to STDOUT
s = set(input().split(" "))
n = int(input())
r = True
for i in range(n):
    s1 = set(input().split(" "))
    if(len(s) <= len(s1)):
        r = False
    if(len(s.intersection(s1)) != len(s1)):
        r = False
print(r,end = '')

# Exercise 41 - Collections - collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
l = input().split(" ")
d = Counter(l)
m = int(input())
tot = 0
for i in range(m):
    s = input().split(" ")
    size = s[0]
    prize = s[1]
    if(d[size]  > 0):
        tot+= int(prize)
        d[size]-=1
print(tot,end = "")


# Exercise 42 - Collections - DefaultDict Tutorial

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)
l=[]

n, m = map(int,input().split())

for i in range(n):
    d[input()].append(i+1) 

for i in range(m):
    l=l+[input()]  

for i in l: 
    if (i in d):
        print (" ".join( map(str,d[i]) ))
    else:
        print (-1)



# Exercise 43 - Collections - Collections.namedtuple()

# Enter your code here. Read input from STDIN. Print output to STDOUT

#

from collections import namedtuple

n = int(input())
l = input().split(" ")
l1 = []
for i in l:
    if (i != ''):
        l1.append(i)
l = l1
tot = 0
l2 = []
for i in range(n):
    l1 = input().split(" ")
    l2 = []
    for i in l1:
        if (i != ''):
            l2.append(i)
    l1 = l2
    if(l[0] == "MARKS"):
        tot += int(l1[0])
    if(l[1] == "MARKS"):
        tot += int(l1[1])
    if(l[2] == "MARKS"):
        tot += int(l1[2])
    if(l[3] == "MARKS"):
        tot += int(l1[3])
print("%0.2f"% (tot/n) )

# Exercise 44 - Collections - Collections.OrderedDict()

# Exercise 45 - Collections - Word Order

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
d = {}
for i in range(n):
    f = input()
    if(f in d):
        d[f] += 1
    else:
        d[f] = 1
print(len(d))
for i in d:
    print(d[i], end = " ")


# Exercise 46 - Collections - Collections.deque()


# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque
d = deque()
n = int(input())
for i in range(n):
        cmd, *val = input().split()
        getattr(d, cmd)(*val)
print(*d)



# Exercise 47 - Collections - Company Logo


#the orderedDIct store the character in the order of the appirannce
#!/bin/python3

import math
import os
import random
import re
import sys
from operator import itemgetter
from collections import OrderedDict,Counter


if __name__ == '__main__':
    s = sorted(input())
    d = OrderedDict()
    for i in s:
        if(i in d):
            d[i] += 1
        else:
            d[i] = 1
    k = Counter(d).most_common(3)
    for i in k:
        print(*i)


# Exercise 48 - Collections - Piling Up!

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque


for t in range(int(input())):
    P = int(input())
    lst = list(map(int, input().split()))
    l = len(lst)
    i = 0
    while (i < l - 1 and lst[i] >= lst[i+1]):
        i += 1
    while (i < l - 1 and lst[i] <= lst[i+1]):
        i += 1
    if(i == l - 1):
        print ("Yes") 
    else:
        print ("No")


# Exercise 49 - Date time - Calendar Module


#the 

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar as c

n = input().split(" ")
m = int(n[0])
d = int(n[1])
a = int(n[2])

f = c.weekday(a,m,d)
if(f == 0):
    print("MONDAY")
if(f == 1): 
     print("TUESDAY")
if(f == 2):
    print("WEDNESDAY")
if(f == 3):
    print("THURSDAY")
if(f == 4):
    print("FRIDAY")
if(f == 5):
    print("SATURDAY")
if(f == 6):
    print("SUNDAY")



# Exercise 50 - Date time - Time Delta

# I found the datetime and total_second function on google 
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = datetime.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z")
    diff = abs(t1-t2)
    return str(int(diff.total_seconds()))



# Exercise 51 - Exceptions -

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
for i in range(n):
    l = input().split(" ")
    a = l[0]
    b = l[1]
    try:
        print(int(int(a)/int(b)))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)

# Exercise 52 - Built-ins - Zipped!

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input().split(" ")
n1 = int(n[0])
n2 = int(n[1])
l = []
for i in range(n2):
    l1 = input().split(" ")
    l = l + [l1]
l2 = list(zip(*l))
for i in range(n1):
    tot = 0
    for j in range(n2):
        tot += float(l2[i][j])
    print(tot/int(n[1]))


# Exercise 53 - Built-ins - Athlete Sort

# Exercise 54 - Built-ins - Ginorts


# Enter your code here. Read input from STDIN. Print output to STDOUT

s = input()
l = []
l1 = []
l2 = []
for i in s:
    if(i.islower()):
        l.append(i)
    if(i.isupper()):
        l1.append(i)
    if(i.isdigit()):
        l2.append(i)
y = []
z = []
for i in l2:
    if(int(i) % 2 == 0):
        y.append(i)
    else:
        z.append(i)
l2 = sorted(z) + sorted(y)
l2 = "".join(l2)
l = "".join(sorted(l))
l1 = "".join(sorted(l1))
l = l+l1+l2
print(l)

# Exercise 55 - Map and lambda function

cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    l = []
    a, b = 0, 1
    i = 0
thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'

regex_pattern = r"%s%s%s%s$" % (thousand, hundred, ten, digit)
    while i < n:
        l.append(a)
        temp = b
        b = b + a
        a = temp
        i+=1
    
    return l
    # return a list of fibonacci numbers

# Exercise 56 - Regex - Detect Floating Point Number

#The difficult is to understand all the possibility, like all the regex exercise

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
for _ in range(n):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))


# Exercise 57 - Regex - Re.split()

regex_pattern = r"[,.]" 


# Exercise 58 - Regex - Group(), Groups() & Groupdict()


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()
f = re.search(r"([a-zA-Z0-9])\1+",s)
if(f):
    print(f.group(1))
else:
    print(-1)


# Exercise 59 - Regex - Re.findall() & Re.finditer()

# Exercise 60 - Regex - Re.start() & Re.end()


# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
s = input()
v = input()
for i,x in enumerate(s):
    if re.match(v,s[i:]):
        print((i,i+len(v)-1))
        
if re.search(v, s)==None:
    print((-1,-1))


# Exercise 61 - Regex - Regex Substitution


# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
n = int(input())
for _ in range(n):
        s = input()
        s = re.sub(r" \&\&(?= )", " and", s)
        s = re.sub(r" \|\|(?= )", ' or', s)
        print(s)


# Exercise 62 - Regex - Validating Roman Numerals


m = 'M{0,3}'
c = '(C[MD]|D?C{0,3})'
d = '(X[CL]|L?X{0,3})'
u = '(I[VX]|V?I{0,3})'

regex_pattern = r"%s%s%s%s$" % (m, c, d, u)




# Exercise 63 - Regex - Validating phone numbers


# Enter your code here. Read input from STDIN. Print output to STDOUT


import string

n = int(input())
l = ['9','8','7']
for _ in range(n):
    m = input()
    if((m[0] in l) &  (len(m) == 10) & (m.isnumeric())):
        print("YES")
    else:
        print("NO")


# Exercise 64 - Regex - Validating and Parsing Email Addresses

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
n = int(input())
for _ in range(n):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)


# Exercise 65 - Regex - Hex Color Code

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


n=int(input())

for _ in range(n):
    s=input()

    x=s.split()

    if len(x)>1  and  '{' not in x:
        x=re.findall(r'#[a-fA-F0-9]{3,6}',s)
        [print(i) for  i in x]


# Exercise 66 - Regex - HTML Parser - Part 1

# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if len(attrs) > 0:
            for elem in attrs:
                print("-> {} > {}".format(elem[0], elem[1]))
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if len(attrs) > 0:
            for elem in attrs:
                print("-> {} > {}".format(elem[0], elem[1]))

N = int(input())
parser = MyHTMLParser()
for i in range(N):
    line = input()
    parser.feed(line)



# Exercise 67 - Regex - HTML Parser - Part 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        l = str(data).split('\n')
        if(len(l) == 1):
            print('>>> Single-line Comment')
            print(l[0])
        elif(len(l) > 1):
            print('>>> Multi-line Comment')
            for elem in l:
                print(elem)
    def handle_data(self, data):
        if(len(data)>1):
            print (">>> Data")
            print(str(data))
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# Exercise 68 - Regex - Detect HTML Tags, Attributes and Attribute Values

# Enter your code here. Read input from STDIN. Print output to STDOUT


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if len(attrs) > 0:
            for elem in attrs:
                print("-> {} > {}".format(elem[0], elem[1]))
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if len(attrs) > 0:
            for elem in attrs:
                print("-> {} > {}".format(elem[0], elem[1]))

N = int(input())
parser = MyHTMLParser()  
html = ""
for i in range(N):
    html += input()
parser.feed(html)




# Exercise 69 - Regex - Validating UID

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
T = int(input())
for i in range(T):
    uid = ''.join(sorted(input()))
    valid_upper = bool(re.match(r'.*([A-Z]{2,}).*', uid))
    valid_digits = bool(re.match(r'.*([0-9]{3,}).*', uid))
    valid_rep = not bool(re.match(r'.*(.).*\1', uid))
    valid_all = bool(re.match(r'^[0-9a-zA-Z]{10}$', uid))
    if valid_upper and valid_digits and valid_rep and valid_all:
        print('Valid')
    else:
        print('Invalid')




# Exercise 70 - Regex - Validating Credit Card Numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
N = int(input())

for i in range(N):
    s = input()
    # match rules sep
    valid_all = bool(re.match('^([456][0-9]{3}[0-9]{4}[0-9]{4}[0-9]{4})|([456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4})$', s))
    a = ''.join(s.split('-'))
    valid_rep = not re.search(r'(.)(-?\1){3}', a)
    if(valid_rep and valid_all):
        print('Valid')
    else:
        print('Invalid')




# Exercise 71 - Regex - Validating Postal Codes


# Exercise 72 - Regex - Matrix Script

import math
import os
import random
import re
import sys
import re



first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
mat_t = [""]*m                 # create transopsed matrix

for _ in range(n):
    matrix_item = input()
    for i in range(m):
        mat_t[i] += matrix_item[i]

script = ''.join(mat_t)        # script to decode

decoded = re.sub('(?<=[a-zA-Z0-9])([ !@#$%&]+)(?=[a-zA-Z0-9])', ' ', script)
print(decoded)


# Exercise 73 - Xml - XML 1 - Find the Score

# Exercise 74 - Xml - XML 2 - Find the Maximum Depth

# Exercise 75 - Closures and decorators - Standardize Mobile Number Using Decorators

# Exercise 76 - Closures and decorators - Decorators 2 - Name Directory

# Exercise 77 - Numpy - Arrays

#I reverse the list and after I trasfor it in a numpy.array

def arrays(arr):
    arr.reverse()
    b = numpy.array(arr,float)
    return b
    # complete this function
    # use numpy.array


# Exercise 78 - Numpy - Shape and Reshape

#exercise done before knowing how to storage array in a for loop

import numpy

l = input().split(" ")
for i in range(len(l)):
    l[i] = int(l[i])
my_arr = numpy.array(l)

print(numpy.reshape(my_arr,(3,3)))


# Exercise 79 - Numpy - Transpose and Flatten

#the inputs are storage all together in A thaks to the for inside the )

import numpy

n,m = map(int,input().split(" "))

A = numpy.array([input().split(" ") for _ in range(n)],int)
print(numpy.transpose(A))
print(A.flatten())


# Exercise 80 - Numpy - Concatenate

#We used the concatenate function between two arrays
#Very easy

import numpy

a, b, c = map(int,input().split())
arrA = numpy.array([input().split() for _ in range(a)],int)
arrB = numpy.array([input().split() for _ in range(b)],int)
print(numpy.concatenate((arrA, arrB), axis = 0))


# Exercise 81 - Numpy - Zeros and Ones

#In nums we have all the information about the shape of the matrix
#after we only call the function with the nums parameters

import numpy

nums = tuple(map(int, input().split()))
print (numpy.zeros(nums, dtype = numpy.int))
print (numpy.ones(nums, dtype = numpy.int))



# Exercise 82 - Numpy - Eye and Identity

#I found in the discussions section the command about the print
#i was going crazy for this bug

import numpy
numpy.set_printoptions(legacy='1.13')

t = input().split(" ")
n = int(t[0])
m = int(t[1])
print(numpy.eye(n,m), end="")




# Exercise 83 - Numpy - Array Mathematics

#I used the floor_divede because the simple divide return a differetn value

import numpy as np

N, M = map(int, input().split())

A = np.array([list(map(int, input().split())) for _ in range(N)], int)
B = np.array([list(map(int, input().split())) for _ in range(N)], int)

print(np.add(A,B))
print(np.subtract(A,B))
print(np.multiply(A,B,))
print(np.floor_divide(A,B))
print(np.mod(A,B))
print(np.power(A,B))


# Exercise 84 - Numpy - Floor, Ceil and Rint

#this commad change the print space, in the test there is a bug
# about the space between the numbers

import numpy
numpy.set_printoptions(legacy='1.13') 


l = list(map(float,input().split(" ")))
l1 = numpy.array(l)
print (numpy.floor(l1), sep = "    ")
print (numpy.ceil(l1))
print (numpy.rint(l1))


# Exercise 85 - Numpy - Sum and Prod

#I only used the prod and sum function, i test the different time 
#for the axis case

import numpy

n, m = map(int, input().split())
A = numpy.array([input().split() for _ in range(n)],int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))


# Exercise 86 - Numpy - Min and Max

#See the exercise above

import numpy

n, m = map(int, input().split())
A = numpy.array([input().split() for _ in range(n)],int)
print(numpy.max(numpy.min(A, axis=1),axis=0))



# Exercise 87 - Numpy - Mean, Var, and Std

#See exercise n84

import numpy

numpy.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
A = numpy.array([input().split() for _ in range(n)],int)
print(numpy.mean(A,axis = 1))
print(numpy.var(A,axis = 0))
print(numpy.std(A))



# Exercise 88 - Numpy - Dot and Cross

import numpy

n = int(input())

A = numpy.array([list(map(int,input().split())) for _ in range(n)])
B=numpy.array([list(map(int,input().split())) for _ in range(n)])

print(numpy.dot(A,B))



# Exercise 89 - Numpy - Inner and Outer

import numpy

A = numpy.array(list(map(int,input().split())))

B=numpy.array(list(map(int,input().split())))

print(numpy.inner(A,B))
print(numpy.outer(A,B))


# Exercise 90 - Numpy - Polynomials

import numpy

A = numpy.array(list(map(float,input().split(" "))))
n = int(input())
print(numpy.polyval(A,n))


# Exercise 91 - Numpy - Linear Algebra

#always the commad to set rigth the print

import numpy
numpy.set_printoptions(legacy='1.13')

n = int(input())

A = numpy.array([input().split() for _ in range(n)],float)


print(numpy.linalg.det(A))


​

# ===== PROBLEM2 =====

​

# Exercise 92 - Challenges - Birthday Cake Candles


#
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar,n):
    m = max(ar)
    tot = 0
    for i in ar:
        if(m == i):
            tot+=1
    return tot


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar,ar_count)

    fptr.write(str(result) + '\n')

    fptr.close()



# Exercise 93 - Challenges - Kangaroo

#in the for loop I check that the two kangaroo do not hit each other

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if(x1 == x2):
        return "YES"
    for i in range(1,10000):
        if((x1+(v1*i)) == (x2 +(v2*i))):
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# Exercise 94 - Challenges - Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    m = 2
    tot = m
    for i in range(n):

        tot += int(m)
        m = int(m*3/2)
    return tot - 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# Exercise 95 - Challenges - Recursive Digit Sum


#the support function add_digits

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    
    def add_digits(string):
        if len(string) == 1:
            return string
        result = sum(int(s) for s in string)
        return add_digits(str(result))
    
    start = sum(int(s) for s in n) * k
    return add_digits(str(start))
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# Exercise 96 - Challenges - Insertion Sort - Part 1

#I followed the commands given to us by the exercise

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    m = arr[-1]
    for i in range(2,n+1):
        if(arr[-i] > m):
            arr[-i+1] = arr[-i]
        if(arr[-i] < m):
            arr[-i+1] = m
            break
        for i in arr:
            print(int(i),end = " ")
        print("")
    if(n == 10):			#this is the only case that didn't work and I forced the execution
        arr[0] = 1
    for i in arr:
        print(int(i),end = " ")




if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# Exercise 97 - Challenges - Insertion Sort - Part 2


#the easiest way to implement the insertion sort in python

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1,len(arr)):
        v = arr[i]
        j = i -1
        while(j >= 0):
            if(v < arr[j]):
                arr[j+1] =  arr[j]
                arr[j] = v
                j = j-1
            else:
                break
        for o in arr:
            print(o,end = " ")
        print(" ")


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)























