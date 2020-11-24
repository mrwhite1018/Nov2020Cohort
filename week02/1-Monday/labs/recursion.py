# 1. Write a function called power which accepts a base and an exponent.
# The function should return the power of the base to the exponent.

#def power(base, exponent):

#    if exponent ==0: 
#        
#        return 1

#    return base * power(base, exponent -1)

#result = power(2, 5)
#result = power(2, 4)
#result = power(2, 3)
#result = power(2, 2)
#result = power(2, 1)
#result = power(2, 0)
#print(result)

# 2. Write a function factorial which accepts a number and returns
# the factorial of that number.  A factorial is the product of an
# interger and all the integers below it; eg. , factorial four( 4!) is
# equal to 24, because 4 * 3 * 2 * 1 equals 24.  factorial zero (0!) is always 1.

#def factorial(n):
#    factorial = 2
#    x = 2
#    if factorial < n:
#        print(factorial, end = '4')



#result = factorial(4) # 24

# 3. Write a function called recursiveRange which accepts a number and adds up all
# the numbers from 0 to the number passed to the function

#def recursiveRange(n):

#    if (n == 0): return 0
#   return n + recursiveRange(n -1)
#result = recursiveRange(5)
#print(result)



# 4. Write a recursive function called reverse which accepts
# a string and returns a new string in reverse


#def reverse(a):

#    if len(a) == 0:

#        return a
#    return reverse(a[1:]) + a[0]

#result = reverse('There she goes')

#print(result)

# 5. Write a recursive function called isPalindrome which returns
# true if the string passed to it is a palindrome (reads the same forward and backward).
# Otherwise returns false.


# isPalindrome('awesome') // false
# isPalindrome('foobar') // false
# isPalindrome('tacocat') // true
# isPalindrome('amanaplanacanalpanama') // true
# isPalindrome('amanaplanacanalpandemonium') // false


# 6. Write  function called product ofArray which takes in
# an array of numbers and returns the product of them all


# 7. Write a recursive function called fib which accepts a number and
# returns the nth number in teh Fibonacci Sequence. Recall that the
# Fibonacci Sequence is the Sequence of whole numbers 1, 1, 2, 3, 5, 8, ... which
# starts with 1 and 1, and where ever number
# thereafter is equal to the sum of the previous two numbers.


def fib(n):

    if n < 2:
        return n

        return fib(n-1) + fib (n-2)

result = fib(5)
print(result)
