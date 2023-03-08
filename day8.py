#A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type
dog = {}
dog = {
    'color': 'black',
    'breed':'husky',
    'legs': 4,
    'age': 20,

}
#creating a Dictionary
student_dict = {
    'first_name': 'indra',
    'last_name' : 'kiran',
    'gender' : 'male',
    'age': 29,
    'marital_status' : 'single',
    'skills' : ['python', 'java','html', 'devops'],
    'address' : {
        'city' : 'austin',
        'country' : 'USA',
        'address': "milliner loop"
    }
}


#Dictionary Length
print(len(student_dict))
#Accessing Dictionary items
print(student_dict['first_name'])
#Accessing through "get" method
student_dict.get('skills')
print(type('skills'))

#Adding items to dictionary
student_dict['skills'].append('AWS')
print(student_dict)
#Modifying items in a DICT


#checking keys in DICT
keys = student_dict.keys()
print(keys)

values = student_dict.values()
print(values)

#removing key and value pairs from DICT

#changing a DICT to list of items()
item = student_dict.items()
print(item)

#deleting a dict

student_dict.pop('address')
print(student_dict)

del student_dict
#copying a dictionary

#Getting DICT keys as a list

#GETTING DICT values as List

