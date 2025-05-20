# Adventure Game: Alien Planet Exploration
# This game takes you on an adventure on an alien planet with three levels of choices.
# Creativity: Added vivid descriptions and a scenario with three plant choices for extra variety.

print("You have just landed on an alien planet. In the distance, you see a mysterious structure, and nearby, there are some unusual plants. Do you want to INVESTIGATE the structure or EXAMINE the plants?")
choice1 = input().strip().lower()

if choice1 == "investigate":
    print("You approach the structure and find a large door that seems locked. Do you want to use a TOOL or your STRENGTH to try to force it open?")
    choice2 = input().strip().lower()
    
    if choice2 == "tool":
        print("You pull out a tool from your spaceship. Do you PRY the door open or CUT through it?")
        choice3 = input().strip().lower()
        if choice3 == "pry":
            print("You pry open the door and find a room full of ancient alien artifacts. You’ve discovered a great treasure! The end.")
        elif choice3 == "cut":
            print("You cut through the door, but it triggers an alarm. You escape back to the spaceship as drones chase you. The end.")
        else:
            print("Invalid choice. Game over.")
    
    elif choice2 == "strength":
        print("You brace yourself to use your strength. Do you PUSH the door or KICK it?")
        choice3 = input().strip().lower()
        if choice3 == "push":
            print("You push with all your might, but the door doesn’t budge. Exhausted, you return to the spaceship. The end.")
        elif choice3 == "kick":
            print("You kick the door, and it cracks open slightly, revealing a dark tunnel. You explore it and find glowing crystals. The end.")
        else:
            print("Invalid choice. Game over.")
    
    else:
        print("Invalid choice. Game over.")

elif choice1 == "examine":
    print("You decide to examine the unusual plants. There are three plants that catch your attention: a red one, a blue one, and a green one. Which one do you want to pick? (RED, BLUE, or GREEN)")
    choice2 = input().strip().lower()
    
    if choice2 == "red":
        print("You pick the red plant, and it starts glowing brightly. Do you DROP it or KEEP holding it?")
        choice3 = input().strip().lower()
        if choice3 == "drop":
            print("You drop the plant, and it explodes in a burst of light, blinding you temporarily. You stumble back to the spaceship. The end.")
        elif choice3 == "keep":
            print("You keep holding the plant, and it communicates telepathically, teaching you the planet’s history. The end.")
        else:
            print("Invalid choice. Game over.")
    
    elif choice2 == "blue":
        print("You pick the blue plant, and it releases a sweet fragrance. Do you SMELL it closely or PUT it in your pocket?")
        choice3 = input().strip().lower()
        if choice3 == "smell":
            print("You smell the plant, and it makes you dizzy. You wake up in the spaceship with no memory of what happened. The end.")
        elif choice3 == "put":
            print("You put the plant in your pocket. Later, it heals a cut you didn’t notice. The end.")
        else:
            print("Invalid choice. Game over.")
    
    elif choice2 == "green":
        print("You pick the green plant, and it feels slimy. Do you TASTE it or THROW it away?")
        choice3 = input().strip().lower()
        if choice3 == "taste":
            print("You taste the plant, and it’s poisonous. You rush back to the spaceship, feeling sick. The end.")
        elif choice3 == "throw":
            print("You throw it away, and it releases spores that attract insects. You run to the spaceship to escape. The end.")
        else:
            print("Invalid choice. Game over.")
    
    else:
        print("Invalid choice. Game over.")

else:
    print("Invalid choice. Game over.")