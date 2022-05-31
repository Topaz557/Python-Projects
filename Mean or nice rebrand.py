def start(nice=0,mean=0,name=""):
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)
    
def describe_game(name):
    """
    check if this is a new game or not
    if it is new, get the user's name
    if it is not a new game, thank the player for
    playing again and continue with the game
    """
    #meaing, if we do not already have this user's name,
    #then they are a new palyer and we need to get their name
    if name !="":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
         if name != "":
            name = input("\nWhat is your name? \n>>> ").capitalize()
            if name !="":
               print("\nWelcome, {}!".format(name))
               print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
               print("but at the end of the game your fate \nwill be sealed by your actions.")
               stop = False

    return name
                

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nThe stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick =="m":
            print ("\n the stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #pass the 3 variables to the score ()

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}. Nice)({}, Mean)".format(name,nice,mean))




def score(nice,mean,name):
      # score function is being passed the values within the 3 varaibles (name, nice, mean)
     if nice > 2: # if the condition of nice being greater than two is valid, call win screen
         win(nice,mean,name)
     if mean > 2: # if this condition of mean is greater than two, you lose the game
         lose(nice,mean,name)
     else:      # else call nice_mean function passing in the variables to it can use them for next operation
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    #substitute the {} wildscards with out variable values
    print ("\nNice job {}, you win! \nEveryone loves you and you've\nmade lots of friends along the way!".format(name))
    # call again function and pass in our var
    again(nice,mean,name)

def lose(nice,mean,name):
    # substitute the {} wi;dcards with our var values
    print ("\nAhhhhh too bad, game over! \n, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    # call again function and pass in our var
    again(nice,mean,name)



def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print ("\nOh, so sad, sorry to see you go")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    # Notice, i do not reset the name value because they have indicated same player
    start(nice,mean,name)



if __name__ == "__main__":
    start()