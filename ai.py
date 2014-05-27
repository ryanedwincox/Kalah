import time
import random 
import io

class key:
    def key(self):
        return "10jifn2eonvgp1o2ornfdlf-1230"

class ai:
    def __init__(self):
        pass

    class state:
        def __init__(self, a, b, a_fin, b_fin):
            self.a = a
            self.b = b
            self.a_fin = a_fin
            self.b_fin = b_fin

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
        
        # create starting state from input parameter
        initial = state(alpha, beta, a_fin, b_fin)
        
        # set the maximum depth the search should execute
        depth = 4
        
        # initial call of the minimax function
        minimax(initial, depth, -infinity, +infinity, True)

    # minimax search function with alpha-beta pruning
    def minimax(self, state, depth, alpha, beta, max):
        # base case
        # reached max depth
        # game is over if either player has more than 36 in their kalah
        if (depth == 0 or a_fin > 36 or b_fin > 36): 
            return heuristic # ****
        # Max players turn
        if (max): 
            # consider each of the five possible moves
            # TODO: order moves for efficiency 
            # TODO: don't consider moves with no stones
            possibleMoves = [0,1,2,3,4,5]
            for move in possibleMoves: # **** 
                # get new game state after the move has been taken
                newState = takeTurn(state, move, max)
                # make recursive call. Decrease depth and switch turns
                alpha = max(alpha, minimax(newState, depth-1, alpha, beta, False)
            if (beta <= alpha):
                break # beta cut-off
            return alpha
        # Min players turn
        else:
            # consider each of the five possible moves
            # TODO: order moves for efficiency 
            # TODO: don't consider moves with no stones
            for child in parent: # **** 
                # make recursive call. Decrease depth and switch turns
                beta = min(beta, minimax(child, depth-1, alpha, beta, True)
            if (beta <= alpha):
                break # alpha cut-off
            return beta
                
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
        
        print (str(A))
        print (str(B))
        # if the last rock lands in the kalah take another turn
        if (A == 6 and B == 0):
            print("max takes another turn")
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
    return state
                    
            




