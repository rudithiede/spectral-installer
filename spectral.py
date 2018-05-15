from random import choice
from random import randint, randrange
import decimal
import sys
from time import sleep

# Import data
with open(sys.path[0] + '/processes.txt') as f:
    processes = f.readlines()

with open(sys.path[0] + '/names.txt') as f:
    names = f.readlines()

with open(sys.path[0] + '/doneMessages.txt') as f:
    doneMessages = f.readlines()

def selectName():
    """Select a random name."""
    name = str(choice(names)).strip()
    return name

def instantProcess():
    """The shortest type of process."""
    process = str(choice(processes)).strip()
    name1 = selectName()
    while True:
        name2 = selectName()
        if not name1 == name2:
            break

    simpleName = False

    # Randomly decide how to composite names
    compositeD20 = randint(0,20)
    if compositeD20 > 0 and compositeD20 < 10:
        # Concatenate names with a hyphen
        name = '{}-{}'.format(name1, name2)
    elif compositeD20 >= 10 and compositeD20 < 17:
        # Concatenate names
        name = '{}{}'.format(name1, name2)
    else:
        # Use only one name, but flag so that a version number is generated
        name = name1
        simpleName = True

    # Randomly decide whether to add a version number
    addNumberD20 = randint(0,20)
    if addNumberD20 > 6 and addNumberD20 < 16:
        # Render with name and version number
        return('{} {}{} ...'.format(process, name, versionNumber()))
    elif addNumberD20 > 16:
        # Render with composite name and version number
        return('{} {}{}{} ...'.format(process, name, randint(0,9), versionNumber()))
    else:
        # Render with name only, but with version number if simple name
        if not simpleName:
            return('{} {} ...'.format(process, name))
        else:
            return('{} {}{} ...'.format(process, name, versionNumber()))

def versionNumber():
    """Generate a random version number."""
    # Add hyphen? Flip a coin
    hyphenCoin = randint(0,1)
    hyphen = '-'
    if hyphenCoin == 0:
        hyphen = ''

    # Number complexity: 50% = x.x.x, 25% = x.x, 25% = x
    complexityD20 = randint(0,20)
    if complexityD20 >= 15 or complexityD20 <= 5:
        return '{}{}.{}.{}'.format(hyphen, randint(0,9), randint(0,9), randint(0,9))
    elif complexityD20 <= 10:
        return '{}{}.{}'.format(hyphen, randint(0,9), randint(0,9))
    else:
        return '{}{}'.format(hyphen, randint(0,9))

def doneMessage():
    """Select a random 'done' message."""
    message = str(choice(doneMessages)).strip()

    # Randomly decide whether to capitalize the done message and/or
    # whether to add a new line before it.
    capitalize = choice([True, False])
    addNewLine = choice([True, False])
    if capitalize:
        message = message.capitalize()
    if addNewLine:
        message = '\n{}'.format(message)

    return message

while True:
    print(instantProcess()),
    sleep(decimal.Decimal(randrange(300))/100),
    print(doneMessage())
