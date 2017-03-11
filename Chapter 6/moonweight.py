current_weight = 98 # in kilos
current_year = 2017
for year in range(0, 15) :
    current_weight = current_weight + 1
    moon_weight = current_weight * 0.165
    msg = "In the year %d my moon weight would be %f kilos."
    print(msg % (current_year + year, moon_weight))
