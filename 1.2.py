# Задача 1
'''
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    #print(name)
'''  
# Задача 2
'''  
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    #print(f'{name}, Колличество букв в имени: {len(name)}')
'''
# Задача 3
'''
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
'''
'''
#Задача 4


groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'] 
]

for a in groups:
    print(f'В группе {len(a)} ученика')

#print(f'Всего групп: {len(groups)}')
#print (f'В группе {len(groups[0])} Ученика')
#print (f'В группе {len(groups[1])} Ученика')

'''

#Задача 5

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша']
  
]

b=0
for a in groups:    
    a = ', '.join(a)
    b +=1
    print(f'Класс {b}: {a}')
    
    
