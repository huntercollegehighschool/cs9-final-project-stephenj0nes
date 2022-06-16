"""
Name(s): Stephen Jones, Katerina Vasyukevich 
Name of Project: Choose Your Adventure
"""

#Write the main part of your program here. Use of the other pages is optional.

alive = True 
dead = False

while alive:
  print("You wake up in a clearing in the middle of the woods  with no memory of how you got there. The sky is pitch black. Beside you is a note on the ground, and a lantern. Around you are two paths, one going left, the other right. ")
  print("Note: There is only one way out of the woods for each road. Stick to the path, and good luck!") 
  
  choice1 = input("You pick up the lantern. Which way do you go? (left/right) : ")
  if choice1 == 'right':
    print("You walk to the right. The path goes on and on, through rough terrain, and you feel a sharp, aching pain in your knee. You sit down, unable to walk any further. As you rest, you notice something. A pleasant smell, coupled with relaxing music seems to be coming from deep in the woods. ") 
    
    choice2 = input("Do you follow it? (follow it/stay where you are): ")
    if choice2 == 'stay where you are' or choice2 == 'stay':
      print("You aren’t going to risk it, deciding to rest your legs until you feel it's time to go. Once you rest up, you keep walking. ")
      print("Eventually, you reach a fork in the road. One direction goes left, the other right.")
      choice6 = input("Left or right? ")
      if choice6 == 'left':
        print("You begin to walk left. You feel a cold wind on your face, and see a break in the trees. You speed forward, but stop short right at the edge of a cliff. Relieved, you begin to look around. All of the sudden, you feel the ground shift beneath your feet. The part of the cliff that you’re on collapses, leaving you frantically grasping for something to hold on to. There's nothing there. You fall to your death. ")
      elif choice6 == 'right':
        print("You walk forwards. The dirt forest path slowly changes into a paved, cobblestone road. Around you, trees give way to farmhouses and fields. The sun reaches the horizon, and a golden pink glow illuminates your surroundings. You reach a sign in the middle of the road. 'Congrats!'' it reads, 'you’ve made it out'. ")
        break
      else:
        print("Whoops! It seems like you've mistyped something. Please be more careful next time, and remember to only use lowercase letters. Please restart the game. ")
        break
    elif choice2 == 'follow it':
      print("You realize just how hungry you’ve been. Unable to resist, you hobble your way off the path and into the woods. The sight that meets you doesn’t disappoint. A table, filled to the brim with all sorts of food and drink, and a phonograph playing soft jazz music. ") 
      choice3 = input("Eat the food/change the music: ")
      if choice3 == 'eat the food':
        print("You walk over to the table, and pick up an apple. Biting into it, you have never tasted a better one. You finish it, and then pick up another one. And another one. Then you take a piece of pie. Then the whole pie. You just can’t seem to stop eating. You don’t notice the shadows creeping out of the treeline towards you. You don’t notice the flame die out in your lantern. And by the time the shadow walks behind you, it's already too late. You die. ")
        break
      elif choice3 == 'change the music':
        print("Curious, you walk towards the record player. You see numerous other CDs lying beside it. You take the original one off, pausing the music. At that moment, the facade around you crumbles. You feel the hairs raise on the back of your neck, and you turn to see the table, now covered in bugs, and rotten food. You look around you to see hungry eyes watching you from behind the trees.")
        choice4 = input("Do you stand still or do you run? ")
        if choice4 == 'stand still':
          print("You freeze up, unable to move. You realize in horror that your lantern is on the other side of the table, but it's too late. The creatures have already surrounded you. You say a last prayer, as you feel the breath leave your lungs and you collapse. You died. ")
          break
        elif choice4 == 'run':
          print("You grab your lantern, and run back in the direction of the path. Luckily, your lantern is still lit, and seems to be keeping the things around you at bay, though they try to surround you. By the time your feet reach the path, they seem to have given up. Though you’re exhausted, you pick yourself up and walk forwards. ")
          print("Eventually, you reach a fork in the road. One direction goes left, the other right.")
          choice5 = input("Left or right? ")
          if choice5 == 'left':
            print("You begin to walk left. You feel a cold wind on your face, and see a break in the trees. You speed forward, but stop short right at the edge of a cliff. Relieved, you begin to look around. All of the sudden, you feel the ground shift beneath your feet. The part of the cliff that you’re on collapses, leaving you frantically grasping for something to hold on to. There's nothing there. You fall to your death. ")
          elif choice5 == 'right':
            print("You walk forwards. The dirt forest path slowly changes into a paved, cobblestone road. Around you, trees give way to farmhouses and fields. The sun reaches the horizon, and a golden pink glow illuminates your surroundings. You reach a sign in the middle of the road. 'Congrats!'it reads, 'you’ve made it out'. ")
          
          else:
            print("Whoops! It seems like you've mistyped something. Please be more careful next time, and remember to only use lowercase letters. Please restart the game.")
            break
        else:
           print("Whoops! It seems like you've mistyped something. Please be more careful next time, and remember to only use lowercase letters. Please restart the game.")
        break
      else:
         print("Whoops! It seems like you've mistyped something. Please be more careful next time, and remember to only use lowercase letters. Please restart the game.")
      break
    else:
      print("Whoops! It seems like you've mistyped something. Please be more careful next time, and remember to only use lowercase letters. Please restart the game.")
      break

  elif choice1 == 'left':
    print("You start walking left. The air is damp, and you feel the ground squelch beneath your feet. The ground becomes softer, until you realize you’re up to your knees in mud. You keep pushing through. As you trudge through the mud, you realize that you can’t move any further. You’re up to your waist are stuck in quicksand. ")
    choice7 = input("Do you give up or do you struggle? ")
    if choice7 == 'give up':
      print("You accept your fate. You realize however, that by remaining calm you’re given a bit more freedom of movement. You slowly distribute your weight, until your limbs are dispersed over the quicksand. You grab onto a nearby tree branch, and manage to pull yourself back. ")
      print("Close call, but you made it! Looking around you see that the southern path has led you into a swamp. The trees are crooked, their branches reaching out like claws. You can’t help but feel like you’re being watched by something, deep in the darkness around you. ")
      print("You square your shoulders, and walk further into the swamp. As you make your way through, you hear a low, rumbling growl to your left. You turn and find yourself face to face with a creature, shrinking in the darkness. It gave the impression of a furless, almost humanoid wolf like thing, but with your lanterns dim glow it was difficult to make out. Its pure black eyes stare at you threateningly. ")
      choice8 = input("Run away/intimidate it: ")
      if choice8 == 'run away':
        print("You stumble backwards, dropping your lantern. The light goes out, and you break off into a run, praying that whichever direction you’re going in is the right one. The creature chases after you. You hear its footsteps pounding behind you, until you trip over a branch, landing face first. You turn around, frantically, and the last thing you see is its gaping maw, filled with razor sharp teeth. It eats you. You died.  ")
        break
      elif choice8 == 'intimidate it':
        print("You decide that you could probably scare it off. It isn’t very big and you pray that it’ll turn tail and run. You step forward, and walk towards it, trying to look as intimidating as possible. Your lantern is swinging from your arm, and you notice that the creature is looking warily at it. You bring it in front of you, inching forward. Just as the light fully illuminates the beast, it yelps and runs off. You see that the creature was actually guarding something. A small box is on the ground. ")
        print("You open the box, finding a small brass key. You take the key.You walk forwards, back along the path. Eventually, the ground becomes more solid, and the trees more pleasant. You come across another fork in the road. One path goes straight forward, the other off to the right. ")
        choice9 = input("Which way do you go? (forward/right): ")
        if choice9 == 'right':
          print("You begin to walk right. The air begins to grow heavy, and sweat beads on your skin. You begin to feel tired, dazed by the heat. You don’t know how long you’ve been walking. A nap would be good right now. The ground is soft, and you want nothing more than to lie down. You collapse. You die.")
          break
        elif choice9 == 'forward':
          print("You continue on forwards. The path seems to go on forever, and you notice the faint light of dawn begin to break through the trees. Birds chirp in the trees around you. Finally, you come across a gate. You try to push it, but it’s locked. ")
          print("You use your key and you manage to open the gate. Congratulations! You've made it out.")
          break
        else: 
          print("Whoops! It seems like you've mistyped something. Please be more careful next time, and remember to only use lowercase letters. Please restart the game.")
          break
      else:
        print("Whoops! It seems like you've mistyped something. Please be more careful next time, and remember to only use lowercase letters. Please restart the game.")
        break
    elif choice7 == 'struggle':
      print("You struggle as you feel your body being pulled beneath the earth. Your efforts are futile, and you take a final gasp of air as your head is sucked in. You die.")
      break
    else:
      print("Whoops! It seems like you've mistyped something. Please be more careful next time, and remember to only use lowercase letters. Please restart the game.")
      break
  else:
    print("Whoops! It seems like you've mistyped something. Please be more careful next time, and remember to only use lowercase letters. Please restart the game.")
      
      
        
        
        
          


      
            
          
      
    

  
      

 

  
