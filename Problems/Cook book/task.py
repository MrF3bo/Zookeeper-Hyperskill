pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingrident = input()

if ingrident in pasta:
    print("pasta time!")
if ingrident in apple_pie:
    print("apple pie time!")
if ingrident in ratatouille:
    print("ratatouille time!")
if ingrident in chocolate_cake:
    print("chocolate cake time!")
if ingrident in omelette:
    print("omelette time!")
