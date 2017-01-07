"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2 """
def num_spaces(string):
    for things in string:
        count = 0
        if things == " ":
            count += 1
        return count

"""   
    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:
"""
def full_title(name, jobtitle="Engineer"): 
    return jobtitle + " "+ name
    """>>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn
    
    """
def write_letter(sender, name, jobtitle="Engineer"):
    def full_title(name, jobtitle="Engineer"):
        print "Dear {}, I think you are amazing! Sincerely, {}".format(full_title, sender)
################################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".
def hello_world():
    print 'Hello World'

# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.
def say_hi(name):
    print "Hi {}".format(name)


# 3. Write a function called 'print_product' that takes two integers and multiplies
#    them together. Print the result.
def print_product(a, b):
    print a*b 

# 4. Write a function called 'repeat_string' that takes a string and an integer and
#    prints the string that many times
def repeat_string(a,b):
    print a*b #this works! how cool

# 5. Write a function called 'print_sign' that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".
def print_sign(integer):
    if integer > 0:
        print "Higher than 0"
    if integer < 0:
        print "Lower than 0"
    else:
        print "Zero"

# 6. Write a function called 'is_divisible_by_three' that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.
def is_divisible_by_three(integer):
    if integer % 3 == 0:
        return True

# 7. Write a function called 'num_spaces' that takes a sentence as one string and
#    returns the number of spaces.
def num_spaces(string):
    for things in string:
        count = 0
        if things == " ":
            count += 1
    return count

# 8. Write a function called 'total_meal_price' that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.
def total_meal_price(price, tip=.15):
    return price + price * tip

# 9. Write a function called 'sign_and_parity' that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.
#
#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity.
def sign_and_parity(a):
    sp = []
    if a%2 == 0:
        sp.append("Even")
        if a > 0:
            sp. append("Positive")
        else:
            sp.append("Negative")
    else:
        sp.append("Odd")
        if a > 0:
            sp.append("Positive")
        else:
            sp.append("Negative")
    print sp


################################################################################
# PART TWO

# 1. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.
def full_title(name, jobtitle="Engineer"): 
    return jobtitle + " "+ name

# 2. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.
def write_letter(sender, name, jobtitle="Engineer"):
    def full_title(name, jobtitle="Engineer"):
        print "Dear {}, I think you are amazing! Sincerely, {}".format(full_title, sender)

#nums function
# >>> nums = [1, 2]
#     >>> add_new_number(5, nums)
#     >>> nums
#     [1, 2, 5]
def nums():
    def add_new_numbers(inte, nums):
        print inte
#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print


