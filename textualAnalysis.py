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

for word in fileLines.split():
    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word] += 1

#Find the frequency of each of these words in the entire novel
print("Number of times extremely is said: {}".format(frequency["extremely"]))
print("Number of times incredibly is said: {}".format(frequency["incredibly"]))
print("Number of times close is said: {}".format(frequency["close"] + frequency["closely"]))
print("Number of times loud is said: {}".format(frequency["loud"] + frequency["loudly"]))

#Other things to look for -->

f.close()
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
