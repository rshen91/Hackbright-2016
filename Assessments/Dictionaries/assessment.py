"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase): #this works on bypthon 
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    words_occurence_in_phrase = {} #create an empty dictionary
    words = phrase.split() #need to use to split on the spaces for each word
    print "This should be all the words in the string", words
    for word in words: #want each word in the string to be checked
        words_occurence_in_phrase[word] = words.count(word) #looked up the 
        # .count() in a lab exercise with the counting words
        return words_occurence_in_phrase


        # incorrect and first instinct commented out below
        # if word not in words_occurence_in_phrase: #is this key in the dictionary yet
        #     words_occurence_in_phrase[words] = 1 #if not add it's value of 1
        # else:
        #     words_occurence_in_phrase[words] += 1 #it's already in the dictionary
        #     #increase its value by one



def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon
    
    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25 
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25
        
        >>> get_melon_price('Tomato')
        'No price found'
    """
    melon_dict = {'Watermelon': 2.95, 'Cantaloupe': 2.50, 'Musk': 3.25, 
                        'Christmas': 14.25} #we can create a dictionary!

    #for melons in melon_dict: #use the first instinct approach
        #return price #we can just return the price
    return melon_dict.get(melon_name, 'No price found')
    # for melon in melon_name: #second instinct and we don't need a for loop
    #     price = melon_name[melon]
    #     return price 

    # return melon_name in melon_dictionary.values() #first instinct 
    


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """
    word_length_dict = {} #need to make a dictionary
    #words = words.split()
    for word in words:
        if len(word) in word_length_dict:
            word_length_dict[len(word)].append(word)
        else:
            word_length_dict[len(word)] = [word]
    return word_length_dict.items().sort()
    #(number of word length : list of words that length)
    #add to the dictionary the keys of word length and the values of the list 
    #of words
    #return the values/list of words

    #sort a lot 
    #     word_length_dict[num_word_length] = list_of_words_that_num

    # for item in letter_counts.items()
    #     if item[1] > max_value:
    #         max_value = item[1]
    #         max_key = item[0]
    


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    pirate_translation = {"sir": "matey", "hotel": "fleabag inn", 
                            "student": "swabble", "man": "matey",
                            "professor": "foul blaggart", "restaurant":
                            "galley", "your": "yer", "excuse": "arr",
                            "students": "swabbles", "are": "be", "restroom": 
                            "head", "my": "me", "is": "be"}
                             # make a dict with the words as key values
    #if the words in the phrase are in the dictionary then replace them
    pirate_talk = ""
    for word in phrase: #word in the list of words from lower and split
        if word in pirate_translation:
            pirate_talk += pirate_translation.get(word)
        else:
            pirate_talk += word
    return pirate_talk
    #return the joined the strings together


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
# names_dict[name] = values name[0] needs to equal the last name [-1]
    return []

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
