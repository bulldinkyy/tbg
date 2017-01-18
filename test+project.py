Name = input('Name: ')

inventory = ['flashlight', 'one battery']
health = '75 HP'
stamina = '50 Speed'

Start = input('Are you read to start, %s? Y/N: ' % Name)

if Start == 'Y':
    print(Name, '||', inventory, '||', health, '||', stamina)
elif Start == 'N':
    quit()
else:
    print("That's not a command buddy pal.")


print("There was a story that some dude entered this house and never returned. There were multiple versions of this story, involving the man either comitting suicide, killing the people that entered or lived in the house, or he kept bodies in the walls. Your brave ass decided to see if any of these were true.")
print("With a flashlight, your dumbass decided to go inside. It was like an episode of Ghost Adventures. You started the second it was dark, and would leave at dawn. The only downside was the fact that you were gay and you didn't have anyone with you.")
print("You arrive to the house a flashlight in hand as well as a battery and a hairclip. What do you do?")

Choose = input("Option One: You decide to enter the house with some fear. You open the door to reveal a dark room. With that you turn the flashlight on. || Option Two: You decide to not go inside. Your sense were coming back and you did not want to risk it. ")

if Choose == 'One':
    del.inventory['flashlight']
    print("With the flashlight now turned on, you close the door behind you. Bad idea, %s. The light was going to be your guide from here on out. You decide to walk around the dark room.")
elif Choose == 'Two':
    quit()
else:
    print("What are you doing?")
