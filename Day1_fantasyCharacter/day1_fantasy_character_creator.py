import random
titles = ["Mystic", "Shadow", "Eternal", "Great", "Marvelous"]
print("Welcome To The Fantasy Character Generator😁✨")
print(r'''
                      ,-,-      
                     / / |      
   ,-'             _/ / /       
  (-_          _,-' `Z_/        
   "#:      ,-'_,-.    \  _     
    #'    _(_-'_()\     \" |    
  ,--_,--'                 |    
 / ""                      L-'\ 
 \,--^---v--v-._        /   \ | 
   \_________________,-'      | 
                    \           
                     \          
                      \         
''')
print("You'll be asked a few questions that will decide your name.. Let's go!!")
color = input("What is your favourite color? ").strip().title()
animal = input("Which animal do you like the most?👀 ").strip().title()
trait = random.choice(titles)
print("And finally..")
print(f"✨✨Let's welcome The {trait} {color} {animal}!!🥳")
