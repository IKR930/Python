#concatenation
first_name = "Indra"
last_name = "Kiran"
full_name = first_name + last_name
print(full_name)

#Escape Sequence of a string
print("I hope i can keep up with python. \nwill you?")
print("day1\tTopics\tlearned")
print("day2\t6\t7")
print("I really hope this course will \"help me\"")

#string format(str.format)

college = "longislanduni"
year = 2018
grade = "A+"
academics = "I studied in {} in {} acquired a grade of {}" .format(college,year,grade)
print(academics)

c = 5
d = 10
print("{} + {} = {}".format(c,d,c+d))

radius = 3
pi = 3.14
area = pi*radius**2
formatted_string = "Area of circle with a radius {} is {:.2f}".format(radius,area)
print(formatted_string)

#string interpolation lets you injects the data if it starts with f

x = 8
y = 9
print(f"{x} + {y} = {x+y}")
print(f"{x} / {y} = {x/y :.2f}")

#Accessing characters in string

language = "python"
first_letter = language[0]
print(first_letter)
last_index = len(language) -1
last_letter = language[last_index]
print(last_letter)

#negative indexing

course = "Pyspark"
last_letter = course[-1]
print(last_letter)

#slicing of strings

company = "capitalone"
first_three = company[0:3]
print(first_three)
last_three = company[7:10]
print(last_three)
#otherway
last_three = company[-3:]
print(last_three)

#reversing a string
greetings = "Hello"
print(greetings[::-1])

#slicing of strings (did not get the full understanding)
breaking = "wearesplittingthis"
first_split = breaking[0:5:6]
print(first_split)

#string methods

challenge = "thirty days of python"
print(challenge.capitalize())

challenge = "thirty days of python"
print(challenge.count("y"))

challenge = "thirty days of python"
print(challenge.endswith("n"))

challenge = "thirty \tdays \tof \tpython"
print(challenge.expandtabs(10))

challenge = "thirty days of python"
print(challenge.find("ay"))

challenge = "thirty days of python"
print(challenge.rfind("on"))

name = "indra"
city = "austin"
age = 29
info = "I am {} I am {} living in {}".format(name,age,city)
print(info)


hours = int(input("number of hours"))
rate = int(input("rate per hour"))
pay = hours*rate
print("your pay is:" , pay)