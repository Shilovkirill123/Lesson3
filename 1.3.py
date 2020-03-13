from collections import Counter

import collections

print('Задача 1 :')

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
b = []
for a in students:
    b.append(a['first_name'])
count = Counter(b)

for name in count:
    print(f'{name}: {count[name]}')



print('---------------------------')
print('Задача 2 :')


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


counter = collections.Counter(a)
common = counter.most_common()[0][0]

print(f'Самое частое имя среди учеников {common}')


print('---------------------------')
print('Задача 3 :')


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


classes=0
for school in school_students:
    student=[]
    classes += 1
    for a in school:
        student.append(a['first_name'])
        counter = collections.Counter(student)
        common = counter.most_common()[0][0]
    print(f'Самое частое имя среди учеников {classes}-го класса: {common}')
    
'''
'''

print('---------------------------')
print('Задача 4 :')


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


for school in school:
    classes=[]
    for a in school['students']:
        classes.append(a['first_name'])
        girls=0
        boys=0
        for a in classes:  
            if a in is_male:
                if is_male[a] == False:
                    girls += 1
                elif is_male[a] == True:
                    boys += 1 

    print(f'В классе {school["class"]} мальчиков: {boys}, девочек: {girls}')
    
    
    

print('---------------------------')
print('Задача 5 :')


school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]}
 
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

girl = []
boy = []
number = []

for school in school:
    classes=[]
    number.append(school['class'])
    for a in school['students']:
        classes.append(a['first_name'])
        girls=0
        boys=0
        for a in classes:  
            if a in is_male:
                if is_male[a] == False:
                    girls += 1
                elif is_male[a] == True:
                    boys += 1

    girl.append(girls)
    boy.append(boys)


x=-1
for a in number:
    x += 1
    if girl[x] > boy[x]:
      print(f'В классе {number[x]} больше девочек')
    elif girl[x] < boy[x]:
      print(f'В классе {number[x]} больше мальчиков')
    else:
      print(f'в классе{number[x]} мальчиков и девочек одинаково')
