fruit_basket = ('apple','orange','strawberry','blueberry','mango')
guess = raw_input('Guess one fruit in the fruit basket:')

if guess in fruit_basket:
    print "Correct! Good guess!"
else:
    print "Nope, don't have that one"

