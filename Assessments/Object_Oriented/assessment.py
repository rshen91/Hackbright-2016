"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
# 1. Encapsulation: Unlike dictionaries, classes allow for encapsulation. Any method
# that will apply to a class can be contained within that class. For instance, we
# used the Animal example during lecture. Since all animals speak, that is 
# encapsulated in the parent class Animal. Class attributes specific to dogs or cats
# can be included within their own classes.

# 2. Abstraction: Abstraction is class's way of hiding the nitty gritty details. The 
# example that helps me remember this design advantage the most is the painterbot 
# example. In the class method, we can see that our method is painting the melon, 
# but we don't know how it is and we don't need to.

# 3. Polymorphism: Polymorphism is classes ability to smoothly change components 
# without a chain of elifs. Even if we change a method in a child class from a parent
# class, or we can use default values. Either way allows the programmer to avoid 
# redundancy. 

2. What is a class?
"Type" of thing like a string or file and it is written is UpperCamelCase. 

3. What is an instance attribute?
# Each time a variable is created in a class, it goes through a dunder init and 
# takes on the class attributes. However, there are instance attributes that differ 
# from the class. I think in one of our lab exercises, if a melon order was less than
# 10 and international then the tax amount would be different. 

4. What is a method?
# A method is really similar ot a function but it's inside the class. Based on 
# lecture notes, they're called like object.method(arguments). Unlike functions, 
# the first argument in a method is always self, even if it isn't called in an 
# instance. 

5. What is an instance in object orientation?
# An instance is an example that belongs in that class. For instance, when we 
# were in class, we had the Animal parent class and the Cat child class. 
# An instance would be Pruscilla the cat. When we call her in the Cat class 
# it might look like this:

# Pruscilla = Cat("Pruscilla") assuming that all that we need to provide in the cat
# class is the cat's name.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

# A class attribute applies to the entire class and any descendent classes, whereas 
# an instance attribute can affects at the level of each instance (an each instance
# could be affected slightly differently). 
# For instance, in the lecture notes when we were using the example of the parent 
# class Animal, if we had a class attribute of species = 'dog', then that's
# making all animals dogs. One example when class attributes would be helpful, 
# especially with a parent class, is similar to the tax melons exercise. If all 
# melons, regardless of being domestic or international orders, are taxed to some 
# degree, then the parent class AbstractMelonOrder could have a class attribute of
# the minimum tax amount. In the descendent classes, the class attribute could be 
# the additional tax amount (like with HungryCat versus Cat). Instance attributes 
# are in the methods within a class. When a method is called, then it only applies 
# to that instance but not necessarily all the other instances in the class. If it
# does apply to all instances in the class, then it should become a class attribute,
# not an instance attribute. 



"""
# Parts 2 through 5:
# Create your classes and class methods
class Students(object):
"""Class Students to store first, last, address"""

def __init__(self, first_name, last_name, address): #each instance will have a different name etc. 
    self.first_name = first_name
    self.last_name = last_name
    self.address = address

class Question(object):
"""Class that can store questions and answers"""

def __init__(self, question, answer, correct_answer):
    self.question = question
    self.answer = answer
    self.correct_answer = correct_answer

def ask_and_evaluate(self, answer, correct_answer):
"""Prints the question asks the user for an answer, return T/F"""
    print answer = question.raw_input() #want the question to be asked to the user
    if answer == correct_answer:
        return True
    False

class Exam(object):
"""Exams have questions within them"""

def __init__(self, name):
"""Using super to initialize in Exams since we want some Question class attr."""
    self.name = first_name+last_name
    super(Question).__init__(question, answer, correct_answer) 

def add_question(self, question, correct_answer):
"""Part 3 of the assessment"""
    return question, correct_answer

def administer(self, question):
"""Administer all the exam's questions, returns user's score"""
    score = 0
    for problems in question:
        if problems.ask_and_evaluate() == True:
            score += 1
    return score

#Part 4
def take_test(exam, student):
"""Takes an exam and student assigns the score to the student"""
    score = {} #a key value pair so a dictionary?
    student_score = student.administer() 
    #hopefully calling a function within a function correctly
    score[student] = student_score #add it to the dictionary
    return score

def example(new_questions, student):
"""Creates an exam, adds questions, creates a student, administers the test"""
    exam = add_question().append(new_questions)
    return student.administer(exam) #can this () have exam in them?

#Part 5: Sounds like mixins?
class Quiz(take_test, object):
"""Quizzes are pass/fail. If you answer half the ques. correctly - you pass"""
#want to take take_test from the Exam class but don't want other parts

def __init__(self,  question, answer, correct_answer):
"""Want to super some of Exam's init"""
    self.name = first_name+last_name
    super(Question).__init__(question, answer, correct_answer)

def take_quiz(take_test, self): #does take_test have to be restated here?
"""Need to override some parts of take test"""
    score = 0
    len_score = len(score)
    if score.take_test()/len_score < .5: #calling a method within this function
        return False





