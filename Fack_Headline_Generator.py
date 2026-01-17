# import random module
import random

# create subjects
subjects = [
    "Sharukh Khan",
    "Salman Khan",
    "Virat kohli",
    "Nirmala Sitharaman",
    "Prime Minister Modi"
]

actions = [
    "dances with",
    "eats",
    "celebrates",
    "declares war on",
    "cancels"
]

places_or_things = [
    'at Red Fort',
    'in Mumbai Local Train',
    'a plate of samosa',
    'inside parliament',
    'during IPL match'
]

# headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {places_or_thing}"
    print('\n' + headline)

    user_input = input('\nDo you want another headline? (yes/no):- ').strip().lower()
    if user_input == 'no':
        break

# goodbye message
print('\nThanks for using the Fack News headline generator, Have a fun')

# categorys, custome detalis, save
