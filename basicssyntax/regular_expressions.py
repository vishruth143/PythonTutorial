import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if (x):
  print("YES! We have a match!")

print("x" * 40)

str = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", str)
print(x)

print("x" * 40)

str = "That will be 59 dollars"
#Find all digit characters:
x = re.findall("\d", str)
print(x)

print("x" * 40)

str = "hello world"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", str)
print(x)

print("x" * 40)

str = "hello world"
#Check if the string starts with 'hello':
x = re.findall("^hello", str)
if (x):
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

print("x" * 40)

str = "hello world"
#Check if the string ends with 'world':
x = re.findall("world$", str)
if (x):
  print("Yes, the string ends with 'world'")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "ai" followed by 0 or more "x" characters:
x = re.findall("aix*", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "ai" followed by 1 or more "x" characters:
x = re.findall("aix+", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "a" followed by exactly two "l" characters:
x = re.findall("al{2}", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain"
#Check if the string starts with "The":
x = re.findall("\AThe", str)
print(x)
if (x):
  print("Yes, there is a match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain"
#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

str = "The rain in Spain"

print("x" * 40)

#Check if "ain" is present at the end of a WORD:
x = re.findall(r"ain\b", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain"
#Check if "ain" is present, but NOT at the beginning of a word:
x = re.findall(r"\Bain", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)


str = "The rain in Spain"
#Check if "ain" is present, but NOT at the end of a word:
x = re.findall(r"ain\B", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain"
#Check if the string contains any digits (numbers from 0-9):
x = re.findall("\d", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain"
#Return a match at every no-digit character:
x = re.findall("\D", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain"
#Return a match at every white-space character:
x = re.findall("\s", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain"
#Return a match at every NON white-space character:
x = re.findall("\S", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain"
#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
x = re.findall("\w", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain"
#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
x = re.findall("\W", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain"
#Check if the string ends with "Spain":
x = re.findall("Spain\Z", str)
print(x)
if (x):
  print("Yes, there is a match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain"
#Check if the string has any a, r, or n characters:
x = re.findall("[arn]", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain"
#Check if the string has any characters between a and n:
x = re.findall("[a-n]", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain"
#Check if the string has other characters than a, r, or n:
x = re.findall("[^arn]", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain"
#Check if the string has any 0, 1, 2, or 3 digits:
x = re.findall("[0123]", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "8 times before 11:45 AM"
#Check if the string has any digits:
x = re.findall("[0-9]", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "8 times before 11:45 AM"
#Check if the string has any two-digit numbers, from 00 to 59:
x = re.findall("[0-5][0-9]", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "8 times before 11:45 AM"
#Check if the string has any characters from a to z lower case, and A to Z upper case:
x = re.findall("[a-zA-Z]", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "8 times before 11:45 AM"
#Check if the string has any + characters:
x = re.findall("[+]", str)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("x" * 40)

str = "The rain in Spain"
x = re.findall("ai", str)
print(x)

print("x" * 40)

str = "The rain in Spain"
x = re.search("\s", str)
print("The first white-space character is located in position:", x.start())

print("x" * 40)

str = "The rain in Spain"
x = re.search("Portugal", str)
print(x)

print("x" * 40)

str = "The rain in Spain"
x = re.split("\s", str)
print(x)

print("x" * 40)

str = "The rain in Spain"
x = re.split("\s", str, 1)
print(x)
x = re.split("\s", str, 1)
print(x)

print("x" * 40)

str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)

print("x" * 40)

str = "The rain in Spain"
x = re.sub("\s", "9", str, 2)
print(x)

print("x" * 40)

str = "The rain in Spain"
x = re.search("ai", str)
print(x) #this will print an object

print("x" * 40)

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())

print("x" * 40)

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.string)

print("x" * 40)

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.group())