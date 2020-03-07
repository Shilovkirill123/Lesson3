from collections import Counter
#word = 'Архангельск'
#print(word[-1])

#word = 'Архангельск'.lower()
#count = Counter(word)
#print(count['а'])

#from collections import Counter

#word = input('Введите город: ').lower()
#text = ['а','е','и', 'о', 'у', 'ы', 'э', 'ю', 'я']
#a=0
#for word1 in word:
   # if word1 in text:
    #    a = a + 1
#print(a)

#sentence = 'Мы приехали в гости'.split()
#print(len(sentence))

#sentence = 'Мы приехали в гости'
#for word in sentence.split():
   # print(word[0])
   
a=0
sentence = 'Мы приехали в гости'
for word in sentence.split():
    a += len(word)
print(a)

c=a/len(sentence.split())
print(c)








