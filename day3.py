age = 29
height = 5.6
base = int(input('enter the base'))
height = int(input('enter the height'))
area = 0.5 * base * height
print('area of the triangle is' , area)


a = int(input('enter side a:'))
b = int(input('enter side b:'))
c = int(input('enter side c:'))
perimeter = a + b + c
print('perimeter of traingele is',perimeter)

l = int(input('enter the lenght of reactangle'))
w = int(input('enter the width of rectangle'))
area = l * w
print('area of reactangle is ', area)
perimeter = 2 * (l + w)
print('perimeter of rectangle is', perimeter)

for x in range(0,10):
    print(x ** 2 + 6 * x + 9) #doesn't really make sense to me

print(len ('python') != len ('dragon'))

print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'I hope this course is not full of jargon')

print('on' not in 'dragon', 'on' not in 'python')

p = len('python')
p_c = float(p)
print(p_c)

number = int(input('the number is '))
print('even' if number % 2 == 0 else 'odd')

s = 7//3
print(s == int(2.7))

hours = int(input('enter hours'))
rph = int(input('enter rate per hour'))
weekly_earnings = hours * rph
print('weekly earnings are:', weekly_earnings)

for i in range(1, 6):
    print(i, i ** 0, i ** 1, i ** 2, i ** 3)
