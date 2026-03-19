Hawaii_points = 0
Tokyo_points = 0
Yakima_points = 0 


answer1 = input ("Do you prefer A beach, B city, or C farm?")
if answer1 == "A":
    Hawaii_points += 1
elif answer1 == "B":
    Tokyo_points = 1
elif answer1 == "C":
    Yakima_points += 1


answer2 = input ("What weather do you prefer?: A tropical weather (rain and sun), B dessert weather (extreme heat), C mixed weather (mild sun, wind, a little rain)")
if answer2 == "A":
    Hawaii_points += 1
elif answer2 == "B":
    Yakima_points += 1
elif answer2 == "C":
    Tokyo_points += 1


answer3 = input ("What sounds the most fun out of these activities?: A shopping, B being at the beach, C riding a horse on the trails")
if answer3 == "A":
    Tokyo_points += 1
elif answer3 == "B":
    Hawaii_points += 1
elif answer3 == "C":  
    Yakima_points += 1


answer4 = input ("What job would you apply for out of these options?: A Architect, B Farmer C Lifeguard")
if answer4 == "A":
    Tokyo_points += 1
elif answer4 == "B":
    Yakima_points += 1
elif answer4 == "C": 
    Hawaii_points += 1


answer5 = input ("Which pet would you get out of these options?: A Dog, B Bird, C Horse")
if answer5 == "A":
    Tokyo_points += 1
elif answer5 == "B":
    Hawaii_points += 1
elif answer5 == "C":
    Yakima_points += 1


answer6 = input ("What kind of house would you like?: A small house on the beach, B Apartment, C cabin in the woods")
if answer6 == "A":
    Hawaii_points += 1
elif answer6 == "B": 
    Tokyo_points += 1
elif answer6 == "C": 
    Yakima_points += 1


answer7 = input ("What is your ideal dinner out of these options?: A late night sushi dinner with friends, B summer evening picnic on the beach, C Barbecue in your back yard of your ranch")
if answer7 == "A":
    Tokyo_points += 1
elif answer7 == "B":
    Hawaii_points += 1
elif answer7 == "C":
    Yakima_points += 1


answer8 = input ("What word best describes your personality?: A adventurous, B go-with-the-flow, C laid back")
if answer8 == "A" or answer8 == "B":
    Yakima_points += 1
elif answer8 == "B":
    Tokyo_points += 1
elif answer8 == "A" or answer8 == "C":
    Hawaii_points += 1

answer9 = input ("What kind of scenery do you want outside your window?: A City B Beach C Mountain range")
if answer9 == "A":
    Tokyo_points += 1
elif answer9 == "B":
    Hawaii_points += 1
elif answer9 == "C":
    Yakima_points += 1
    
# End: three different types of points
if Tokyo_points > Yakima_points and Tokyo_points > Hawaii_points:
    print("You should live in Tokyo!")
elif Yakima_points > Tokyo_points and Yakima_points > Hawaii_points:
    print ("You should live in Yakima!")
elif Hawaii_points > Tokyo_points and Hawaii_points > Yakima_points:
    print ("You should live in Hawaii!")