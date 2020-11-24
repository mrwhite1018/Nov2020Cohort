
#myList = (2, 5, 12, 13, 17)
#def smallest(a):
#    c = a[0]
#    for item in a:
#        if item < c:
#            c = item
#    return c
#print(f'Smallest number: {smallest(myList)}')


#myList = (2, 5, 12, 13, 17)
#def largest(a):
#    c = a[0]
#    for item in a:
#        if item > c:
#            c = item
#    return c
#print(f'largest number: {largest(myList)}')

#strList = ['Pariis', 'CJ', 'Jeremiah', 'Harrisyn', 'Liincoln', 'Zaemier']
#def shortest(short):
#    c = len(short[0])
#    d = short[0]
#    for item in short:
#        if len(item) < c:
#            c = len(item)
#            d = item
#    return d
#print(shortest(strList))

strList = ['Pariis', 'CJ', "Jeremiah", 'Harrisyn', 'Liincoln', 'Zaemier']
def longest(long):
    c = len(long[0])
    d = long[0]
    for item in long:
        if len(item) > c:
            c = len(item)
            d = item
    return d
print(longest(strList))