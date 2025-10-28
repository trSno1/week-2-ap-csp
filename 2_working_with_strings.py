
# ----------------------------------------
# . Working with Strings
# ----------------------------------------

# Strings are sequences of characters enclosed in quotes (' ' or " ")
greeting = "Hello"    #string date type 
name = "World"        # strng data type 

# ----------------------------------------
# Basic String Operations
# ----------------------------------------

# 1. Concatenation: Combining strings using the + operator
message = greeting + " " + name
print("Concatenated String:", message)  # Output: Hello World

# ----------------------------------------
# 2. String Functions
# ----------------------------------------

phrase = "Python is FUN!"

# # Convert all characters to lowercase
print("Lowercase:", phrase.lower())  # Output: python is fun!

# # Convert all characters to uppercase
print("Uppercase:", phrase.upper())  # Output: PYTHON IS FUN!

name = "Jayden Aguilar"
print("Is Uppercase?:", phrase.isupper())
print("name:", name.islower())
print("name", name.capitalize)
print("Length of phrases:"len(phrase))

declaration_of_independence = "When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."
length_dec = len(declaration_of_independence) 
# # Check if all characters are uppercase
# print("Is Uppercase?", phrase.isupper())  # Output: False

# # Find the length of the string
# print("Length of phrase:", len(phrase))  # Output: 14

# # ----------------------------------------
# # 3. Indexing and Slicing
# # ----------------------------------------

# # Indexing: Access characters by position (0-based index)
# print("First character:", phrase[0])  # Output: P
# print("Last character:", phrase[-1])  # Output: !

# # Slicing: Get a range of characters (start inclusive, end exclusive)
# print("Characters 1 to 4:", phrase[1:4])  # Output: yth

# # Example combining everything:
# print("Formatted Example:", (greeting + " " + name + "!").upper())
# # Output: HELLO WORLD!


# # ----------------------------------------
# # 7. Strings: Advanced Concepts
# # ----------------------------------------

# # Creating Strings: use single or double quotes
# greeting1 = 'Hello'
# greeting2 = "Hi there"

# # Printing Strings
# print(greeting1)
# print(greeting2)

# # ----------------------------------------
# # String Methods
# # ----------------------------------------

# sentence = "Python is fun to learn"

# # .split(): Splits the string into a list of words
# words = sentence.split()
# print("Split result:", words)

# # .format(): Allows inserting values into strings using {}
# name = "Marvin"
# age = 35
# intro = "My name is {} and I am {} years old.".format(name, age)
# print(intro)

# # You can also use f-strings (Python 3.6+)
# intro_fstring = f"My name is {name} and I am {age} years old."
# print(intro_fstring)
