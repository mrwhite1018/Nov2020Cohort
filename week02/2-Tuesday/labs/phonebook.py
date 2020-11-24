import pickle

with open('phoneBook.pickle', 'rb') as fh:
    data = pickle.load(fh)

phoneBook = {'mom': '7701234567', 'wife': '7702345678', 'son1': '7703456789', 'son2': '7704567890', 'son3': '3021234567'}
def lookUp():
    nameEntry = input('Enter name: ')
    lnameEntry = nameEntry.lower()
    print('Name: ' + nameEntry)
    print('Number: ' + phoneBook.get(lnameEntry))
def setEntry():
    newEntry = input('Enter name: ').lower()
    cnewEntry = newEntry.capitalize()
    newNumber = str(input('Enter number (no spaces):'))
    phoneBoook[newEntry] = newNumber
def delete():
    newDelete = input('Enter name: ').lower()
    del phoneBook [newDelete]
def listEntries():
    print(phoneBook)
def quit():
    with open('phonebook.pickle', 'wb') as fx:
        pickle.dump(phoneBook, fx)
    print('bye.') 

x = 0
while x == 0:
    firstInput = int(input('Electronic Phone Book \n =\n1. Look up an entry\n2. Set an enrty\n3. Delete an entry\n4. List all entries\n5. Quit\nWhat do you want to do (1-5)?'))
    if firstInput == 1:
        lookUp()
    elif firstInput == 2:
        setEntry()
    elif firstInput == 3:
        delete()
    elif firstInput == 4:
        listEntries()
    elif firstInput == 5:
        break
    else:
        print('Sorry wrong number.')

print('Thank you. Have a nice day.')