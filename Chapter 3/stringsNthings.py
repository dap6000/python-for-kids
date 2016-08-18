# Double quoted string in a variable
fred = "Why do gorillas have big nostrils? Big fingers!!"
print(fred)
# Single quoted string in a variable (reusing the same variable)
fred = 'What is pink and fluffy? Pink fluff!!'
print(fred)

# The book next shows an example that raises a SyntaxError due to EOL
# I'll skip that here since I'm not writing this in the Python shell

# Triple quoted (really 3 single quotes) string example
# Only one exclaimation point this time, but as you can see line breaks are OK
fred = '''How do dinosaurs pay their bills?
With tyrannosaurus checks!'''
print(fred)

# Next the book covers additional SyntaxError examples caused by unescpaed
# quotes. I'll skip those as well.

# Triple quotes to the rescue again! We can safely use both single and double
# quotes inside a triple quoted string and we don't even have to escape them.
silly_string = '''He said, "aren't can't shoulnd't wouldn't."'''
print(silly_string)

# But you can use whatever you want so long as you escape the character you are
# using to quote your string when they appear _inside_ your string.
single_quote_str = 'He said, "aren\'t can\'t shoulnd\'t wouldn\'t."'
double_quote_str = "He said, \"aren't can't shoulnd't wouldn't.\""
print(single_quote_str)
print(double_quote_str)

# String substitution / embedding values / inserting values
# G and I discussed this the other night in the context of Pokemon, as in:
# template = "%s used %s."
# pokemon_name = "PIKACHU"
# move_name = "Scratch"
# print(template % (pokemon_name, move_name))
# Anyway...
myscore = 1000
message = 'I scored %s points'
print(message % myscore)

# Dynamic string substitution
joke_text = '%s: a device for finding furniture in the dark'
bodypart1 = 'Knee'
bodypart2 = 'Shin'
print(joke_text % bodypart1)
print(joke_text % bodypart2)

# Multiple placeholders
nums = 'What did the number %s say to the number %s? Nice belt!!'
print(nums % (0, 8))

# Multiplying strings
print(10 * 'a')
print(1000 * 'snirt')

# See myletter.py

# Lists
wizard_list = 'spider legs, toe of frog, eye of newt, bat wing, slug butter, snake dandruff'
print(wizard_list)
wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing',
    'slug butter', 'snake dandruff']
print(wizard_list)

# Printing an individual value
print(wizard_list[2])

# Changing an individual value
wizard_list[2] = 'snail tongue'
print(wizard_list)

# Getting a subset from a list
print(wizard_list[2:5])

# List of numberic values
some_numbers = [1, 2, 5, 10, 20]
print(some_numbers)

# List of string values, including repeated values
some_strings = ['Which', 'Witch', 'Is', 'Which']
print(some_strings)

# List of mixed values
numbers_and_strings = ['Why', 'was', 6, 'afraid', 'of', 7, 'because', 7, 8, 9]
print(numbers_and_strings)

# Nested Lists
numbers = [1, 2, 3, 4]
strings = ['I', 'kicked', 'my', 'toe', 'and', 'it', 'is', 'sore']
mylist = [numbers, strings]
print(mylist)

# Adding items to a list
wizard_list.append('bear burp')
print(wizard_list)
wizard_list.append('mandrake')
wizard_list.append('hemlock')
wizard_list.append('swamp gas')
print(wizard_list)

# Removing items from a list
del wizard_list[5]
print(wizard_list)
del wizard_list[8]
del wizard_list[7]
del wizard_list[6]
print(wizard_list)

# List arithmetic, page 36
# List concatenation
list1 = [1, 2, 3, 4]
list2 = ['I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']
print(list1 + list2)

# Storing a concatenated list in a variable
list1 = [1, 2, 3, 4]
list2 = ['I', 'ate', 'chocolate', 'and', 'I', 'want', 'more']
list3 = list1 + list2
print(list3)

# Repeating a list with multiplication
list1 = [1, 2]
print(list1 * 5)

# tuples
fibs = (0, 1, 1, 2, 3)
print(fibs[3])

# Tuples are immutable. This line would raise an error if we actually ran it.
# fibs[0] = 4

# Maps
favorite_sports = {'Ralph Williams' : 'Football',
    'Michael Tippett' : 'Basketball',
    'Edward Elgar' : 'Baseball',
    'Rebecca Clarke' : 'Netball',
    'Ethel Smyth' : 'Badminton',
    'Frank Bridge' : 'Rugby'
    }
# Print entire map
print(favorite_sports)
# Print a single item from the map
print(favorite_sports['Rebecca Clarke'])

# Delete an item from the map
del favorite_sports['Ethel Smyth']
print(favorite_sports)

# Replace an item from the map
favorite_sports['Ralph Williams'] = 'Ice Hockey'
print(favorite_sports)

# This isn't covered in the book but we can also add a new item to the map
# using the same syntax as the replace example. Just use a brand new key.
favorite_sports['Derek Pennycuff'] = 'Calvinball'
print(favorite_sports)
