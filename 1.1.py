from collections import Counter

print('Задача 1 :')

word = 'Архангельск'
print(word[-1])

print('---------------------------')
print('Задача 2 :')

word = 'Архангельск'.lower()
count = Counter(word)
print(count['а'])

print('---------------------------')
print('Задача 3 :')

word = input('Введите город: ').lower()
text = ['а','е','и', 'о', 'у', 'ы', 'э', 'ю', 'я']
a=0
for word1 in word:
    if word1 in text:
        a = a + 1
print(a)

print('---------------------------')
print('Задача 4 :')

sentence = 'Мы приехали в гости'.split()
print(len(sentence))

sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])

print('---------------------------')
print('Задача 5 :')
   
a=0
sentence = 'Мы приехали в гости'
for word in sentence.split():
    a += len(word)
print(a)

c=a/len(sentence.split())
print(c)








