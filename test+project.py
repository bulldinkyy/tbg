Name = input('Name: ')

inventory = []
health = '75 HP'
stamina = '50 Speed'

Start = input('Are you read to start, %s? Y/N: ' % Name)

if Start == 'Y' or 'Yes' or 'y' or 'yes':
    print(Name, '||', inventory, '||', health, '||', stamina)
elif Start == 'N' or 'n' or 'no' or 'No':
    quit()
else:
    input('Try again: ')
    
    
# Cool || things are for decoration.
# NOTE:
# Name might not be as useful for it isn't brought up in the game.
    
if Start or input == 'Y' or 'N':
  print("How you entered the house is unknown. You questioned it yourself too. You woke"
  ' up on the floor with three things beside you: a flashlight, a battery, and a' 
  " paperclip.")
  print("Your main objective is to exit the room without any sort of harm being done" 
  " to you. You wanted to get out of there as quickly as possible. With the three" 
  " things beside you, what do you reach over for?")
  print(" → 𝐭𝐡𝐞 𝐩𝐚𝐩𝐞𝐫 𝐜𝐥𝐢𝐩")
  print(" → 𝐭𝐡𝐞 𝐟𝐥𝐚𝐬𝐡𝐥𝐢𝐠𝐡𝐭 𝐚𝐧𝐝 𝐭𝐡𝐞 𝐛𝐚𝐭𝐭𝐞𝐫𝐲")
  print(" → 𝐚𝐥𝐥 𝐨𝐟 𝐭𝐡𝐞 𝐢𝐭𝐞𝐦𝐬")
  
Choose = input('> ')
if Choose == 'the paper clip':
    inventory.append('paper clip')
    print("𝐍𝐞𝐰 𝐢𝐭𝐞𝐦 𝐚𝐝𝐝𝐞𝐝 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐢𝐧𝐯𝐞𝐧𝐭𝐨𝐫𝐲!")
    print(Name, '||', inventory, '||', health, '||', stamina)
    print("What you thought the paper clip would do was your idea. With this in your" 
    " hand, you slowly stand up from your current spot on the floor and make your way" 
    " towards the door. At least, attempt to by having the wall be your guide. Time to" 
    " pick lock.")
elif Choose == 'the flashlight and the battery':
    inventory.append('flashlight')
    inventory.append('battery')
    print("𝐍𝐞𝐰 𝐢𝐭𝐞𝐦𝐬 𝐚𝐝𝐝𝐞𝐝 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐢𝐧𝐯𝐞𝐧𝐭𝐨𝐫𝐲!")
    print(Name, '||', inventory, '||', health, '||', stamina)
    print("The light was now your guide. Getting up from your current spot, you turned"
    " the flashlight on and shine it on pretty much everything. The room wasn't decorated;" 
    " it was completely empty which gave it a more eery vibe. You make your way towards the"
    " door in hope that the door was opened.") 
elif Choose == "all of the items":
    inventory.append('flashlight')
    inventory.append('battery')
    inventory.append('paper clip')
    print("𝐍𝐞𝐰 𝐢𝐭𝐞𝐦𝐬 𝐚𝐝𝐝𝐞𝐝 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐢𝐧𝐯𝐞𝐧𝐭𝐨𝐫𝐲!")
    print(Name, '||', inventory, '||', health, '||', stamina)
    print("All of these items could be useful in their own way at one point. You turn the" 
    " flashlight on and shine it on the room. The first thing that catches your attention is"
    " the door. You make your way towards it in hopes that it was already opened. If not," 
    " you would try and use your handy dandy paperclip.")
else:
  print("What?")
  input("Try again, buddy: ")
  
if Choose == 'the paper clip':
  print("Without the flashlight, you crouch down and rest your hand against the door." 
  " The other hand with the paperclip moves up to the doorknob. Of course it's going to" 
  " be a struggle to do this without a flashlight. Just as you were about to start, you" 
  " end up falling forward for the door ended up getting pushed open. Huh, that was useful,"
  " you think to yourself with a shake to the head. It was dim, but a flashlight wasn't exactly"
  " going to help. Standing up, you dust yourself off and go back to search.")
  del inventory[0]
  print("𝐈𝐭𝐞𝐦 𝐫𝐞𝐦𝐨𝐯𝐞𝐝 𝐟𝐫𝐨𝐦 𝐲𝐨𝐮𝐫 𝐢𝐧𝐯𝐞𝐧𝐭𝐨𝐫𝐲.")
  print("𝐑𝐞𝐚𝐬𝐨𝐧: 𝐘𝐨𝐮 𝐝𝐫𝐨𝐩𝐩𝐞𝐝 𝐢𝐭. 𝐎𝐫, 𝐝𝐞𝐞𝐦𝐞𝐝 𝐢𝐭 𝐮𝐬𝐞𝐥𝐞𝐬𝐬.")
  print(Name, '||', inventory, '||', health, '||', stamina)
elif Choose == "the flashlight and the battery" or "all of the items":
  print("You hope that the flashlight was the only thing that was needed right now."
  " Using the light, you make your way towards the door and hope the door was already"
  " opened. You give it a gentle push and alas, the door is open. With a sigh of relief,"
  " you search through the house.")

print("Going out the window didn't seem too bad. That is, if you wanted to injure" 
" yourself in someway. Breaking something was not on your agenda. Getting out of here" 
" safetly was. You decide to search the rooms with light possibly going through. Your"
" options are:")
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
  print("You decide to go to the door to your left. You didn't trust it; you didn't"
  " know the house like the back of your hand. For all you knew, a monster could be"
  " lurking behind it, or there could even be a dead body. Who knew what was behind"
  " door number one? It was your best option.")
  print("Hesitantly, you approach the door. Part of you wanted to run away and jump"
  " out some window. It seemed like a better plan, but this was a better way. Who knows," 
  " maybe they'll be something useful in there.")
if Option_Two == 'the door to your right':
  print("You decide to go to the door to your right. You didn't trust it; you didn't"
  " know the house like the back of your hand. For all you knew, a monster could be"
  " lurking behind it, or there could even be a dead body. Who knew what was behind"
  "door number two? It was your best option.")
  print("Hesitantly, you approach the door. Part of you wanted to run away and jump" 
  " out some window. It seemed like a better plan, but this was a better way. Who knows,"
  " maybe they'll be something useful in there.")
if Option_Three == 'the door ahead of you':
  print("You decide to go to the door right ahead of you. You didn't trust it; you" 
  "didn't know the house like the back of your hand. For all you knew, a monster could"
  " be lurking behind it, or there could even be a dead body. Who knew what was behind"
  "door number three? It was your best option.")
  print("Hesitantly, you approach the door. Part of you wanted to run away and jump out"
  " some window. It seemed like a better plan, but this was a better way. Who knows,"
  " maybe they'll be something useful in there.")

if a_list == ['flashlight', 'battery', 'paper clip'] or ['flashlight', 'battery']:
  if Door == 'the door to your left':
    print("Taking the flashlight out of your inventory / pocket, you turned it on. You"
    " were somewhat hesitant due to the fact that it might call the attention of something"
    " or someone. It was risk that you were willing to take. Who knew if the door room was"
    " was completely dark, or something along those lines. With the flashlight facing the floor,"
    " you place your hand on the door knob.")
    print("The door squeaks as you twisted the door knob and slowly push it open. You were"
    " hesitant to shine the light in the room, but you did.")
    print("Your light shines on every part of the room, getting every inch of it. The second"
    " it reaches the left corner of the room, a key is visible. You furrow your eyebrows"
    " before making your way closer to it. Do you pick it up?")
    Key = input('> ')
    if Key == 'Y' or 'Yes' or 'y' or 'yes':
      inventory.append('key')
      print("𝐍𝐞𝐰 𝐢𝐭𝐞𝐦 𝐚𝐝𝐝𝐞𝐝 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐢𝐧𝐯𝐞𝐧𝐭𝐨𝐫𝐲!")
      print(Name, '||', inventory, '||', health, '||', stamina)
      print("The key may be your way out. You were going to get out of here. You were going to be"
      " fine. However, you knew better. You exit the room without tripping over anything. You"
      " were calm and collective. At least, you were on the outside. On the inside, you were"
      " over the moon.")
      print("You turn your flashlight off. The dimly lit hallway was going to save you, and so" 
      " was this key. You look around, a slight grin on your lips. You make your way towards"
      " the main door. Using the key, you insert it in and unlock the door. Perfect.")
      if inventory == ['flashlight', 'battery', 'paper clip', 'key']:
        del inventory[3]
        print("GAME OVER")
        quit()
      elif inventory == ['flashlight', 'battery', 'key']:
        del inventory[2]
        print("GAME OVER")
        quit()
  elif Door == 'the door to your right':
    print("Absolutely nothing. It looked exactly like the first room, except there was nothing"
    " . The other room at least had a few things like the flashlight, the battery, and the"
    " paper clip. A sigh leaves your mouth and you scratch at the back of your neck. There was"
    " no hope for you. The floor boards squeak and you heart drops. You freeze. You want to"
    " turn around and see what it was, but you were just too scared. Great. Swallowing down" 
    " whatever fear you had, you ask one of the following: ")
    print(" → 1. Who are you? O-or what are you?")
    print(" → 2. What are you going to do with me?")
    print(" → 3. What do you want from me?")
    Speak = input('> ')
    if Speak == '1':
      print("Silence. You were genuinely hoping it was your weight that caused the creak rather"
      " than somebody else. The last thing you wanted to do was die in this forbidden place. Then"
      ", you get an answer. 'Ooh, introductions.' It was a goofy type of voice, a cartoonish one."
      " You couldn't make out if this was some guy or a female. 'My name is Jamie. Don't worry, %s"
      ", I already know who you are.' The fact this person knew your name made it worse. 'All you"
      " have to do is comply and you'll be out of here, okay?' You didn't respond. All you did was"
      " nod. If it wasn't for the sound of the floor boards coming closer to you, you would have"
      " felt somewhat better. Your heart was beating rapidly against your chest. Shivers were being"
      " sent down your spine. You hated this feeling. And you hated this entire situation you were"
      " in. Again, how did you even get here?" % Name)
      print("'A silent one, huh? I can work with that. It makes this much easier to do.' Instantly"
      ", you open your mouth to speak. 'What do you mean by that?' You couldn't see it, but 'Jamie',"
      " had a grin on their face. 'You'll see.' It was all they said. The boards make their"
      " infamous noise before it stops. You feel a presense behind you. What do you do?")
      print(" → 1. Fight back. It would be a struggle, but it was worth a shot.")
      print(" → 2. Let it happen. You had the energy, but it could be useful for a fight later on.")
      print(" → 3. Scream. It was worth a shot.")
      Action = input("> ")
      if Action == '1':
        print("You throw your head back, hitting said person in the face. It hurt your head. You"
        " were probably going to regret it due to the fact that a headache may come back. 'Fesity"
        "', the person breaths out as they take a step back. You were rubbing the back of your head"
        " which was the reason why arms went around your waist and you were thrown over someone's"
        " shoulder. You thrash and thrash before a hand meets your mouth followed by a cloth.")
        print("You try and fight it, but your eyes begin to feel heavy. . .")
        print("GAME OVER")
      elif Action == '2':
        print("You didn't do anything. It took Jamie by surprise, but it just made things easier."
        " 'Just like that,' Jamie murmurs. Before you knew it, a cloth was put over your mouth and"
        " nose. Your eyes feel heavy and you didn't feel anything after that. But, you did hear"
        " 'You'll be out, promise.'")
        print("GAME OVER")
      elif Action == '3':
        print("You scream. You scream as loud as you possibly can to the point where you would"
        " end up with a sore throat. You hoped someone would hear you, but the chances were very"
        " slim. It doesn't help at all. If anything, it makes your situation worse. A smelly cloth"
        " gets put over your nose and your mouth. You were out.")
        print("GAME OVER")
    if Speak == '2' or '3':
      if '2':
        print("'What am I going to do with you?' The person stays silent for a moment. 'This isn't a"
        " horror game for nothing, right? I think you know what's going to happen.' It was the sad"
        " truth. Fourth wall breaking, am I right? 'You keep it to yourself. Just comply and we'll get"
        " through this, okay? What do you do:")
        print(" → 1. Fight back. It would be a struggle, but it was worth a shot.")
        print(" → 2. Let it happen. You had the energy, but it could be useful for a fight later on.")
        print(" → 3. Scream. It was worth a shot.")
      elif '3':
        print("'What do I want from you?' The person stays silent for a moment. 'This isn't a"
        " horror game for nothing, right? I think you know what's going to happen.' It was the sad"
        " truth. Fourth wall breaking, am I right? 'You keep it to yourself. Just comply and we'll get"
        " through this, okay? What do you do:")
        print(" → 1. Fight back. It would be a struggle, but it was worth a shot.")
        print(" → 2. Let it happen. You had the energy, but it could be useful for a fight later on.")
        print(" → 3. Scream. It was worth a shot.")
        
        Action = input("> ")
        if Action == '1':
          print("You throw your head back, hitting said person in the face. It hurt your head. You"
          " were probably going to regret it due to the fact that a headache may come back. 'Fesity"
          "', the person breaths out as they take a step back. You were rubbing the back of your head"
          " which was the reason why arms went around your waist and you were thrown over someone's"
          " shoulder. You thrash and thrash before a hand meets your mouth followed by a cloth.")
          print("You try and fight it, but your eyes begin to feel heavy. . .")
          print("GAME OVER")
          quit()
        elif Action == '2':
          print("You didn't do anything. It took Jamie by surprise, but it just made things easier."
          " 'Just like that,' Jamie murmurs. Before you knew it, a cloth was put over your mouth and"
          " nose. Your eyes feel heavy and you didn't feel anything after that. But, you did hear"
          " 'You'll be out, promise.'")
          print("GAME OVER")
          quit()
        elif Action == '3':
          print("You scream. You scream as loud as you possibly can to the point where you would"
          " end up with a sore throat. You hoped someone would hear you, but the chances were very"
          " slim. It doesn't help at all. If anything, it makes your situation worse. A smelly cloth"
          " gets put over your nose and your mouth. You were out.")
          print("GAME OVER")
          quit()
  elif Door == 'the door ahead of you':
    print("There was a smell and there was also the occasional fly passing by you. Deep down,"
    " you know what was there. You didn't want to admit it, though. It would be your way of"
    " keeping yourself calm and collective rather than uneasy and all over the place. Maybe"
    " it was something rottening. Like- like meat or food. Hesitantly, you decide to shine"
    " the flashlight on the place it was coming from. It was a body. You wanted to puke, and" 
    " maybe cry a little. Maggots were coming in and out of it, flies flew around. You could"
    " have sworn you heard a mouse squeak.")
    print("'That's going to be you', a voice calls out. You're startled. You're shaking. You"
    " might have peed a little. You didn't know if that did happen and you didn't know if you"
    " who's voice was that. You didn't know if this was prank. But, you did know one thing:"
    " you were going to die in here and look exactly like that body. You're silent for a"
    " moment before speaking.")
    print(" → 1. Who are you?")
    print(" → 2. Is this a prank? Please tell me this is a prank.")
    print(" → 3. No. That's going to be you.")
    Answer = input('> ')
    if Answer == '1':
      print("'It's a little too late for introductions. . . But, my name is Jamie."
      " You don't need to tell me yours. I've already got it %s.' You were shook."
      " Were they the one that brought you here? How did they know your name? How"
      " did you even get into this mess in the first place? It was all so confusing." % Name)
      print("'I really would love to stay and chit-chat, but time's a tickin' and I"
      " really have to make you look something like Lumps over there. We can do this"
      " the easy way, or the hard way. Your pick.")
      print('TYPE IN EASY WAY OR HARD WAY')
      EasyOrHard = input('> ')
      if EasyOrHard == 'easy way':
        print("Jamie nods their head and they approach you. You weren't going to put"
        " up a fight. What's the point? Any last words?")
        YourLastWords = input('> ')
        print("GAME OVER")
        quit()
      elif EasyorHard == 'hard way':
        print("'A fighter, huh?' Jamie purses their lips before nodding their head. I"
        " can work with that. I like a challenge.' The end was near and the best thing"
        " you can do is turn around, pull the battery out and chuck it at Jamie.")
        del inventory[1]
        print(Name, '||', inventory)
        print("'Ow!' They cry out, rubbing at their forehead. While that had happened, you"
        " ran. You ran as fast as you can. Home. Think of home, $s. Think of home. You were"
        " a fighter. And as a fighter, you were going to get out. You were silent as you opened"
        " a door. You closed it and acted as though it wasn't open. Your back presses up against"
        " the wall near the door and you suck your stomach in. You're absolutely silent as you"
        " you listen for any movement outside. 'Come out, come out wherever you are. . .'")
        print("GAME OVER")
    elif Answer == '2':
      print("You refused to believe that this was actually happening. You thought it"
      " it was your mind playing tricks on you. Or, it was your friend that simply" 
      " put that Party City blood on a dummy and they stuffed it with meat and maggots"
      " which would explain the flies. So on, and so forth. But, it was real. That was"
      " a real body. This was no prank. This was no trick. You were here. This was real.")
      print("'Telling you this is a prank will only bring your hopes up. And when I"
      " say you'll become exactly like that, I mean it.' This person was insane." 
      " Could you even consider them a person with how this entire thing was playing"
      " out? Just as you were about to open your mouth to speak, they beat you to it."
      " 'We can either do this the very easy way or the hard way. Which would you"
      " 'prefer?'")
      print(" → 1 'The easy way'. You were going to fight.")
      print(" → 2 'The hard way. I would very much like to live.'")
      print(" → 3 Silence.")
      Response = input("> ")
      if Response == '1':
        print("'That's what I like to hear', they say. If it wasn't for you refusing"
        " to turn around and face the horror, you would have seen the grin on their"
        " face. Just as they were about to approach you, you were quick to throw the"
        " flashlight in their direction. If it hit them, you didn't know. But, you"
        " had no source of light.")
        del inventory[0]
        print(Name, '||', inventory)
        print("'That's not nice!' The person yells, shaking their head in the process."
        " You tried to be as silent as possible as well as trying to make your way"
        " through the darkness without creating a shadow. It was silence on your part,"
        " but you bumped right into a figure. Great. 'Hard way it is,' said person mumbles"
        " as they pick you up without a struggle. Screams try to come out from your mouth,"
        ", but they become muffled with their dirty hand going over your mouth. 'You're just"
        " making it worse for yourself'.")
        print("GAME OVER")
        quit()
      elif Response == '2':
        print("'That's not an answer I'm used to hearing,' the creep muses with a"
        " chuckle. 'But, there's always time for new things, right?' As if you were"
        " going to respond to that. Just as they approach you, you run. You hold"
        " your flashlight as tight as you can and you run. You need to get out. If it"
        " meant jumping out of a window, so be it. You simply wanted to get out and"
        " never come back to this looney bin. But because you were running, it"
        " allowed the person to go after you and it had you stamina draining. Plus,"
        " who said you knew this house?")
        stamina = '25 speed'
        print(Name, '||', stamina)
        print("'You're making this worse for yourself, kid!' The person yells out,"
        " clearly irritated with your shenanigans. At least, they were shenanigans"
        " to them. To you, it was called survival. But, by the time you came to a stop"
        ", it was over for you. You were tired. Your legs gave up, your lungs felt like"
        " they were on fire, and your heart was beating rapdily against your chest. This"
        " was not the way you wanted to die. Then again, you didn't want to die. Not now."
        " 'Told you,' the person says as they approach your trapped figure. With the light"
        " shining on them, you got a somewhat clearer image of them. Dirty, ragged clothing,"
        " messy hair. Eyes that looked souless. Late thirties, early forties. 'Any last words?'")
        LastWord = input('> ')
        print("GAME OVER")
        quit()
      elif Response == '3':
        print("It just made it easier for the person to get you. You were shook."
        " You dropped your flashlight and with that, you were a goner.")
        print("GAME OVER")
        quit()
      
if a_list == []:
  if Door == 'the door to your left':
    print("You had nothing. You were regretting your previous choices and despite the"
    " temptation of going back, your place was to get out. Plus, you might not get caught with"
    " the fact that you didn't have anything bright attracting to you. You place your hand on"
    "the door knob.")
    print("You were an idiot for not picking up the flashlight. Why did you think a paper"
    " clip was useful in a case like this? In some way, it was. But, you ended up losing the"
    " darn thing. You did exactly what you did to get out of the first room; run your hand"
    " along the wall and walk around slowly. Your feet were helping out too. It was slow, but"
    " you were being careful. Who knows; there could be some sort of puddle. You get to the"
    " left corner of the room. At least, you THINK it's the left. Your step on something"
    " hard. Slowly, you crouch down and replace your foot with your hand. You fingers touch"
    " said item. It's cold and it feels like a key. Do you pick it up?")
    Key = input('> ')
    
    if Key == 'Y' or 'Yes' or 'y' or 'yes':
      inventory.append('key')
      print("𝐍𝐞𝐰 𝐢𝐭𝐞𝐦 𝐚𝐝𝐝𝐞𝐝 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐢𝐧𝐯𝐞𝐧𝐭𝐨𝐫𝐲!")
      print(Name, '||', inventory, '||', health, '||', stamina)
      print("The key may be your way out. You were going to get out of here. You were going to be"
      " fine. However, you knew better. You exit the room without tripping over anything. You"
      " were calm and collective. At least, you were on the outside. On the inside, you were"
      " over the moon.")
      del inventory[0]
      print("GAME OVER")
      quit()
  elif Door == 'the door to right':
    print("You did your previous tactic with the first room. The wall is your guide. You"
    " didn't need any flashlight, right? You use your feet as some sort of stick and move"
    " around it to get a feel for what's on the ground. You do this maybe two times before"
    " moving your way towards most of the room. Nothing. Your brows furrow and you shake your"
    " head in disappointment. Amazing. The floor boards creak and you shake your head. You"
    " were hoping it was your weight rather than it being something or someone. But just to be"
    " sure, you open your mouth to speak.")
    print(" → Who are you? O-or what are you?")
    print(" → What are you going to do with me?")
    print(" → What do you want from me?")
    Speak = input('> ')
    if Speak == '1':
      print("Silence. You were genuinely hoping it was your weight that caused the creak rather"
      " than somebody else. The last thing you wanted to do was die in this forbidden place. Then"
      ", you get an answer. 'Ooh, introductions.' It was a goofy type of voice, a cartoonish one."
      " You couldn't make out if this was some guy or a female. 'My name is Jamie. Don't worry, %s"
      ", I already know who you are.' The fact this person knew your name made it worse. 'All you"
      " have to do is comply and you'll be out of here, okay?' You didn't respond. All you did was"
      " nod. If it wasn't for the sound of the floor boards coming closer to you, you would have"
      " felt somewhat better. Your heart was beating rapidly against your chest. Shivers were being"
      " sent down your spine. You hated this feeling. And you hated this entire situation you were"
      " in. Again, how did you even get here?" % Name)
      print("'A silent one, huh? I can work with that. It makes this much easier to do.' Instantly"
      ", you open your mouth to speak. 'What do you mean by that?' You couldn't see it, but 'Jamie',"
      " had a grin on their face. 'You'll see.' It was all they said. The boards make their"
      " infamous noise before it stops. You feel a presense behind you. What do you do?")
      print(" → 1. Fight back. It would be a struggle, but it was worth a shot.")
      print(" → 2. Let it happen. You had the energy, but it could be useful for a fight later on.")
      print(" → 3. Scream. It was worth a shot.")
      Action = input("> ")
      if Action == '1':
        print("You throw your head back, hitting said person in the face. It hurt your head. You"
        " were probably going to regret it due to the fact that a headache may come back. 'Fesity"
        "', the person breaths out as they take a step back. You were rubbing the back of your head"
        " which was the reason why arms went around your waist and you were thrown over someone's"
        " shoulder. You thrash and thrash before a hand meets your mouth followed by a cloth.")
        print("You try and fight it, but your eyes begin to feel heavy. . .")
        print("GAME OVER")
        quit()
      elif Action == '2':
        print("You didn't do anything. It took Jamie by surprise, but it just made things easier."
        " 'Just like that,' Jamie murmurs. Before you knew it, a cloth was put over your mouth and"
        " nose. Your eyes feel heavy and you didn't feel anything after that. But, you did hear"
        " 'You'll be out, promise.'")
        print("GAME OVER")
        quit()
      elif Action == '3':
        print("You scream. You scream as loud as you possibly can to the point where you would"
        " end up with a sore throat. You hoped someone would hear you, but the chances were very"
        " slim. It doesn't help at all. If anything, it makes your situation worse. A smelly cloth"
        " gets put over your nose and your mouth. You were out.")
        print("GAME OVER")
        quit()
        
    elif Speak == '2':
      print("'What am I going to do with you?' The person stays silent for a moment. 'This isn't a"
      " horror game for nothing, right? I think you know what's going to happen.' It was the sad"
      " truth. Fourth wall breaking, am I right? 'You keep it to yourself. Just comply and we'll get"
      " through this, okay? What do you do:")
      print(" → 1 Fight back. It would be struggle, but it was worth a shot.")
      print(" → 2. Let it happen. You had the energy, but it could be useful for a fight later on.")
      print(" → 3. Scream. It was worth a shot.")
      Action = input("> ")
      if Action == '1':
        print("You throw your head back, hitting said person in the face. It hurt your head. You"
        " were probably going to regret it due to the fact that a headache may come back. 'Fesity"
        "', the person breaths out as they take a step back. You were rubbing the back of your head"
        " which was the reason why arms went around your waist and you were thrown over someone's"
        " shoulder. You thrash and thrash before a hand meets your mouth followed by a cloth.")
        print("You try and fight it, but your eyes begin to feel heavy. . .")
        print("GAME OVER")
        quit()
      elif Action == '2':
        print("You didn't do anything. It took Jamie by surprise, but it just made things easier."
        " 'Just like that,' Jamie murmurs. Before you knew it, a cloth was put over your mouth and"
        " nose. Your eyes feel heavy and you didn't feel anything after that. But, you did hear"
        " 'You'll be out, promise.'")
        print("GAME OVER")
        quit()
      elif Action == '3':
        print("You scream. You scream as loud as you possibly can to the point where you would"
        " end up with a sore throat. You hoped someone would hear you, but the chances were very"
        " slim. It doesn't help at all. If anything, it makes your situation worse. A smelly cloth"
        " gets put over your nose and your mouth. You were out.")
        print("GAME OVER")
        quit()

    elif Speak == '3':
      print("'What do I want from you?' The person stays silent for a moment. 'This isn't a"
      " horror game for nothing, right? I think you know what's going to happen.' It was the sad"
      " truth. Fourth wall breaking, am I right? 'You keep it to yourself. Just comply and we'll get"
      " through this, okay? What do you do:")
      print(" → 1. Fight back. It would be a struggle, but it was worth a shot.")
      print(" → 2. Let it happen. You had the energy, but it could be useful for a fight later on.")
      print(" → 3. Scream. It was worth a shot.")
      Action = input("> ")
      if Action == '1':
        print("You throw your head back, hitting said person in the face. It hurt your head. You"
        " were probably going to regret it due to the fact that a headache may come back. 'Fesity"
        "', the person breaths out as they take a step back. You were rubbing the back of your head"
        " which was the reason why arms went around your waist and you were thrown over someone's"
        " shoulder. You thrash and thrash before a hand meets your mouth followed by a cloth.")
        print("You try and fight it, but your eyes begin to feel heavy. . .")
        print("GAME OVER")
        quit()
      elif Action == '2':
        print("You didn't do anything. It took Jamie by surprise, but it just made things easier."
        " 'Just like that,' Jamie murmurs. Before you knew it, a cloth was put over your mouth and"
        " nose. Your eyes feel heavy and you didn't feel anything after that. But, you did hear"
        " 'You'll be out, promise.'")
        print("GAME OVER")
        quit()
      elif Action == '3':
        print("You scream. You scream as loud as you possibly can to the point where you would"
        " end up with a sore throat. You hoped someone would hear you, but the chances were very"
        " slim. It doesn't help at all. If anything, it makes your situation worse. A smelly cloth"
        " gets put over your nose and your mouth. You were out.")
        print("GAME OVER")
        quit()
  elif Door == 'the door ahead of you':
    print("The wall is your guide, your dominant foot is your stick. You were going to feel"
    " your way around a room once more. This was simply an intense game of dark 'hide 'n' go"
    " seek'. You do this twice between making your way towards the center of the room. This"
    " was like ice-skating: you didn't want to seperate yourself from the wall. The wall was"
    " helpful while the center was scary. But, if you were to going to learn, you needed to"
    " take risks. Your feet meet something and you furrow your eyebrows. It felt squishy"
    " underneath your foot. But maybe it was something useful, right? You crouch down slowly"
    " and your hand presses against said thing. Your hand moves around and the second it"
    " reaches a certain area, you instantly pull your hand back. Your hand's covered in"
    " something that feels sticky and there's all the sound of flies going pass your ear.")
    print("'That's going to be you,' a voice calls out. It sounded nearby, but also distant."
    " But because it was startling, you nearly fell back. You keep your balance before standing"
    " up. Your hand wipes against your thigh and you open your mouth to speak.")
    print(" → Who are you?")
    print(" → Is this a prank? Please tell me this is a prank.")
    Answer = input('> ')
    if Answer == '1':
      print("'It's a little too late for introductions. . . But, my name is Jamie."
      " You don't need to tell me yours. I've already got it $s.' You were shook."
      " Were they the one that brought you here? How did they know your name? How"
      " did you even get into this mess in the first place? It was all so confusing." % Name)
      print("'I really would love to stay and chit-chat, but time's a tickin' and I"
      " really have to make you look something like Lumps over there. We can do this"
      " the easy way, or the hard way. Your pick.")
      print('TYPE IN EASY WAY OR HARD WAY')
      EasyOrHard = input('> ')
      if EasyOrHard == 'easy way':
        print("Jamie nods their head and they approach you. You weren't going to put"
        " up a fight. What's the point? Any last words?")
        YourLastWords = input('> ')
        print("GAME OVER")
        quit()
      elif EasyOrHard == 'hard way':
        print("'A fighter, huh?' Jamie purses their lips before nodding their head. I"
        " can work with that. I like a challenge.' The end was near and the best thing"
        " you can do is turn around, go pass them, and run.")
        stamina = 24
        print(Name, '||', inventory)
        print("'Hey' They cry out, rubbing at their forehead. While that had happened, you"
        " ran. You ran as fast as you can. Home. Think of home, $s. Think of home. You were"
        " a fighter. And as a fighter, you were going to get out. You were silent as you opened"
        " a door. You closed it and acted as though it wasn't open. Your back presses up against"
        " the wall near the door and you suck your stomach in. You're absolutely silent as you"
        " you listen for any movement outside. 'Come out, come out wherever you are. . .'")
        print("GAME OVER")
    elif Answer == '2':
      print("You refused to believe that this was actually happening. You thought it"
      " it was your mind playing tricks on you. Or, it was your friend that simply" 
      " put that Party City blood on a dummy and they stuffed it with meat and maggots"
      " which would explain the flies. So on, and so forth. But, it was real. That was"
      " a real body. This was no prank. This was no trick. You were here. This was real.")
      print("'Telling you this is a prank will only bring your hopes up. And when I"
      " say you'll become exactly like that, I mean it.' This person was insane." 
      " Could you even consider them a person with how this entire thing was playing"
      " out? Just as you were about to open your mouth to speak, they beat you to it."
      " 'We can either do this the very easy way or the hard way. Which would you"
      " 'prefer?'")
      print(" → 1 'The easy way'. You were going to fight.")
      print(" → 2 'The hard way. I would very much like to live.'")
      print(" → 3 Silence.")
      Response = input("> ")
      if Response == '1':
        print("'That's what I like to hear', they say. If it wasn't for you refusing"
        " to turn around and face the horror, you would have seen the grin on their"
        " face. Just as they were about to approach you, you were quick to elbow them"
        " in the face.")
        print("'That's not nice!' The person yells, shaking their head in the process."
        " You tried to be as silent as possible as well as trying to make your way"
        " through the darkness without creating a shadow. It was silence on your part,"
        " but you bumped right into a figure. Great. 'Hard way it is,' said person mumbles"
        " as they pick you up without a struggle. Screams try to come out from your mouth,"
        ", but they become muffled with their dirty hand going over your mouth. 'You're just"
        " making it worse for yourself'.")
        print("GAME OVER")
        quit()
      elif Response == '2':
        print("'That's not an answer I'm used to hearing,' the creep muses with a"
        " chuckle. 'But, there's always time for new things, right?' As if you were"
        " going to respond to that. Just as they approach you, you run. You need to"
        "get out. If it meant jumping out of a window, so be it. You simply wanted"
        "to get out and never come back to this looney bin. But because you were"
        "running, it allowed the person to go after you and it had you stamina"
        "draining. Plus, who said you knew this house?")
        stamina = '25 speed'
        print(Name, '||', stamina)
        print("'You're making this worse for yourself, kid!' The person yells out,"
        " clearly irritated with your shenanigans. At least, they were shenanigans"
        " to them. To you, it was called survival. But, by the time you came to a stop"
        ", it was over for you. You were tired. Your legs gave up, your lungs felt like"
        " they were on fire, and your heart was beating rapdily against your chest. This"
        " was not the way you wanted to die. Then again, you didn't want to die. Not now."
        " 'Told you,' the person says as they approach your trapped figure. With the light"
        " shining on them, you got a somewhat clearer image of them. Dirty, ragged clothing,"
        " messy hair. Eyes that looked souless. Late thirties, early forties. 'Any last words?'")
        LastWord = input('> ')
        print("GAME OVER")
        quit()
      elif Response == '3':
        print("It just made it easier for the person to get you. You were shook."
        " You were a goner.")
        print("GAME OVER")
        quit()
