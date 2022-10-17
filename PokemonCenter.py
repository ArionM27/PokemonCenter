"""
Arion Mercado
11/29/21
Section 003
Pokemon Center Database #2
"""
    
#Converting the data to a text file

fp = open("pokemon.txt", "r")
data = fp.read()
linesplit= data.split("\n")
pokemon= {}
types= []
countertype= 0
for i in linesplit:
    a= i.split(",")
    try:
        pokemon[str(a[0])]= {'quantity':int(a[1]),'fee':float(a[2]),'powers':a[3]}
        countertype += 1
    except:
        randomnumber= 0

fp.close()

    


valid_pokemon_types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']


while True:

    print("Welcome to the Pokemon Center!")
#Asking the user for an input
    options = input("(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit: ")
    #Quitting the user out of the program
    if options.lower() == "q":
        print("See you next time!")
        print("")

        #Ensuring the data stays 
        fp = open("pokemon.txt", "w")
        for i in pokemon:
            fp.write(str(i))
            fp.write(',')
            fp.write(str(pokemon[i]['quantity']))
            fp.write(',')
            fp.write(str(pokemon[i]['fee']))
            fp.write(',')
            fp.write(str(pokemon[i]['powers']))
            fp.write('\n')
        fp.close()

        break
    #Allowing the user to search for a program
    elif options.lower() == "s":
        name = input("Enter the name of a pokemon: ")
        name= name.lower()
        if name in pokemon:

            print("We have", pokemon[name]['quantity'], name.capitalize(), "at the Pokemon Center")
            print("It will cost", "$" + format(float(pokemon[name]['fee']), ',.2f'), "to adopt this Pokemon")
            print(name.capitalize(), "has the following types: ", end= '')
            types= pokemon[name]['powers']
            print(types, end= ' ')
            print("")
            print("")
        
        else:
            print("We do not have any", name, "at the Pokemon Center")
            print("")
        

#Giving the user a list
    elif options.lower() == "l":
        print(format('Name', '<12s'), format('Amount Available', '<18s'), "Adoption Fee", " Type(s)")
        for i in pokemon:
            types = ''
            types += (pokemon[i]['powers']) + " "

            print(format(i.capitalize(),'<13s'), format(str(pokemon[i]['quantity']), '>15s'), format(str(format(float(pokemon[i]['fee']), ',.2f')), '>14s'), "", format(str(types), '>2s'))

        print("") 

#Allowing the user to search by type
    
    elif options.lower() == "t":
        chosentype= input("Enter Pokemon type: ")
        chosentype= chosentype.capitalize()


        #Creating the list headers
        for i in pokemon:
            typecount= 0
            if chosentype in pokemon[i]['powers']:  
                typecount+= 1
                print(format('Name', '<12s'), format('Amount Available', '<18s'), "Adoption Fee", " Type(s)")
                break
        #searching for given type
        for i in pokemon:
            types = ''
            types += (pokemon[i]['powers']) + " "
            if chosentype in pokemon[i]['powers']:
                print(format(i.capitalize(),'<13s'), format(str(pokemon[i]['quantity']), '>15s'), format(str(format(float(pokemon[i]['fee']), ',.2f')), '>14s'), "", format(str(types), '>2s'))

        #Checking if type does exist or not
        if typecount == 1:
            print("")
        else:
            print("We have no Pokemon of that type at our Pokemon Center")
            print("") 
        
        

    #Giving the user the report
    
    elif options.lower() == "e":
        
        #Finding the max amount
        largest= 0
        for i in pokemon:
            if pokemon[i]['fee']> largest:
                largest= pokemon[i]['fee']
        for i in pokemon:
            if pokemon[i]['fee'] == largest:
                highestpokemon= i.capitalize()

        #Finding the min amount
        lowest= largest
        for i in pokemon:
            if pokemon[i]['fee']< lowest:
                lowest= pokemon[i]['fee']
        for i in pokemon:
            if pokemon[i]['fee'] == lowest:
                lowestpokemon= i.capitalize()

        #Finding the total amount
        totalamount= 0 
        for i in pokemon:
            specifictotal= pokemon[i]['quantity'] * pokemon[i]['fee']
            totalamount += specifictotal
        

    #Printing out highest prices, lowest, and totals
        print("Highest priced pokemon:", highestpokemon,  "@", "$" + str(format(float(largest), ',.2f')), "per pokemon")
        print("Lowest priced pokemon:", lowestpokemon,  "@", "$" + str(format(float(lowest), ',.2f')), "per pokemon")
        print("Total cost to adopt all Pokemon in the Center:", "$" + str(format(float(totalamount), ',.2f')))
        print("")


    #Creating an add function
    elif options.lower()== 'a':
    #Asking the user information about the new pokemon
        new_pokemon= input("Enter name of new pokemon: ")
        new_pokemon= new_pokemon.lower()
            
        if new_pokemon not in pokemon:
            
            #Asking for amount and adoption fee using while loop in the case of an invalid number
            while True:
                try:
                    new_pokemon_amount= int(input("How many of these pokemon are you adding? "))
                    if new_pokemon_amount>= 1:
                        break
                    else:
                        print("Invalid, please try again")
                except:
                    print("Invalid, please try again")
            
            while True:
                try:
                    new_pokemon_fee= float(input("What is the adoption fee for this pokemon? "))
                    if new_pokemon_fee> float(0):
                        break
                    else:
                        print("Invalid, please try again")

                except:
                    print("Invalid, please try again")
        #Informing the user of the rules surrounding pokemon types
        
            print("Next you will be prompted to enter the 'types' for this Pokemon.  Pokemon can have multiple types. Type 'help' to view all possible Pokemon types, and type 'end' to stop entering types. You must enter at least one valid 'type'")
        #Ensuring the user add a valid pokemon type or function
            validtypeadd= ''
            while True:
                
                typeadd= input("What type of Pokemon is this? ")
                typeadd= typeadd.lower()
                if typeadd in valid_pokemon_types:
                    validtypeadd+= typeadd.capitalize() + " "
                    print("Type", typeadd, "applied")
        
            #Giving the user a list of types if needed
                elif typeadd== "help":
                    for i in valid_pokemon_types:
                        print("* "+ i)
                elif typeadd== "end":
                    print("Pokemon Added!")
                    print("")
                    break
                else:
                    print("This is not a valid type, please try again")
                    print("")
            pokemon[str(new_pokemon)]= {'quantity':new_pokemon_amount,'fee':new_pokemon_fee,'powers':validtypeadd}
        else:
            print("Duplicate name, add operation cancelled")
            print("")

    elif options.lower()== 'r':
        pokemon_remove= input("Enter name of Pokemon to remove: ")
        if pokemon_remove in pokemon:
            del pokemon[pokemon_remove]
            print("Pokemon Removed")
            print("")
        else:
            print("Pokemon not found, cannot remove")
            print("")

    #Giving the user an error if command does not work
    else:
        print("Unknown command, try again")
        print("")