print("Top 5 cool words starting with the letter W.")
words = ['Werewolf', 'Wreckage', 'Wildfire', 'Wraith', 'Warp']
count = 1
for word in words :
    print("%d %s" % (count, word))
    count = count + 1
# When using a format string with more than 1 argument pass a tuple containing
# the arguments in order after the % character.
