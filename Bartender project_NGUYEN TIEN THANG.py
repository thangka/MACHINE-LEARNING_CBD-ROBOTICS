questions = {
"strong": "Do ye like yer drinks strong?",
"salty": "Do ye like it with a salty tang?",
"bitter": "Are ye a lubber who likes it bitter?",
"sweet": "Would ye like a bit of sweetness with yer poison?",
"fruity": "Are ye one for a fruity finish?",}
ingredients = {
"strong": ["glug of rum", "slug of whisky", "splash of gin"],
"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
"fruity": ["slice of orange", "dash of cassis", "cherry on top"],}
#Given two above dictionaries, construct the Python program (using functions) to ask users entering their
#tastes and then match randomly with the ingredients (print out outputs for user)

import random
taste = input('Enter your taste: ')
print(questions[taste])
li = [i for i in questions.keys()]
def Bartender(taste):
    if taste in li:
        result = random.choice(ingredients[taste])
    else:
        result = 'ERROR INPUT. TRY AGAIN'
    return result
print(Bartender(taste))
