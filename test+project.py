Name = input('Name: ')

inventory = []
health = '75 HP'
stamina = '50 Speed'

Start = input('Are you read to start, %s? Y/N: ' % Name)

if Start == 'Y':
    print(Name, '||', inventory, '||', health, '||', stamina)
elif Start == 'N':
    quit()
else:
    input('Try again: ')
    
if Start or input == 'Y' or 'N':
  print("How you entered the house is unknown. You questioned it yourself too. You woke up on the floor with three things beside you: a flashlight, a battery, and a paperclip.")
  print("Your main objective is to exit the room without any sort of harm being done to you. You wanted to get out of there as quickly as possible. With the three things beside you, what do you reach over for?")
  print(" → 𝐭𝐡𝐞 𝐩𝐚𝐩𝐞𝐫 𝐜𝐥𝐢𝐩")
  print(" → 𝐭𝐡𝐞 𝐟𝐥𝐚𝐬𝐡𝐥𝐢𝐠𝐡𝐭 𝐚𝐧𝐝 𝐭𝐡𝐞 𝐛𝐚𝐭𝐭𝐞𝐫𝐲")
  print(" → 𝐚𝐥𝐥 𝐨𝐟 𝐭𝐡𝐞 𝐢𝐭𝐞𝐦𝐬")
else:
  print(Start)

Choose = input('> ')
if Choose == 'the paper clip':
    inventory.append('the paper clip ')
    print("𝐍𝐞𝐰 𝐢𝐭𝐞𝐦 𝐚𝐝𝐝𝐞𝐝 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐢𝐧𝐯𝐞𝐧𝐭𝐨𝐫𝐲!")
    print(Name, '||', inventory, '||', health, '||', stamina)
    print("What you thought the paper clip would do was your idea. With this in your hand, you slowly stand up from your current spot on the floor and make your way towards the door. At least, attempt to by having the wall be your guide. Time to pick lock.")
elif Choose == 'the flashlight and the battery':
    inventory.append('flashlight')
    inventory.append('battery')
    print("𝐍𝐞𝐰 𝐢𝐭𝐞𝐦𝐬 𝐚𝐝𝐝𝐞𝐝 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐢𝐧𝐯𝐞𝐧𝐭𝐨𝐫𝐲!")
    print(Name, '||', inventory, '||', health, '||', stamina)
    print("The light was now your guide. Getting up from your current spot, you turned the flashlight on and shine it on pretty much everything. The room wasn't decorated; it was completely empty which gave it a more eery vibe. You make your way towards the door in hope that the door was opened.") 
elif Choose == "all of the items":
    inventory.append('flashlight')
    inventory.append('battery')
    inventory.append('paper clip')
    print("𝐍𝐞𝐰 𝐢𝐭𝐞𝐦𝐬 𝐚𝐝𝐝𝐞𝐝 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐢𝐧𝐯𝐞𝐧𝐭𝐨𝐫𝐲!")
    print(Name, '||', inventory, '||', health, '||', stamina)
    print("All of these items could be useful in their own way at one point. You turn the flashlight on and shine it on the room. The first thing that catches your attention is the door. You make your way towards it in hopes that it was already opened. If not, you would try and use your handy dandy paperclip.")
else:
  print("What?")
  input("Try again, buddy: ")
  
if Choose == 'the paper clip':
  print("Without the flashlight, you crouch down and rest your hand against the door. The other hand with the paperclip moves up to the doorknob. Of course it's going to be a struggle to do this without a flashlight. Just as you were about to start, you end up falling forward for the door ended up getting pushed open. 𝘏𝘶𝘩, 𝘵𝘩𝘢𝘵 𝘸𝘢𝘴 𝘶𝘴𝘦𝘧𝘶𝘭, you think to yourself with a shake to the head. It was dim, but a flashlight wasn't exactly going to help. Standing up, you dust yourself off and go back to search.")
  del inventory[0]
  print("𝐈𝐭𝐞𝐦 𝐫𝐞𝐦𝐨𝐯𝐞𝐝 𝐟𝐫𝐨𝐦 𝐲𝐨𝐮𝐫 𝐢𝐧𝐯𝐞𝐧𝐭𝐨𝐫𝐲.")
  print("𝐑𝐞𝐚𝐬𝐨𝐧: 𝐘𝐨𝐮 𝐝𝐫𝐨𝐩𝐩𝐞𝐝 𝐢𝐭. 𝐎𝐫, 𝐝𝐞𝐞𝐦𝐞𝐝 𝐢𝐭 𝐮𝐬𝐞𝐥𝐞𝐬𝐬.")
  print(Name, '||', inventory, '||', health, '||', stamina)
elif Choose == "the flashlight and the battery" or "all of the items":
  print("You hope that the flashlight was the only thing that was needed right now. Using the light, you make your way towards the door and hope the door was already opened. You give it a gentle push and alas, the door is open. With a sigh of relief, you search through the house.")

print("Going out the window didn't seem too bad. That is, if you wanted to injure yourself in someway. Breaking something was not on your agenda. Getting out of here safetly was. You decide to search the rooms with light possibly going through. Your options are:")
print(" → 𝐭𝐡𝐞 𝐝𝐨𝐨𝐫 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐥𝐞𝐟𝐭")
print(" → 𝐭𝐡𝐞 𝐝𝐨𝐨𝐫 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐫𝐢𝐠𝐡𝐭")
print(" → 𝐭𝐡𝐞 𝐝𝐨𝐨𝐫 𝐚𝐡𝐞𝐚𝐝 𝐨𝐟 𝐲𝐨𝐮")

Door = input("> ")

if Door == 'the door to your left':
  print(Name, '||', inventory)
elif Door == 'the door to your right':
  print(Name, '||', inventory)
elif Door == 'the door ahead of you':
  print(Name, '||', inventory)
else: 
  print("What are you doing? Try again: ")
  
Option_One = Door
Option_Two = Door
Option_Three = Door

a_list = inventory

if Option_One == 'the door to your left':
  print("You decide to go to the door to your left. You didn't trust it; you didn't know the house like the back of your hand. For all you knew, a monster could be lurking behind it, or there could even be a dead body. Who knew what was behind door number one? It was your best option.")
if Option_Two == 'the door to your right':
  print("You decide to go to the door to your right. You didn't trust it; you didn't know the house like the back of your hand. For all you knew, a monster could be lurking behind it, or there could even be a dead body. Who knew what was behind door number two? It was your best option.")
if Option_Three == 'the door ahead of you':
  print("You decide to go to the door right ahead of you. You didn't trust it; you didn't know the house like the back of your hand. For all you knew, a monster could be lurking behind it, or there could even be a dead body. Who knew what was behind door number three? It was your best option.")
  
if Option_One == 'the door to your left' and a_list == ['flashlight', 'battery', 'paper clip']:
  print("u")
elif Option_One == 'the door to your left' and a_list == ['flashlight', 'battery']:
  print("x")
elif Option_One == 'the door to your left' and a_list == []:
  print("l")

if Option_Two == 'the door to your right' and a_list == ['flashlight', 'battery', 'paper clip']:
  print("Testing")
elif Option_Two == 'the door to your right' and a_list == ['flashlight', 'battery']:
  print("H")
elif Option_Two == 'the door to your right' and a_list == []:
  print("L")

if Option_Three == 'the door ahead of you' and a_list == ['flashlight', 'battery', 'paper clip']:
  print('J')
elif Option_Three == 'the door ahead of you' and a_list == ['flashlight', 'battery']:
  print('M')
elif Option_Three == 'the door ahead of you' and a_list == []:
  print('Yes')
