from collections import Counter

f = open('Extremely Loud And Incredibly Close -Jonathan Safran_djvu.txt', 'r')

fileLines = f.read().lower()

frequency = {}

for word in fileLines.split():
    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word] += 1

#print(dict(Counter(frequency).most_common(200)))

print(frequency["extremely"])
print(frequency["incredibly"])
print(frequency["close"] + frequency["closely"])
print(frequency["loud"] + frequency["loudly"])


f.close()

oskar = open('Oskar.txt', 'r')
stringOskar = oskar.read().lower()
print("Oskar's Commas: ")
print(stringOskar.count(','))
print("Oskar's Questions: ")
print(stringOskar.count('?'))
print(stringOskar.count("what about"))
print("Bruises: ")
print(stringOskar.count("bruise"))
print("Boots: ")
print(stringOskar.count("boots"))

sentences = stringOskar.split('.')
averageLength = sum(len(x.split()) for x in sentences) / len(sentences)
print(averageLength)

oskar.close()

grandma = open('Grandma.txt', 'r')
stringGrandma = grandma.read()
print("Grandma's Commas: ")
print(stringGrandma.count(','))
print("Grandma's Questions: ")
print(stringGrandma.count('?'))


sentences = stringGrandma.split('.')
averageLength = sum(len(x.split()) for x in sentences) / len(sentences)
print(averageLength)

grandma.close()

grandpa = open('Grandpa.txt', 'r')
stringGrandpa = grandpa.read()
print("Grandpa's Commas: ")
print(stringGrandpa.count(','))
print("Grandpa's Questions: ")
print(stringGrandpa.count('?'))

sentences = stringGrandpa.split('.')
averageLength = sum(len(x.split()) for x in sentences) / len(sentences)
print(averageLength)

grandpa.close()
