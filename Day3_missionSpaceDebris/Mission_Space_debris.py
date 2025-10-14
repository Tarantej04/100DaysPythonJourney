import random

print("MISSION : SPACE DEBRIS ☄️")
print(r'''
             .       .                   .       .      .     .      .
            .    .         .    .            .     ______
        .           .             .               ////////
                  .    .   ________   .  .      /////////     .    .
             .            |.____.  /\        ./////////    .
      .                 .//      \/  |\     /////////
         .       .    .//          \ |  \ /////////       .     .   .
                      ||.    .    .| |  ///////// .     .
       .    .         ||           | |//`,/////                .
               .       \\        ./ //  /  \/   .
    .                    \\.___./ //\` '   ,_\     .     .
            .           .     \ //////\ , /   \                 .    .
                         .    ///////// \|  '  |    .
        .        .          ///////// .   \ _ /          .
                          /////////                              .
                   .   ./////////     .     .
           .           --------   .                  ..             .
    .               .        .         .                       .
                          ________________________
  ____________------------                        -------------_________
      ''')
print("You are Commander Aria, ISRO's rising analyst, chosen to lead a simulation mission to track dangerous debris threatening Earth's orbit.")
print('''
Your XP starts at 100.
Each decision changes your XP.
Lose all XP → mission failed 🚨\n
''')
xp = 100
print(f"🧮 Current XP: {xp}\n")
print("Scene 1\n")
print("An alert flashes — a rogue satellite fragment is spinning toward Earth's communication network.")
scene1 = int(input('''
You must decide:
1. Predict its path manually
2. Use the 'AI' tracker (untested)
Your choice? (1/2) : 
'''))
if scene1 == 1:
    xp += 20
    print("You triple-check every coordinate and dodge the impact 💪... 🟢+20XP\n")
elif scene1 == 2:
    xp -= 15
    print("The AI tracker misreads the path; you catch it late. The fragment hits a minor relay.... 🔴-15XP")
    print("🟣 Clue gained: The AI miscalculates high-velocity objects.\n")
else:
    print("Enter proper choice (either 1 or 2).\n")
    quit()
print(f"🧮 Current XP: {xp}\n")
print("Scene 2\n")
print("You detect a cluster of debris moving erratically.")
scene2 = int(input('''
1. Fire the Laser Net System (experimental)
2. Evacuate nearby satellites instead
Your choice? (1/2) :
'''))
if scene2 == 1:
    choice = random.choices([-10, 10])[0]
    xp += choice
    print(f"You manage to vaporize half the cluster, but one beam misfires and fries a solar panel 💀... {choice}XP")
    print("HQ warns you to be more careful..\n")
elif scene2 == 2:
    xp -= 10
    print("You save the network by moving them out — but it consumes a ton of fuel and leaves a smaller debris untracked.")
    print("You avoided damage, but lost time and resources... 🔴-10XP\n")
else:
    print("Enter proper choice (either 1 or 2).\n")
    quit()
print(f"🧮 Current XP: {xp}\n")
print("Scene 3\n")
print("Suddenly, your power core starts to fluctuate mid-mission! You can either:")
scene3 = int(input('''
1. Pause debris tracking to stabilize the reactor
2. Ignore it and focus on completing tracking
Your choice? (1/2) :
'''))
if scene3 == 1:
    xp -= 5
    print("You lose tracking time but prevent a total system meltdown... 🔴-5XP\n")
elif scene3 == 2:
    choice = random.choices([+15, -25])[0]
    xp += choice
    print("You push through -- system overheats 😬")
    print(f"You complete the scan, but now energy is critically low... {choice}XP\n")
else:
    print("Enter proper choice (either 1 or 2).\n")
    quit()
print(f"🧮 Current XP: {xp}\n")
print("Scene 4\n")
print('''
A massive rocket fragment is tumbling toward Earth.
Your reactor is low. You must decide:
''')
scene4 = int(input('''
1. Use all power to neutralize it
2. Predict its landing and warn Earth  
Your choice? (1/2) : 
'''))
if scene4 == 1:
    choice = random.choices([+25, -15])[0]
    xp += choice
    print(f"The beam works, but the overload fries your sensors⚡... {choice}XP\n")
elif scene4 == 2:
    choice = random.choices([+15, -10])[0]
    xp += choice
    print("You make a perfect prediction and alert HQ in time--")
    print(f"but your slow response costs one satellite... {choice}XP\n")
else:
    print("Enter proper choice (either 1 or 2).\n")
    quit()
print(f"🧮 Final XP: {xp}\n")
print("\n...FINAL OUTCOME...\n")
if xp <= 0:
    print("You lose control -- Mission failed💀.'Even the best commanders need backup.'")
elif (1 <= xp < 60):
    print("You barely save orbit👾.'You made it... but at what cost?'")
elif(60 <= xp < 100):
    print("You protect all major networks.'Your name shines at ISRO HQ.'")
else:
    print("You detect a debris cluster that moves like it's alive. 'That's not debris… it's a signal.' 👽")
