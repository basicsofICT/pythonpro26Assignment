"""
5.3.5 Phone book, version 2

Please write an improved version of the phone book application. It should work 
as follows:

    command (1 search, 2 add, 3 quit): 2
    name: peter
    number: 040-5466745
    ok!
    command (1 search, 2 add, 3 quit): 2
    name: peter
    number: 09-22223333
    ok!
    command (1 search, 2 add, 3 quit): 1
    name: peter
    040-5466745
    09-22223333
    command (1 search, 2 add, 3 quit): 2
    name: emily
    number: 045-1212344
    ok!
    command (1 search, 2 add, 3 quit): 1
    name: emily
    045-1212344
    command (1 search, 2 add, 3 quit): 1
    name: mary
    no number
    command (1 search, 2 add, 3 quit): 3
    quitting...

In this version each name can have multiple numbers attached. Adding a new number 
will not replace the old one, but adds to the list of numbers.

Notice! In this exercise you should not print any of the three commands (search, 
add, quit) shown above. Only print the prompt "command (1 search, 2 add, 3 quit): ".
"""

# TODO: Implement your solution below this line

