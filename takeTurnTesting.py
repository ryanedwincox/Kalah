class state:
    def __init__(self, a, b, a_fin, b_fin):
        self.a = a
        self.b = b
        self.a_fin = a_fin
        self.b_fin = b_fin
 
# prints game state to console 
def display(state):
    print("\t")
    bString = "    "
    for i in range(0,6):
        bString = bString + str(state.b[5-i]) + " "
    print bString
    print(str(state.b_fin) + "\t\t" + str(state.a_fin))
    aString = "    "
    for i in range(0,6):
        aString = aString + str(state.a[i]) + " "
    print aString
        
        
        
# Returns the next game state based on the input parameters
# current state
# chosen move
# whos turn
def takeTurn(state, move, max):
    # player a's turn
    if max:
        # get numbers of rocks in chosen hole
        rocks = state.a[move]
        # take all the rocks from the chosen hole
        state.a[move] = 0
        # put 1 rock in each hole till you run out
        A = move + 1 # start in the next hole
        B = 6
        for i in range(0, rocks):
            if (A < 6):
                state.a[A] = state.a[A] + 1
                if (i != rocks - 1):
                    A = A + 1 # on the last move don't increment
            elif (A == 6 and B == 6): # B==6 insures this case only occurs once
                state.a_fin = state.a_fin + 1
                if (state.a_fin > 36): # game over
                    print("max wins")
                    break
                B = 0
            elif (B < 6):
                state.b[B] = state.b[B] + 1
                B = B + 1
                if (B == 6):
                    A = 0
                
        # if the last rock lands in an empty spot on the A side then take all the opposite rocks and put them in A's kalah
        if (A != 6 and state.a[A] == 1 and rocks > 6):
            state.a_fin = state.a_fin + state.b[5-A]
            state.b[5-A] = 0;
        
        # if the last rock lands in the kalah take another turn
        if (A == 6 and B == 0):
            print("max takes another turn")
            
        # if there are no rocks on a's side all b's rocks go to b's kalah
        if (state.a[0] == 0 and state.a[1] == 0 and state.a[2] == 0 and state.a[3] == 0 and state.a[4] == 0 and state.a[5] == 0):
            state.b_fin = state.b_fin + state.b[0] + state.b[1] + state.b[2] + state.b[3] + state.b[4] + state.b[5]
            
    else: # mins turn
        # get numbers of rocks in chosen hole
        rocks = state.b[move]
        # take all the rocks from the chosen hole
        state.b[move] = 0
        # put 1 rock in each hole till you run out
        B = move + 1 # start in the next hole
        A = 6
        for i in range(0, rocks):
            if (B < 6):
                state.b[B] = state.b[B] + 1
                if (i != rocks - 1):
                    B = B + 1 # on the last move don't increment
            elif (B == 6 and A == 6): # A==6 insures this case only occurs once
                state.b_fin = state.b_fin + 1
                if (state.b_fin > 36): # game over
                    print("min wins")
                    break
                A = 0
            elif (A < 6):
                state.a[A] = state.a[A] + 1
                A = A + 1
                if (A == 6):
                    B = 0
                
        # if the last rock lands in an empty spot on the A side then take all the opposite rocks and put them in A's kalah
        if (B != 6 and state.b[B] == 1 and rocks > 6):
            state.b_fin = state.b_fin + state.a[5-B]
            state.a[5-B] = 0;
        
        # if the last rock lands in the kalah take another turn
        if (B == 6 and A == 0):
            print("min takes another turn")
            
        # if there are no rocks on b's side all a's rocks go to a's kalah
        if (state.b[0] == 0 and state.b[1] == 0 and state.b[2] == 0 and state.b[3] == 0 and state.b[4] == 0 and state.b[5] == 0):
            state.a_fin = state.a_fin + state.a[0] + state.a[1] + state.a[2] + state.a[3] + state.a[4] + state.a[5]
    return state
 
#initialize a game state, call the takeTurn method and display the results
move = 5
max = False
bStart = [0,0,0,0,0,1]
aStart = [0]*6
for i in range(0,6):
    aStart[i] = 2
    # aStart[i] = 4
startingBoard = state(aStart, bStart, 0, 0)
display(startingBoard)
newState = takeTurn(startingBoard, move, max)
display(newState)


    

