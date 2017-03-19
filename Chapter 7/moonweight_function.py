import sys

def astro_weight(gained, current_w, current_y, years, planet, gravity):
    current_weight = current_w
    for year in range(0, years) :
        current_weight = current_weight + gained
        moon_weight = current_weight * gravity
        msg = "In the year %d my %s weight would be %f kilos."
        print(msg % (current_y + year, planet, moon_weight))

def moon_weight():
    planet = 'moon'
    gravity = 0.165
    print('Please enter your current Earth weight (in kilos)')
    current_w = int(sys.stdin.readline())
    print('Please enter the current year')
    current_y = int(sys.stdin.readline())
    print('Please enter the amount your weight might increase each year')
    gained = float(sys.stdin.readline())
    print('Please enter the number of years to calculate')
    years = int(sys.stdin.readline())
    astro_weight(gained, current_w, current_y, years, planet, gravity)

moon_weight()
