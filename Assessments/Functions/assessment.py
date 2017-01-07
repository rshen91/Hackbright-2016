# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def item_cost(state, cost, tax_amount=0.05):
    if state == "CA":
        tax_amount = 0.07
        return cost*tax_amount + cost 
    else:
        return cost*tax_amount + cost

item_cost("ND", 4) #=> Should be $4.20
item_cost("CA", 4) #=> Should be $4.28

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".
def is_berry(fruit_name):
    if fruit_name == "strawberry" or fruit_name == "cherry" or fruit_name == "blackberry":
        return True
    return False


#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.
def shipping_cost(fruit_name):
    if is_berry == True:
        return 0
    else:
        return 5


# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
def is_hometown(town):
    real_hometown = raw_input("What is your hometown? ")
    if town == real_hometown:
        return True
    else: 
        return False

#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
def full_name(first, last):
    return first+ " "+ last

#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.
def hometown_greeting(hometown, first, last):
    if is_hometown == True:
        print "Hi {}, we're from the same place!".format(full_name)
    else:
        print "Hi {}, where are you from?".format(full_name)

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.
def increment(x=1):
    def add(y):
        return x + y 

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to 
# a variable name, addfive. Call addfive with y = 5. Call again with y = 20.
#Will need more help with this one - not sure what it's asking  
addfive = increment(5)
addfive(5)
addfive(20)

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.
def append_numbers_to_number_list(number, lst_numbers):
    return lst_number.append(number)
#####################################################################