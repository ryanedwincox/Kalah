import time
import random 
import io
import sys
import copy

class key:
    def key(self):
        return "10jifn2eonvgp1o2ornfdlf-1230"
        
class ai:
    def __init__(self, moves = 0):
        #pass ****
        self.moves = moves # ****

    class state:
        def __init__(self, a=[0,0,0,0,0,0], b=[0,0,0,0,0,0], a_fin=0, b_fin=0):
            self.a = a
            self.b = b
            self.a_fin = a_fin
            self.b_fin = b_fin
            
    class moveCounter:
        def __init__(self, moves=0):
            self.moves = moves


    # Kalah:
    #         b[5]  b[4]  b[3]  b[2]  b[1]  b[0]
    # b_fin                                         a_fin
    #         a[0]  a[1]  a[2]  a[3]  a[4]  a[5]
    # Main function call:
    # Input:
    # a: a[5] array storing the stones in your holes
    # b: b[5] array storing the stones in opponent's holes
    # a_fin: Your scoring hole (Kalah)
    # b_fin: Opponent's scoring hole (Kalah)
    # t: search time limit (ms)
    # a always moves first
    #
    # Return:
    # You should return a value 0-5 number indicating your move, with search time limitation given as parameter
    # If you are eligible for a second move, just neglect. The framework will call this function again
    # You need to design your heuristics.
    # You must use minimax search with alpha-beta pruning as the basic algorithm
    # use timer to limit search, for example:
    # start = time.time()
    # end = time.time()
    # elapsed_time = end - start
    # if elapsed_time * 1000 >= t:
    #    return result immediately 
    def move(self, a, b, a_fin, b_fin, t):
        # #For test only: return a random move
        # r = []
        # for i in range(6):
            # if a[i] != 0:
                # r.append(i)
        # # To test the execution time, use time and file modules
        # # In your experiments, you can try different depth, for example:
        # f = open('time.txt', 'a') #append to time.txt so that you can see running time for all moves.
        # # Make sure to clean the file before each of your experiment
        # for d in [3, 5, 7]: #You should try more
            # f.write('depth = '+str(d)+'\n')
            # t_start = time.time()
            # self.minimax(depth = d)
            # f.write(str(time.time()-t_start)+'\n')
        # f.close()
        # return r[random.randint(0, len(r)-1)]
        # #But remember in your final version you should choose only one depth according to your CPU speed (TA's is 3.4GHz)
        # #and remove timing code. 
        
        # *****
        
        # create starting state from input parameters
        initial = ai.state(a, b, a_fin, b_fin)
        
        # set the maximum depth the search should execute
        depth = 3
        
        # initial call of the minimax function
        # the helper method returns the desired move
        return ai.minimaxHelper(self, initial, depth-1, -sys.maxint, sys.maxint, True)

    # This helper method does the first step of the recursion so that it can identify the move that returns the highest alpha
    def minimaxHelper(self, state, depth, alpha, beta, max):
        # In this method it is always max's turn
        
        # consider each of the six possible moves
        # TODO: order moves for efficiency 
        bestMove = 0
        highestAlpha = -sys.maxint
        possibleMoves = [0,1,2,3,4,5]
        for move in possibleMoves: 
            self.moves = self.moves + 1
            print("move " + str(move)) # ****
            # don't consider moves with no stones
            if (state.a[move] > 0):
                # get new game state after the move has been taken
                newState = copy.deepcopy(state)
                maxTurn = self.takeTurn(newState, move, max)
                print("max turn: " + str(maxTurn))
                # extend search if player gets another turn
                if (maxTurn):
                    depth = depth + 0
                print("first max turn") # ****
                self.display(newState) # ****
                # if the depth is 0 return heuristic value without recursing 
                if (depth == 1):
                    alpha = self.objective(newState, max)
                    print ("move: " + str(move) + "\theuristic value: " + str(alpha)) # ****
                else:
                    # make recursive call. Decrease depth and switch turns
                    alpha = self.minimax(newState, depth-1, alpha, beta, maxTurn)
                # keeps track of the highest alpha and the associated best move
                if (alpha > highestAlpha):
                    highestAlpha = alpha
                    bestMove = move
                # decrease depth for all other moves
                if (maxTurn):
                    depth = depth - 0
        return bestMove
        
    # minimax search function with alpha-beta pruning
    def minimax(self, state, depth, alpha, beta, mx):
        # base case
        # reached max depth
        # game is over if either player has more than 36 in their kalah
        if (depth == 0 or state.a_fin > 36 or state.b_fin > 36): 
            print ("Heuristic Value: " + str(self.objective(state, mx)))
            return self.objective(state, mx) # ****
        # Max players turn
        if (mx): 
            # consider each of the six possible moves
            # TODO: order moves for efficiency 
            possibleMoves = [0,1,2,3,4,5]
            for move in possibleMoves:
                self.moves = self.moves + 1
                # don't consider moves with no stones
                if (state.a[move] > 0):
                    # get new game state after the move has been taken
                    newState = copy.deepcopy(state)
                    maxTurn = self.takeTurn(newState, move, mx)
                    print("max turn: " + str(maxTurn))
                    # extend search if player gets another turn
                    if (maxTurn):
                        depth = depth + 0
                    print("max turn")
                    self.display(newState) # ****
                    # make recursive call. Decrease depth and switch turns
                    alpha = max(alpha, self.minimax(newState, depth-1, alpha, beta, maxTurn))
                    if (beta <= alpha):
                        print("beta cut-off")
                        break # beta cut-off
                    # decrease depth for all other moves
                    if (maxTurn):
                        depth = depth - 0
            return alpha
        # Min players turn
        else:
            # consider each of the five possible moves
            # TODO: order moves for efficiency 
            possibleMoves = [0,1,2,3,4,5]
            for move in possibleMoves:  
                self.moves = self.moves + 1
                # don't consider moves with no stones
                if (state.b[move] > 0):
                    # get new game state after the move has been taken
                    newState = copy.deepcopy(state)
                    maxTurn = self.takeTurn(newState, move, mx)
                    print("max turn: " + str(maxTurn))
                    # extend search if player gets another turn
                    if (maxTurn == False):
                        depth = depth + 0
                    print("min turn")
                    self.display(newState) # ****
                    # make recursive call. Decrease depth and switch turns
                    beta = min(beta, self.minimax(newState, depth-1, alpha, beta, maxTurn))
                    if (beta <= alpha): 
                        print("alpha cut-off")
                        break # alpha cut-off
                    # decrease depth for all other moves
                    if (maxTurn):
                        depth = depth - 0
            return beta
    
    # rocks in kalah = 10 points
    # rocks in opposite kalah = -10 points
    def objective(self, state, max):
        val = 0
        # points in the Kalah's give most of the weight 
        # first half of the game play a little more defensive
        if (state.b_fin < 15):
            val = state.a_fin * 10 + state.b_fin * -13
        else:
            val = state.a_fin * 13 + state.b_fin * -10
            
        # favour states that potentially lead to extra moves
        for i in range(0,6):
            if (state.a[i] == 6-i):
                val = val + 3
        for i in range(0,6):
            if (state.b[i] == 6-i):
                val = val - 3
                
        # favour states with empty holes that have rocks directly across
        for i in range(0,6):
            bonus = state.b[5-i]
            if (state.a[i] == 0):
                val = val + bonus/2
        for i in range(0,6):
            bonus = state.a[5-i]
            if (state.b[i] == 0):
                val = val - bonus/2
        
        # avoid running out of rocks
        if (state.a[0] == 0 and state.a[1] == 0 and state.a[2] == 0 and state.a[3] == 0 and state.a[4] == 0 and state.a[5] == 0):
            val = val - 10000
        if (state.b[0] == 0 and state.b[1] == 0 and state.b[2] == 0 and state.b[3] == 0 and state.b[4] == 0 and state.b[5] == 0):
            val = val + 10000
        
        return val
    
    # Returns the next game state based on the input parameters
    # current state
    # chosen move
    # whos turn
    def takeTurn(self, state, move, max):
        # # deep copy so original state is not modified ****
        # state = copy.deepcopy(oldState)
        # player a's turn
        maxTurn = not max
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
            if (A != 6 and state.a[A] == 1 and rocks > 0):
                state.a_fin = state.a_fin + state.b[5-A]
                state.b[5-A] = 0;
            
            # if the last rock lands in the kalah take another turn
            if (A == 6 and B == 0):
                print("max takes another turn") # ****
                maxTurn = max
                
            # if there are no rocks on a's side all b's rocks go to b's kalah
            if (state.a[0] == 0 and state.a[1] == 0 and state.a[2] == 0 and state.a[3] == 0 and state.a[4] == 0 and state.a[5] == 0):
                state.b_fin = state.b_fin + state.b[0] + state.b[1] + state.b[2] + state.b[3] + state.b[4] + state.b[5]
                state.b[0] = 0
                state.b[1] = 0
                state.b[2] = 0
                state.b[3] = 0
                state.b[4] = 0
                state.b[5] = 0
                
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
            if (B != 6 and state.b[B] == 1 and rocks > 0):
                state.b_fin = state.b_fin + state.a[5-B]
                state.a[5-B] = 0;
            
            # if the last rock lands in the kalah take another turn
            if (B == 6 and A == 0):
                print("min takes another turn")
                maxTurn = max
                
            # if there are no rocks on b's side all a's rocks go to a's kalah
            if (state.b[0] == 0 and state.b[1] == 0 and state.b[2] == 0 and state.b[3] == 0 and state.b[4] == 0 and state.b[5] == 0):
                state.a_fin = state.a_fin + state.a[0] + state.a[1] + state.a[2] + state.a[3] + state.a[4] + state.a[5]
                state.a[0] = 0
                state.a[1] = 0
                state.a[2] = 0
                state.a[3] = 0
                state.a[4] = 0
                state.a[5] = 0
        return maxTurn
        
    # prints game state to console 
    def display(self, state):
        print("\t")
        bString = "   "
        for i in range(0,6):
            bString = bString + str(state.b[5-i]) + " "
        print bString
        print(str(state.b_fin) + "\t\t" + str(state.a_fin))
        aString = "   "
        for i in range(0,6):
            aString = aString + str(state.a[i]) + " "
        print aString
                            
                




