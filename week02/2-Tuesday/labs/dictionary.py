# 1. Create a dictionary called zodiac with the following inforation.
# Each key is the name of the zodiac

#myZodiac = {

#'Aries - The Warrior'
#'Taurus - The Builder'
#'Gemini - The Messenger'
#'Cancer - The Mother'
#'Leo - The King'
#'Virgo -The Analyst'
#'Libra - The Judge'
#'Scorpio - The Magician'
#'Sagittarius - the Gypsy'
#'Capricorn - the Father'
#'Pisces - TheMystic'
#}

#name = myZodiac['Taurus']

#print(myZodiac)




# 1a. Retrieve information about your zodiac from the zodiac dictionary


# 2. Given the following dictionary

#phonebook_dict = {
#    'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#    'Elizabeth': '484-584-2923'
#}


#phonebook_dict["Kareem"] = "938-489-1234"
# 2a. Print Elizabeth's phone number
# 2b. Add a entry to the dictionary: Kareem's number is 938-489-1234.
# 2c. Delete Alice's phone entry.
# 2d. Change Bob's phone number to '968-345-2345'.
# 2e. Print all the phone entries.


# 3. Nested dictionaries

#ramit = {
#    'name': 'Ramit',
#    'email': 'ramit@gmail.com',
#    'interests': ['movies', 'tennis'],
#    'friends': [
#        {
#            'name': 'Jasmine',
#            'email': 'jasmine@yahoo.com',
#            'interests': ['photography', 'tennis']
#        },
#        {
#            'name': 'Jan',
#            'email': 'jan@hotmail.com',
#            'interests': ['movies', 'tv']
#        }
#    ]
#}
#print(ramit.get('email'))
#print(ramit['interests'][0])
#print(ramit['friends'][0]['email'])
#print(ramit['friends'])
# 3a. Write a python expression that gets the email address of Ramit.
# 3b. Write a python expression that gets the first of Ramit's interests.
# 3c. Write a python expression that gets the email address of Jasmine.
# 3d. Write a python expression that gets the second of Jan's two interests.


# 4. Letter Summary
# Write a letter_histogram function that takes a word as its input,
# and returns a dictionary containing the tally of how many times
# each letter in the alphabet was used in the word. For example:

word = input('Enter a word: ')
wordList =[]
alphabetDict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
alphabetlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for y in word:
    wordList.append(y)
listcounter = 0
wordcounter = 1
while wordcounter < len(word):
    for x in alphabetList:
        if x == wordList [wordcounter]:
            alphabetDict[x] += 1
wordcounter += 1
print(alphabetDict)

# >>>letter_histogram('banana')
# {'a': 3, 'b': 1, 'n': 2}


# Word Summary
# Write a word_histogram function that takes a paragraph of text as its input, and returns a dictionary containing the tally of how many times each word in the alphabet was used in the text. For example:

# >>> word_histogram('To be or not to
