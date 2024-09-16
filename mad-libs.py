# Arden Boettcher
# 9/16/24
# Mad Libs

adjective1 = input('Give me an adjective: ')
color = input('Give me a color: ')
time = input('Give me a time: ')
adjective2 = input('Give me another adjective: ')
place = input('Give me a place: ')
food1 = input('Give me a food: ')
food2 = input('Give me another food: ')
verb = input('Give me a verb: ')
noun = input('Give me a noun: ')
number = input('Give me a number: ')

print(f'BATS ARE SO {adjective1.upper()}! They are {color.lower()} animals which have wings.') # it was too long so I split it up onto multiple lines
print(f'They like to fly around at {time} which makes some people scared of them.') # the reason there are so many .lower() 
print(f'But bats are {adjective2.lower()}, and they don\'t want to hurt people. ')
print(f'I have a pet bat that lives in {place.lower()}. I like to feed him {food1.lower()} and {food2.lower()}. ')
print(f'He likes to {verb.lower()}. I am his favorite person, but he also likes {noun}. ')
print(f'I want to convince my parents to get me {number.lower()} more bats.')
