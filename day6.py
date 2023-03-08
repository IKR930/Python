first = tuple()
print(len(first))
tup_brothers = ("indra","kiran","rishi")
tup_sisters = ("vidya","sneha","sri")
tup_siblings = tup_brothers + tup_sisters
print(tup_siblings)
print(len(tup_siblings))
tup_modify = list(tup_siblings)
print(tup_modify)
tup_modify[0] = "krishna"
tup_modify[1] = "amaravathi"
print(tup_modify)
tup_modify = tuple(tup_modify)
print(tup_modify)
siblings = tup_modify[2:]
print(siblings)
parents = tup_modify[0:2]
print(parents)

fruits = ("apple", "banana","orange","avocado")
vegetables = ("spinach", "lettuce", "brinjal")
animal_products = ("milk", "chicken","eggs")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
food_stuff_tp = list(food_stuff_tp)
print(food_stuff_tp)
slicing = food_stuff_tp[5:6]
print(slicing)
particular_slicing = food_stuff_tp[3:8]
print(particular_slicing)
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

does_exist = "estonia" in nordic_countries
print(does_exist)
print("Iceland" in nordic_countries)