# Suppose you are digging in your backyard and uncover a bag of 20 gold coins.
# The next day, you sneak down to the basement and stick the coins inside your
# grandfather's steam-powered replicating invention (luckily, you can just
# fit the 20 coins inside). You hear a whiz and a pop and, a few hours later,
# out shoot another 10 gleaming coins.
# How many coins would you have in your treasure chest if you did this every
# day for a year? On paper, the equations might look like this:
#
# 10 x 365 = 3650
# 20 + 3650 = 3670
10 * 365
20 + 3650

# Now, what if a raven spots the shiny gold sitting in your bedroom, and every
# week flies in and manages to steal three coins?
3 * 52
3670 - 156

# Or we can define everything in variables. If we name our vairables clearly
# then the program we write can almost be read like a story. Or at least
# like a word problem from math class. In the real world we probably would
# not use variable names quite THIS long. :)
coins_found = 20
coins_replicated_per_day = 10
days_per_year = 365
raven_stolen_coins_per_week = 3
weeks_per_year = 52

coins_replicated_per_year = coins_replicated_per_day * days_per_year
year_of_coins = coins_found + coins_replicated_per_year
year_of_stolen_coins = raven_stolen_coins_per_week * weeks_per_year
coins_at_years_end = year_of_coins - year_of_stolen_coins

print("At the end of a year you would have %d coins." % coins_at_years_end)

# We can change the story our program tells by changing the value of any of
# our variables. The example in the book is that you set up a scare crow
# so now the raven only steals 2 coins a week. But we could also change the
# story by making the steam-powered replicating invention produce a different
# number of coins. Or we could move our story to some sort of alien world with
# a year having a different number of days or weeks or both. Or any combination
# of those changes.
