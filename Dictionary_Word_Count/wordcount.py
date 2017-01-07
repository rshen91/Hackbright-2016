# put your code here.

# counts how many times each space-separated word occurs in the file
def count_words(poem):
    poem = open(poem)
    word_count = {} #empty dictionary named word_count
    for lines in poem: #iterate through the file to get each line that creates a bunch of strings
        #words = lines.strip() #gets rid of blank space
        words = lines.strip().split() #gets each individual word
        for word in words: #iterates through each word in each string
            word_count[word] = word_count.get(word, 0) + 1 #empty dict gets all the words/keys and giving the value
    for word, count in word_count.items():
        print word, count
    poem.close()
count_words("test.txt")