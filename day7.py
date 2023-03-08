#create empty set
st = set()

#create set with initial values
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#get set's length
print(len(it_companies))
#checking an item

#Adding items to set

it_companies.add('Twitter')
print(it_companies)

#Add multiple items to set

sister_companies =['meta', 'capone']
it_companies.update(sister_companies)
print(it_companies)
#removing an item from a set

it_companies.remove('meta')



#clearing items in a set


#converting set to list

#joining sets

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)
print(C)


#intersection items(returns the item from both sets)
inter = A.intersection(B)
print(inter)

#subset and superset
sub = A.issubset(B)
sup = A.issuperset(B)
#difference between two sets

#symmetric difference

sym = A.symmetric_difference(B)
print(sym)

#joining sets

dis = A.isdisjoint(B)
print(dis)


#deleting a set

del it_companies



age = [22, 19, 24, 25, 26, 24, 25, 24]
updateset = set(age)
print(updateset)
print(len(age) >= len(updateset))

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.



