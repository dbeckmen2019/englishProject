from collections import Counter

'''Drew Beckmen
   English Creative Project
   Dr. Cottingham, Magical Realism(Block 6)

   Apply computer science and data analysis to investigate the style of the
   author and how that style differs among the three different narrators in
   the novel Extremely Loud and Incredibly Close'''


#-----------------ANALYSIS OF TEXT AS A WHOLE-----------------------------------
f = open('Extremely Loud And Incredibly Close -Jonathan Safran_djvu.txt', 'r')
fileLines = f.read().lower()
frequency = {}
entireFrequency = {}

s = open('1-1000.txt', 'r')
readLines = s.readlines()

animals = open('Animal-words.txt', 'r')
animalList = animals.readlines()

#Get rid of newline
for i in range(len(readLines)):
    readLines[i] = readLines[i].strip('\n')

for i in range(len(animalList)):
    animalList[i] = animalList[i].strip('\n').lower()

for word in fileLines.split():
    if word not in readLines:
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1

for word in fileLines.split():
    if word not in entireFrequency:
        entireFrequency[word] = 1
    else:
        entireFrequency[word] += 1

#Get the top 5 most used words outside of the 250 most commonly used words
top5 = dict(Counter(frequency).most_common(25))
print(top5)

#Find the frequency of each of these words in the entire novel
print("Number of times extremely is said: {}".format(entireFrequency["extremely"]))
print("Number of times incredibly is said: {}".format(entireFrequency["incredibly"]))
print("Number of times close is said: {}".format(entireFrequency["close"] + entireFrequency["closely"]))
print("Number of times loud is said: {}".format(entireFrequency["loud"] + entireFrequency["loudly"]))




#Look for colors in the book
colors = [" blue ", " red ", " orange ", " yellow ", " green ", " white ", " brown ", " purple ", " violet "]
timesMentioned = 0
for key in colors:
    timesMentioned += fileLines.count(key)
    print("Number of times {} is said: {}".format(key, fileLines.count(key)))

print("Colors are brought up {} times.".format(timesMentioned))

#Look for animals in the book
animalsMentioned = 0;
animalsMentioned += entireFrequency["animal"]
for animal in animalList:
    if animal in frequency:
        animalsMentioned += entireFrequency[animal]

print("Animals are brought up {} times".format(animalsMentioned))


def testFloat(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

numbers = 0
for key in entireFrequency:
    if testFloat(key):
        numbers += 1

print("Numbers are brought up {} times".format(numbers))

f.close()
s.close()


#-------------------------------------------------------------------------------


#-------------------------ANALYZE OSKAR'S NARRATION-----------------------------
oskar = open('Oskar.txt', 'r')
stringOskar = oskar.read().lower()
print("Oskar's Commas: {}".format(stringOskar.count(',')))
print("Oskar's Questions: {}".format(stringOskar.count('?')))
print("Number of times he says What about: {}".format(stringOskar.count("what about")))
print("Bruises: {}".format(stringOskar.count("bruise")))
print("Boots: {}".format(stringOskar.count("boots")))

#Find the average sentence length
sentences = stringOskar.split('.')
averageLength = sum(len(x.split()) for x in sentences) / len(sentences)
print("Average sentence length for Oskar: {}".format(averageLength))

oskar.close()


#-------------------------ANALYZE GRANDMA'S NARRATION-----------------------------
grandma = open('Grandma.txt', 'r')
stringGrandma = grandma.read()
print("Grandma's Commas: ")
print(stringGrandma.count(','))
print("Grandma's Questions: ")
print(stringGrandma.count('?'))

#Find the average sentence length
sentences = stringGrandma.split('.')
averageLength = sum(len(x.split()) for x in sentences) / len(sentences)
print(averageLength)

grandma.close()

#-------------------------ANALYZE GRANDPA'S NARRATION-----------------------------
grandpa = open('Grandpa.txt', 'r')
stringGrandpa = grandpa.read()
print("Grandpa's Commas: ")
print(stringGrandpa.count(','))
print("Grandpa's Questions: ")
print(stringGrandpa.count('?'))

#Find the average sentence length
sentences = stringGrandpa.split('.')
averageLength = sum(len(x.split()) for x in sentences) / len(sentences)
print(averageLength)

grandpa.close()
