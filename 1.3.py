from collections import Counter

#задача 1
'''
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
b = []
for a in students:
    b.append(a['first_name'])
count = Counter(b)

x=count['Вася']
y=count['Петя']
z=count['Маша']

print(f'Вася: {x}')
print(f'Петя: {y}')
print(f'Маша: {z}')
'''
#Задача 2

'''
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
a=[]
for b in students:
    a.append(b['first_name'])      

import collections

counter = collections.Counter(a)
common = counter.most_common()[0]

print(f'Самое частое имя среди учеников {common}')
'''

#Задача 3

'''
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

first=[]
for a in school_students[0]:
    first.append(a['first_name']) 
print(first)

second=[]
for a in school_students[1]:
    second.append(a['first_name']) 
print(second)

import collections

counter = collections.Counter(first)
common = counter.most_common()[0]

counter1 = collections.Counter(second)
common1 = counter1.most_common()[0]

print(f'Самое частое имя среди учеников 1-го класса: {common[0]}')
print(f'Самое частое имя среди учеников 2-го класса: {common1[0]}')
'''
#Задача 4

'''
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

first=[]
for a in school[0]['students']:
    first.append(a['first_name']) 
#print(first)

second=[]
for a in school[1]['students']:
    second.append(a['first_name']) 
#print(second)

girls=0
boys=0
for a in first:
    #print(a)  
    if a in is_male:
        if is_male[a] == False:
            girls += 1
        elif is_male[a] == True:
            boys += 1 

#print(girls, boys)            

girls1=0
boys1=0
for a in second:
    #print(a)  
    if a in is_male:
        if is_male[a] == False:
            girls1 += 1
        elif is_male[a] == True:
            boys1 += 1 

#print(girls1, boys1)

print(f'в классе 2а {girls} девочки и {boys} мальчика')
print(f'в классе 3с {girls1} девочки и {boys1} мальчика')
'''



school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

first=[]
for a in school[0]['students']:
    first.append(a['first_name']) 
#print(first)

second=[]
for a in school[1]['students']:
    second.append(a['first_name']) 
#print(second)

girls=0
boys=0
for a in first:
    #print(a)  
    if a in is_male:
        if is_male[a] == False:
            girls += 1
        elif is_male[a] == True:
            boys += 1 

#print(girls, boys)            

girls1=0
boys1=0
for a in second:
    #print(a)  
    if a in is_male:
        if is_male[a] == False:
            girls1 += 1
        elif is_male[a] == True:
            boys1 += 1 

#print(girls1, boys1)

if boys > boys1:
    print('в 2а классе больше мальчиков')
elif boys < boys1:
    print('в 3c классе больше мальчиков')
else:
    print('В разных классах мальчиков одинаковое колличество')

if girls > girls1:
    print('в 2а классе больше девочек')
elif girls < girls1:
    print('в 3c классе больше девочек')
else:
    print('В разных классах девочек одинаковое колличество')
