print('Welcome to the Band Name Generator.')

# getting name of the city in which the user grew using input() method and saving that in a variable
cityName = input('What\'s name of the city you grew up in?\n')  # here \n is added for getting
# the input in a new line

# getting name of the pet of the user using the input() method and saving that in a variable
petName = input('What\'s your pet\'s name?\n')  # here \n is added for getting
# the input in a new line

# concatenating the cityName and petName to form the name of the band
bandName = cityName + " " + petName

print('Your band name could be ' + bandName)
