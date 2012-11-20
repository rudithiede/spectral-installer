from random import choice
from random import randint, randrange
import decimal
from time import sleep

# Import data
with open('processes.txt') as f:
    processes = f.readlines()

with open('names.txt') as f:
    names = f.readlines()

with open('doneMessages.txt') as f:
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

    # Randomly decide how to composite names
    compositeD20 = randint(0,20)
    if compositeD20 > 0 and compositeD20 < 10:
        # Concatenate names with a hyphen
        name = '%s-%s' % (name1, name2)
    elif compositeD20 >= 10 and compositeD20 < 17:
        # Concatenate names
        name = '%s%s' % (name1, name2)
    else:
        # Use only one name
        name = name1

    # Randomly decide whether to add a version number
    addNumberD20 = randint(0,20)
    if addNumberD20 > 6 and addNumberD20 < 16:
        # Render with name and version number
        return('%s %s-%s ...' % (process, name, versionNumber()))
    elif addNumberD20 > 16:
        # Render with composite name and version number
        return('%s %s%s-%s ...' % (process, name, randint(0,9), versionNumber()))
    else:
        # Render with name only
        return('%s %s ...' % (process, name))

def versionNumber():
    """Generate a random version number."""
    return '%s.%s.%s' % (randint(0,9), randint(0,9), randint(0,9))

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
        message = '\n%s' % message

    return message

while True:
    print(instantProcess()),
    sleep(decimal.Decimal(randrange(300))/100),
    print(doneMessage())
