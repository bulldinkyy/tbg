Name = input('Name: ')

inventory = []
health = '75 HP'
stamina = '50 Speed'

Start = input('Are you ready to begin, %s? Y/N: ' % Name)

if Start == 'Y':
    print(Name, '||', inventory, '||', health, '||', stamina)
elif Start == 'N':
    quit()
else:
    print("That's not a command buddy pal.")
    start(Start)

print("How you entered the house is unknown. You questioned it yourself too. You woke up on the floor with three things beside you: a flashlight, a battery, and a paperclip.")
print("Your main objective is to exit the room without any sort of harm being done to you. You wanted to get out of there as quickly as possible. With three three things beside you, what do you reach over for?")
print(" → the paper clip")
print(" → the flashlight and the battery")
print(" → all of the items")
Choose = input('> ')
if Choose == 'the paper clip':
    inventory.append('the paper clip')
    print(Name, '||', inventory, '||', health, '||', stamina)
    print("You thought the paper clip would do. With this in your hand, you slowly stand up from your current spot on the floor and make your way towards the door. At least, attempt to by having the wall be your guide. Time to pick lock.")
elif Choose == 'the flashlight and the battery':
    inventory.append('flashlight')
    inventory.append('a battery')
    print(Name, '||', inventory, '||', health, '||', stamina)
    print("The light was now your guide. Getting up from your current spot, you turned the flashlight on and shine it on pretty much everything. The room wasn't decorated; it was completely empty which gave it a more eery vibe. You make your way towards the door in hope that the door was opened.") 
elif Choose == "all of the items":
    inventory.append('flashlight')
    inventory.append('a battery')
    inventory.append('paper clip')
    print(Name, '||', inventory, '||', health, '||', stamina)
    print("All of these items could be useful in their own way at one point. You turn the flashlight on and shine it on the room. The first thing that catches your attention is the door. You make your way towards it in hopes that it was already opened. If not, you would try and use your handy dandy paperclip.")
else:
    print("What?")
