# Take a look at the space ship building function on page 86 of the book.
def spaceship_building(cans):
        total_cans = 0
        for week in range(1, 53):
            total_cans = total_cans + cans
            print('Week %s = %s cans' % (week, total_cans))

# One very important skill for programmers is to spot assumptions built in to
# code and condsider how likely those assumptions are to to shift over the
# lifetime of a project. This function is only 5 lines long but I can spot
# 2 assumptions in this code that could be factored out into parameters.
#
# Assumption 1 - We start with zero cans
def improved_spaceship_building1(cans_per_week, starting_cans) :
    total_cans = starting_cans
    for week in range(1, 53) :
        total_cans = total_cans + cans_per_week
        print('Week %s = %s cans' % (week, total_cans))

# Assumption 2 - We will always build our spaceships on planets with 52 weeks
# in a year
def improved_spaceship_building2(cans_per_week, starting_cans, weeks_per_year) :
    total_cans = starting_cans
    for week in range(1, weeks_per_year + 1) :
        total_cans = total_cans + cans_per_week
        print('Week %s = %s cans' % (week, total_cans))

# You may be able to spot some problems here. Our function names are getting
# long. But we don't HAVE to use long names. I'm just trying to make things
# a bit more clear through the names I use. But it also means we MUST include
# all 3 parameters to call the final version. We can fix that by setting
# default values for the 2nd and 3rd parameters.
def can_ship(cans_per_week, starting_cans=0, weeks_per_year=52) :
    total_cans = starting_cans
    for week in range(1, weeks_per_year + 1) :
        total_cans = total_cans + cans_per_week
        print('Week %s = %s cans' % (week, total_cans))

# Now if we want the same behavior as the version in the book we can just call:
can_ship(12)
# For example. But, if we get a grant for starting funds for 100 cans to build
# new ships we don't have to rewrite the fuction. We can just call it with a
# different value for the 2nd parameter:
can_ship(15, 100)
# And then, a year from now, when our successful spaceship building opperation
# gets moved to Mars, where there are 98 weeks in a year, we STILL don't have
# to rewrite our function. We can just call it like:
can_ship(20, 100, 98)

# And yes maybe this all seems a little silly. It's based on an example in the
# book that was a bit silly on purpose. But even those of us who have been doing
# this sort of thing for years can often catch ourselves building assumptions
# into our code. Sometimes an assumption works out and never causes a problem.
# Other times they cause us to have to rewrite significant chunks of a project.
# The worst part is even the idea of an assumption in our code needing to change
# or not is itself an assumption! We're not pyschic. And it takes time to write
# code with fewer assumptions. That extra work may never pan out. Or it may
# save us a ton more work in the future.

# I named this file after a web comic that has a strip dealing with this sort
# of problem. See it here https://xkcd.com/974/
