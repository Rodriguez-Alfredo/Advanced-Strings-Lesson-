#!/bin/python3

#ADVANCED STRINGS

my_name = "Alfredo"

print(my_name[0]) #return first letter of the string
print(my_name[-1]) #returns last letter of the string

sentence = "This is a sentence."
print(sentence[:4]) #returns the 4 letters but stops at position 4... counts start with 0 

print(sentence.split()) #delimeter - default is a space.. makes it a list

sentence_split = sentence.split()#made to delimeter
sentence_join= ' '.join(sentence_split) #joined it back together with a space
print(sentence_join) #strings are still immutable

quote = "He said, 'give me all your money'"
print(quote) #shows how to enter quotes in a string by using opposite of the quotes used to start the string

quote = "He said, \"give me all your money\"" #use backslach to ignore 

print(quote)

too_much_space = "        hello       "
print(too_much_space.strip()) #remove the extra space '.strip'

print("A" in "Apple") #case sensative - looking for capital A in apple.. True
print("a" in "Apple") #searches for lowercase a in Apple... Flase

letter = "A"
word = "Apple"

print(letter.lower() in word.lower()) #frocing all character to be lowercase to force a TRUE

movie = "Scream"
print ("My favorite movie is {}.".format(movie)) #string format method

print ("My favorite movie is %s." %movie)

print (f"My favorite movie is {movie}.") #string literal -- recommended method!!

#Thank You TCM Security