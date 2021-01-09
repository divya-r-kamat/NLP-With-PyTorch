# write a python function to check if the user provided string is palindrome or not a palindrome

def ifPalindrome(inVar):
    revInvar = []
    for _ in range((len(inVar)-1), -1, -1):
        revInvar.append(inVar[_])
    if revInvar == inVar:
        return "Palindrome"
    else:
        return "Not a palindrome"

# write a python function to Calculate the date of n days from the given date.

from datetime import datetime, timedelta
def add_days(n, d = datetime.today()):
  return d + timedelta(n)

# write a python function to check if all elements in a list are equal.

def all_equal(lst):
  return len(set(lst)) == 1

# write a python function to check if all elements in a list are unique.

def all_unique(lst):
  return len(lst) == len(set(lst))

# write a python function to find the average of two or more numbers and return the average

def average(*args):
  return sum(args, 0.0) / len(args)

# write a python function to convert a user provided string to camelcase

from re import sub
def camel(s):
  s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
  return ''.join([s[0].lower(), s[1:]])

# write a python function to capitalize the first letter of a string

def capitalize(s, lower_rest = False):
  return ''.join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])

# write a python function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(degrees):
  return ((degrees * 1.8) + 32)

# write a python function to convert a given string into a list of words.

import re
def words(s, pattern = '[a-zA-Z-]+'):
  return re.findall(pattern, s)

# write a python function thats returns a flat list of all the values in a flat dictionary

def values_only(flat_dict):
  return list(flat_dict.values())

# write a python function thats accepts a list and returns most frequent element that appears in a list

def most_frequent(list):
    return max(set(list), key = list.count)

# write a python program to create multiplication table of 5

n=5
for i in range(1,11):
   print(n,'x',i,'=',n*i)

# write a python function to create multiplication table from the user provided number 

def multiplication_table(n):
  for i in range(1,11):
    print(n,'x',i,'=',n*i)

# write a python program to print a dictionary where the keys are numbers between 1 and 10 (both included) and the values are square of keys.

d=dict()
for x in range(1,11):
    d[x]=x**2
print(d)

# write a python program to sort a list of tuples using Lambda.

marks = [('Computer Science', 88), ('Physics', 90), ('Maths', 97), ('Chemistry', 82)]
print("Original list of tuples:")
print(marks)
marks.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(marks)

# write a python function to calculate the median of user provided list of numbers

def median(list):
  list.sort()
  list_length = len(list)
  if list_length % 2 == 0:
    return (list[int(list_length / 2) - 1] + list[int(list_length / 2)]) / 2
  return float(list[int(list_length / 2)])

# write a Python program to calculate simple interest

p = 10000
t = 6
r = 8
si = (p * t * r)/100
print(f'Simple interest is {si}')

# write a python program to check if year is a leap year or not

year = 2004
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(f"{year} is a leap year")
       else:
           print(f"{year} is not a leap year")
   else:
      print(f"{year} is a leap year")
else:
   print(f"{year} is not a leap year")

# Write a python function to check if user provided year is a leap year or not

def is_leap(year):
  if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
  else:
    print(f"{year} is not a leap year")

# Write a python function to check the strength of user provided password

def check_password_strength(password):
  import re 
  flag = 0
  while True:   
      if (len(password)<8): 
          flag = -1
          break
      elif not re.search("[a-z]", password): 
          flag = -1
          break
      elif not re.search("[A-Z]", password): 
          flag = -1
          break
      elif not re.search("[0-9]", password): 
          flag = -1
          break
      elif not re.search("[_@$]", password): 
          flag = -1
          break
      elif re.search("\s", password): 
          flag = -1
          break
      else: 
          flag = 0
          print("Strong Password") 
          break  
  if flag ==-1: 
      print("Weak Password")

# write a python Program to find area of circle 

PI = 3.14
radius = float(6)
area = PI * radius * radius
circumference = 2 * PI * radius
print(f'Area Of a Circle {area}')
print(f'Circumference Of a Circle {circumference}')

# write a python function to find the area of a circle using the user provided radius

def area_of_circle(radius):
  PI = 3.14
  radius = float(radius)
  area = PI * radius * radius
  circumference = 2 * PI * radius
  print(f'Area Of a Circle {area}')
  print(f'Circumference Of a Circle {circumference}')

# write a python function to find the area of a circle using the user provided circumference

def area_of_circle(circumference):
  circumference = float(circumference)
  PI = 3.14
  area = (circumference * circumference)/(4 * PI)
  print(f'Area Of a Circle {area}')

# write a python function to find the area of a circle using the user provided diameter

def area_of_circle(diameter):
  PI = 3.14
  area = (PI/4) * (diameter * diameter)
  print(f'Area Of a Circle {area}')

# write a python function to generate 4 digit OTP

import math, random 
def generateOTP() : 
    digits = "0123456789"
    OTP = "" 
    for i in range(4) : 
        OTP += digits[math.floor(random.random() * 10)] 
    return OTP

# write a python function to generate 6 digit OTP

import math, random 
def generateOTP() :  
    digits = "0123456789"
    OTP = "" 
    for i in range(6) : 
        OTP += digits[math.floor(random.random() * 10)]  
    return OTP

# write a python program to calculate distance between tao points

import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
print(f"The distance between {p1} and {p2} is {distance}")

# write a python function to calculate compound interest

def compound_interest(principle, rate, time): 
    Amount = principle * (pow((1 + rate / 100), time)) 
    CI = Amount - principle 
    print(f"Compound interest is {CI}")

# write a python function to convert hours to minutes

def convert_to_minutes(num_hours):
    minutes = num_hours * 60
    return minutes

# write a python function to convert hours to seconds

def convert_to_seconds(num_hours):
    minutes = num_hours * 60
    seconds = minutes * 60
    return seconds

# write a python function to remove vowels from a string
def vowel_remover(text):
    string = ""
    for l in text:
        if l.lower() != "a" and l.lower() != "e" and l.lower() != "i" and l.lower() != "o" and l.lower() != "u":
            string += l
    return string

# write a python program to print all integers that aren’t divisible by either 2 or 3 and lies between 1 and 50.
for i in range(0,50):
  if((i%2!=0) & (i%3!=0)):
      print(i)

# write a python function to print odd numbers between user provided ranges

def odd_numbers(lower,upper):
  for i in range(lower,upper+1):
    if(i%2!=0):
        print(i)

# write a python program to find sum of natural numbers up to a 16

num = 16
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)

# write a python program to remove punctuations from a string

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "Hello!!!, she said ---and went."
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# write a python function to find the resolution on the user provided image

def jpeg_res(filename):
   with open(filename,'rb') as img_file:
       img_file.seek(163)
       a = img_file.read(2)
       height = (a[0] << 8) + a[1]
       a = img_file.read(2)
       width = (a[0] << 8) + a[1]
   print(f"The resolution of the image is {width}x{height}")

# write a python program to count the number of each vowels in a given text


vowels = 'aeiou'
text = 'Hello, have you tried our tutorial section yet?'
text = text.casefold()
count = {}.fromkeys(vowels,0)
for char in text:
   if char in count:
       count[char] += 1
print(count)

# write a python function to check if a key exists in a dictionary

d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')

# write a python program to check if the list is empty

l = []
if not l:
  print("List is empty")
else:
  print("List is not empty")

# write a python program to convert two lists into dictionary

column_names = ['id', 'color', 'style']
column_values = [1, 'red', 'bold']
name_to_value_dict = dict(zip(column_names, column_values))
name_to_value_dict = {key:value for key, value in zip(column_names, column_values)}
name_value_tuples = zip(column_names, column_values) 
name_to_value_dict = {} 
for key, value in name_value_tuples: 
    if key in name_to_value_dict: 
        pass  
    else: 
        name_to_value_dict[key] = value
print(name_to_value_dict)

# write a python program to get index values for a list in the form of key:value pair using enumerate

my_list = ['a', 'b', 'c', 'd', 'e']
for index, value in enumerate(my_list):
    print('{0}: {1}'.format(index, value))

# write a python program to merge two dictionaries

dict_1 = {'apple': 9, 'banana': 6}
dict_2 = {'banana': 4, 'orange': 8}
combined_dict = {**dict_1, **dict_2}
print(combined_dict)

# write a python function to check if all elements in a list are unique or not

def unique(l):
    if len(l)==len(set(l)):
        print("All elements are unique")
    else:
        print("List has duplicates")

# write a python function to validate the email 

import re 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'      
def check(email):  
    if(re.search(regex,email)):  
        print("Valid Email")         
    else:  
        print("Invalid Email")

# write a python function to calculate the age with the user provided date of birth

from datetime import date
def calculate_age(dtob):
    today = date.today()
    return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))

# write a python function to check if a user provided number is a perfect square.

def is_perfect_square(n):
    x = n // 2
    y = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y: return False
        y.add(x)
    return True

# write a python function that removes element from a list using a user provided number

def drop(a, n = 1):
  return a[n:]

# write a program function to check if given words appear together in a list of sentence

def check(sentence, words): 
    res = [all([k in s for k in words]) for s in sentence] 
    return [sentence[i] for i in range(0, len(res)) if res[i]]

# write a python program  to convert list of tuples into list 

lt = [('English', 2), ('Maths', 4), ('Science', '6')] 
out = [item for t in lt for item in t]  
print(out)

# write a python program to count the number of words in a sentence

test_string = "This is a good book"
res = len(test_string.split()) 
print (f"The number of words in string are :{str(res)}")

# write a python function to count the occurrences of a value in a list.

def count_occurrences(lst, val):
  return lst.count(val)

# write a python function to return the length of user provided string in bytes

def byte_size(s):
  return len(s.encode('utf-8'))

# write a python function to calculate the greatest common divisor (GCD) of two user provided positive integers. 

def gcd(num1, num2):
    gcd = 1  
    if num1 % num2 == 0:
        return num2
    for k in range(int(num2 / 2), 0, -1):
        if num1 % k == 0 and num2 % k == 0:
            gcd = k
            break  
    return gcd

# write a python function to calculate the least common multiple (LCM) of two user provided positive integers.

def lcm(num1, num2):
   if num1 > num2:
       z = num1
   else:
       z = num2
   while(True):
       if((z % num1 == 0) and (z % num2 == 0)):
           lcm = z
           break
       z += 1
   return lcm

# write a python program to split the string into chunks of size 3

str = 'CarBadBoxNumKeyValRayCppSan'
n = 3
chunks = [str[i:i+n] for i in range(0, len(str), n)]
print(chunks)

# write a python function to read first n lines from a file

def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
      for line in islice(f, nlines):
        print(line)

# write a python program to check whether a person is eligible to vote or not

age=23
if age>=18:
        status="Eligible"
else:
    status="Not Eligible"
print("You are ",status," for Vote.")

# write a python program to check if a number is positive, negative or zero.

num = 5
if num > 0:
   print("It is positive number")
elif num == 0:
   print("It is Zero")
else:
   print("It is a negative number")

# write a python program to get numbers divisible by fifteen from a list

num_list = [45, 55, 60, 37, 100, 105, 220]
result = list(filter(lambda x: (x % 15 == 0), num_list))
print(f"Numbers divisible by 15 are {result}")

# write a python function to append text to a user provided file

def file_read(fname):
    with open(fname, "w") as myfile:
      myfile.write("Appending line one\n")
      myfile.write("Appending line two")
      txt = open(fname)
      print(txt.read())

# write a python function to pad a user provided number to specified length

def pad_number(n, l):
  return str(n).zfill(l)

# write a python function to convert a user provided list of dictionaries into a list of values corresponding to the user specified key

def pluck(lst, key):
  return [x.get(key) for x in lst]

# write a python function to convert the values of RGB components to a hexadecimal color code.

def rgb_to_hex(r, g, b):
  return ('{:02X}' * 3).format(r, g, b)

# write a python function to reverse a user provided list or string

def reverse(itr):
  return itr[::-1]

# write a python function to convert an angle from radians to degrees.

def rads_to_degrees(rad):
  return (rad * 180.0) / 3.14

# write a python function that returns a list of elements that exist in both user provided lists.

def similarity(a, b):
  return [item for item in a if item in b]

# write a python function that converts a user provided string to snake case

from re import sub
def snake(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()

# write a python function that sorts a list based on the user provided list of indexes.

def sort_by_indexes(lst, indexes, reverse=False):
  return [val for (_, val) in sorted(zip(indexes, lst), key=lambda x: \
          x[0], reverse=reverse)]

# write a python function to sort the dictionary by key

def sort_dict_by_key(d, reverse = False):
  return dict(sorted(d.items(), reverse = reverse))

# write a python function to sort the dictionary by values

def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

# write a python function to capitalize first letter of a string

def capitalize(s, lower_rest = False):
  return ''.join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])

# write a python function that chunks a list into smaller lists of a specified size

from math import ceil
def chunk(lst, size):
  return list(
    map(lambda x: lst[x * size:x * size + size],
      list(range(ceil(len(lst) / size)))))

# write a python function to calculate a sigmoid value for any user provided real numbers

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

# write a python program to count the number of lines in a text file

!touch abc.txt
file = open("abc.txt","r") 
Counter = 0
Content = file.read() 
CoList = Content.split("\n")  
for i in CoList: 
    if i: 
        Counter += 1          
print(f"There are {Counter} number of lines in the file")

# write a python program to count the number of lower case in a string

string="This is a very good place to Visit"
count=0
for i in string:
      if(i.islower()):
            count=count+1
print(f"The number of lowercase characters is:{count}")

# write a python program to find the sequences of one upper case letter followed by lower case letters.


import re
text="Albert"
patterns = '[A-Z]+[a-z]+$'
if re.search(patterns, text):
  print('Found a match!')
else:
  print('Not matched!')

# write a python program to find the number of files in a directory

import os
dir='.'
list = os.listdir(dir) 
number_files = len(list)
print(f'There are {number_files} file in the directory')

# write a python function to clamp a number within a user specified range

def clamp_number(num, a, b):
  return max(min(num, max(a, b)), min(a, b))

# write a python function that returns every nth element in a list

def every_nth(lst, nth):
  return lst[nth - 1::nth]

# write a python function that returns first element of a list

def head(lst):
  return lst[0]

# write a python function to check if two lists contains same elements regardless of order

def have_same_contents(a, b):
  for v in set(a + b):
    if a.count(v) != b.count(v):
      return False
  return True

# write a python function to rotate the given list by n times toward left 

def rotate(lst, offset):
  return lst[offset:] + lst[:offset]

# write a python function to transpose a user provided two dimensional list

def transpose(lst):
  return list(zip(*lst))

# write a python function to convert a user provided date to iso representation

from datetime import datetime
def to_iso_date(d):
  return d.isoformat()

# write a python function to convert an integer to its roman numeral representation

def to_roman_numeral(num):
  lookup = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
  ]
  res = ''
  for (n, roman) in lookup:
    (d, num) = divmod(num, n)
    res += roman * d
  return res

# write a python function that returns binary representation of given number

def to_binary(n):
  return bin(n)

# write a python function to calculate weighted average of two or more numbers

def weighted_average(nums, weights):
  return sum(x * y for x, y in zip(nums, weights)) / sum(weights)

# write a python program to filter out non-empty rows of a matrix


test_list = [[4, 5, 6, 7], [], [], [9, 8, 1], []] 
print(f"The original list is :{test_list} ") 
res = [row for row in test_list if len(row) > 0]
print(f"Filtered Matrix {res}")

# write a python program to print prime factors of user provided number

import math 
def primeFactors(n): 
	while n % 2 == 0: 
		print(2), 
		n = n / 2
	for i in range(3,int(math.sqrt(n))+1,2): 
		while n % i== 0: 
			print(i), 
			n = n / i 
	if n > 2: 
		print(n)

# write a python function to return sum of the powers between two numbers

def sum_of_powers(end, power = 2, start = 1):
  return sum([(i) ** power for i in range(start, end + 1)])

# write a python function to implement odd-even sort

def oddEvenSort(arr, n): 
	isSorted = 0
	while isSorted == 0: 
		isSorted = 1
		temp = 0
		for i in range(1, n-1, 2): 
			if arr[i] > arr[i+1]: 
				arr[i], arr[i+1] = arr[i+1], arr[i] 
				isSorted = 0
		for i in range(0, n-1, 2): 
			if arr[i] > arr[i+1]: 
				arr[i], arr[i+1] = arr[i+1], arr[i] 
				isSorted = 0	
	return

# write a python program to find the smallest multiple of the first n numbers. 

def smallest_multiple(n):
    if (n<=2):
      return n
    i = n * 2
    factors = [number  for number in range(n, 1, -1) if number * 2 > n]
    print(factors)
    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i

# write a python program to generate random float numbers in a specific numerical range.

import random
for x in range(6):
    print('{:04.3f}'.format(random.uniform(x, 100)), end=' ')

# write a python program to drop microseconds from datetime.

import datetime
dt = datetime.datetime.today().replace(microsecond=0)
dt

# write a python program to convert unix timestamp string to readable date.

import datetime
unix_timestamp="1284105682"
print(
    datetime.datetime.fromtimestamp(
        int(unix_timestamp)
    ).strftime('%Y-%m-%d %H:%M:%S')
)

# write a python program to add two matrices


X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
for r in result:
   print(r)

# write a python program to multiply two matrices


X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
for r in result:
   print(r)

# write a python function to calculate the day difference between two user provided dates

def days_diff(start, end):
  return (end - start).days

# write a python function to decapitalize the first letter of user provided string.

def decapitalize(s, upper_rest = False):
  return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])

# write a python program to reverse user provided number 

n = 4562; 
rev = 0
while(n > 0): 
    a = n % 10
    rev = rev * 10 + a 
    n = n // 10   
print(rev)

