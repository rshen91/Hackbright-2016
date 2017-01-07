"""List Assessment 

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """
    odd = [] #empty list to return at the end
    for odds in numbers: #let's go through each thing in the input numbers
        if odds%2 != 0: #is the thing odd
            odd.append(odds) #append that to the list
    return odd


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo
    """
    for item in items: #go through each thing in the items list
        print items.index(item), item #print its index and then it


def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale"],
        ...     ["hummus", "beets", "bagel", "lentils", "kale"]
        ... )
        ['bagel', 'kale']

    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """
    the_best_foods = [] #new empty list to add the common foods in
    for foods in foods1: #iterate through foods
        if foods in foods2: #if it's in the first list and the second list
            the_best_foods.append(foods) #we add it
    return the_best_foods #here's the awesome list


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """
    every_other = []
    for item in items:
        if int(items.index(item)) % 2 == 0:
            every_other.append(item)
    return every_other


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """
    n_large_things = [] 
    count = 0
    if n == 0:
        return []
    else:
        while count < n: #While loop to run until the big values are taken n times 
            for item in items: #iterate 
               big_n = max(items) #has to be inside the for loop or there's an 
               #unbound local error
               n_large_things.append(big_n) #add the max to the n large things list
               items.remove(big_n) #couldnt get del or pop to work
               count += 1 #since we are changing len we need to have 
               #a count variable or something
               
               #need to get duplicates removed or only counted per n times
               if len(n_large_things) > n:
                n_large_things.pop() #used pop since we don't know the values in the list
    n_large_things = sorted(n_large_things) #sorts the list to ascending order
    return n_large_things


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
