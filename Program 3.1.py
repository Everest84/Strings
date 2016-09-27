## Program 3.py
## Program 3
## Matthew Downs
## CS 101
## Fall 2016
## Brian Hare
#################

import random, string


goal = 'This is a test.' # Assign the goal string

goal_fit = 0
for ch in goal: # Find its character value
    temp = ord(ch)
    goal_fit += temp
print("Desired text:", "'"+goal+"'", "\nValue:", goal_fit, "(character value sum)")


#### Step 1: String Generation >>


# Create random string population

print("\nHow many random strings would you like to generate?")
while True:
    try: # Checking for integer input
        pop_amt = int(input(">> "))
        break
    except ValueError: # Sends user back to input if input is not an integer
        print("Please enter an integer.")
        continue

while True:
    try: # Checking for integer input
        length = int(input("How many characters per string?:\n>> "))
        break
    except ValueError: # Sends user back to input if input is not an integer
        print("Please enter an integer.")
        continue
    
population = [] # New list created for the total string population
fit_list = [] # New list created for the fitness values

for i in range(pop_amt): # Iterates through number of strings desired
    
    string = '' # Reassigns variable *string* to be empty every iteration so they won't keep adding onto each other
    total = 0 # Reassigns variable *total* (which calculates the fitness score) to be zero every iteration
    
    for p in range(length): # Iterates through each character position and assigns a random one
        ch = chr(random.randint(32,126))
        string += ch

    for val in string: # Iteraters through each character space in the newly generated string and sums its value
        temp = ord(val)
        total += temp

    fitness = abs(goal_fit - total) # Determines the difference in character values
    population.append(string) # Adds this iteration string to the population list
    fit_list.append(fitness)
    print(string, "--- Fitness:", fitness)


#### Step 2: String Consolidation >>


# Retrieve the best fitting half of strings based on their fitness scores

set_full = [] # Assigns the list for appending every string generated to it

for a, b in zip(population,fit_list): # Joins the string with its fitness score and places them in a separate list
    set_item = [b,a]
    set_full += [set_item]
    
half = int(pop_amt/2) # The number of half the number of strings generated
fit_org = fit_list.sort() # Put the list in ascending order
fit_org = fit_list[:half] # Cuts the list in half from the beginning to the middle and deletes the rest
print(fit_org)




        
