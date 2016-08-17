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

# page 30
