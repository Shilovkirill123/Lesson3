print('Задача 1 :')

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(name)

print('---------------------------')
print('Задача 2 :')


names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(f'{name}, Колличество букв в имени: {len(name)}')

print('---------------------------')
print('Задача 3 :')


is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

for name in names:
    if name in is_male:
        if is_male[name] == False:
           print(f'{name} Пол ЖЕН')
        else:
            print(f'{name} Пол МУЖ')

print('---------------------------')
print('Задача 4 :')


groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'] 
]

group1 = 0
for group in groups:
    group1 +=1
    print(f'В группе {group1}: {len(group)} ученика')

print(f'Всего групп: {group1}')


print('---------------------------')
print('Задача 5 :')


groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша']
  
]

b=0
for a in groups:    
    a = ', '.join(a)
    b +=1
    print(f'Класс {b}: {a}')
    
    
