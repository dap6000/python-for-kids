fname = 'Derek'
lname = 'Pennycuff'
template = 'Hi there, %s %s!'
# If multiple placeholders expects to be given a tuple then we can store
# that tuple in a variable first.
full_name = (fname, lname)
print(template % full_name)
