import math 

#List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
#Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
#Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
#Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.



print('30 Days of Python Programming')
first_name = 'indra'
last_name = 'kiran'
full_name = first_name + last_name
country = 'india'
age = 29
year = 2023
is_married = False
is_light_on = True
college, course = 'LIU', 'CIS'

print(type(full_name))
print(len(first_name))
print(len(first_name) == len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
remainder = num_two % num_one
exp = num_one**num_two
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)