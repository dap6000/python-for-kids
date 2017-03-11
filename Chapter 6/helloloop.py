for x in range(0, 20):
    print('hello %s' % x)
    if x < 9:
        break
print("Loop is done!")
# range(0, 20) produces an iterator that will count from zero to twenty, and the
# for loop will execute for each count in the range storing the current count
# in x. But on the firts pass x will be zero and the if statement on line 4 will
# be true so we will execute the break statement on line 4 and break out of the
# loop. We will only get the print statement for x = 0.
