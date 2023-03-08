#empty list
empty_list = []
print(len(empty_list))

fruits = ["banana","apple","lime","coconut"]
print(len(fruits))
print("num of fruits", len(fruits))
lst_mixdata = ["indra", 29, {"last_name":"reddy"}]
print(lst_mixdata)

print(fruits[0])
last_index = len(fruits) -1
last_fruit = fruits[last_index]
print(last_fruit)

print(fruits[-2])
#unpacking list items

unpack = [1,2,3,4,5,6,7,8,9]
first_item, second_item, third_item, *rest, ninth_item = unpack
print(first_item)
print(second_item)
print(rest)
countries = ["india","italy","portugal","germany","aregentina","france","belgium"]
ind,it,po,*scandic,ar = countries
print(ind)
print(scandic)
print(ar)

#modifying lists
fruits[0] = "bell peppers"
print(fruits)

#checking items in list
does_exist = "bell peppers" in fruits
print(does_exist)

#adding items to list
fruits.append("avocado")
print(fruits)

#insret items 
sports = ["handball", "volleyball", "cricket"]
sports.insert(0, "football")
print(sports)
sports.remove("cricket")
print(sports)

sports.pop(1)
print(sports)
del sports [0]
print(sports)
fruits.clear()
print(fruits)

copie = ["i", "am copying this", "list"]
copy_list = copie.copy()
print(copy_list)

#joining lists

list_one = [1,2,3,4,5,6,7,8,9,0]
list_two = [-1,-2,-3,-4,-5]
list_five = [20,30,40]
list_three = list_one + list_two
print(list_three)

list_one.extend(list_two)
print(list_one)
#counting items in a list
courses = ["html", "java","python"]
print(courses.count("p"))
print(courses.count("python"))

#fiding index
print(courses.index("java"))
#reversing a list
courses.reverse()
print(courses)

#sorting list items

months = ["january", "february", "march", "april", "december"]
months.sort()
print(months)
months.sort(reverse=True)
print(months)

ages = [19,22,19,24,20,25,26,24,25,24]
ages.sort()
print(ages)
minimum = min(ages)
print(minimum)
addition = sum(ages)
print(addition)