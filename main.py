import heapq

class node:
    # used to store the state of board
    def __init__(self,state,parent = None,action = None,cost = 0,distance = 0,hashed = None,max_ring_position = (0,0)):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost # heuristic cost of state
        self.dis_from_start = distance # step moves distance from start state
        self.hashable_state = hashed# hashable state so it can be put into seen set
        self.max_ring_position = max_ring_position # position of the biggest ring in the board
        
    def __lt__(self, other):
        if self.cost+self.dis_from_start == other.cost+other.dis_from_start:
            return self.dis_from_start>other.dis_from_start # same H value so deeper is better
        # because if H is same then deep have better goal distance 
        
        elif self.cost+self.dis_from_start < other.cost+other.dis_from_start:  # lower cost = higher priority
            return True
        return False



class FRONTIER: 
    maximum = 100000005
    def __init__(self):
        self.count = 0
        self.heap = []
    
    def pop(self):
        if self.isempty():
            raise Exception("EMPTY!!!")
        ele = heapq.heappop(self.heap)
        self.count -= 1
        return ele
    
    def push(self,ele:node):
        if self.isfull():
            print("FULL")
        self.count += 1
        heapq.heappush(self.heap,ele)
    
    def isempty(self):
        return self.count<=0
    
    def isfull(self):
        return self.count>=self.maximum

class puzzle:
    def __init__(self,numOfTower = 3,numOfRings = 3,board = None,position = (0,0)):
        self.towers = numOfTower
        self.rings = numOfRings
        if board is None:
            self.board = [[] for i in range(self.towers)] # Will store int as 1 2 3 where 3 is  on top and largest ring 
        else:
            self.board = [i[::] for i in board]
        
        self.max =  position # position of the maximum ring    
            
    def __valide_input(self,num):
        """take valid index from user for the board
        """
        if num<0 or num >= self.towers:
            return False
        if len(self.board[num])>self.rings:
            print("tower full")
            return False
        return True
    
    def initialize_board_FromInput(self):
            count = self.rings
            avail = {s for s in range(1,self.rings+1)}
            self.board = [[] for i in range(self.towers)]
            while count>0:
                try:
                    x = int(input(f"Enter index for ring number {self.rings - count + 1} (1 to {self.towers}) "))
                except ValueError:
                    print("only integers")
                    continue
                except Exception as e:
                    print(e)
                    print("somehting went wrong")
                    continue
                else:
                                
                    if not(self.__valide_input(x-1)):
                        print()
                        print("invalide number for the tower" )
                        print(f"number must be >0 and <={self.towers}")
                        print() 
                        continue
                    count -= 1
                    
                    while True:
                        try:
                            print(f"available size options {avail}")    
                            print()
                            print(f"BOARD=> {self.board}")
                            print()
                            size = int(input(f"size of ring (1 is smallest and {self.rings} is largest) : "))    
                            
                        except ValueError :
                            print("only integers")  
                            continue  
                        else:
                            if size<0 or size > self.rings:
                                print()
                                print("invalide size") 
                                print() 
                                continue  
                            if size not in avail:
                                print()
                                print("not available")
                                print()
                                continue
                            avail.remove(size)
                            self.board[x-1].append(size)
                            break
            print(self.board)            
    
    def find_max_ring(self):
        for i in range(self.towers):
            for j in range(len(self.board[i])):
                if self.board[i][j]==self.rings:
                    self.max == (i,j)
                    return True
        return False        
    
    def heuristicFunction(self,dis_From_start,position):
        """
            return heuristic value
            
        Args:
            dis_From_start (int): distence of a state from given start state
            position (tuple):position of the largest ring in the board

        Returns:
            int: heuristic value
        """
        cost = 0
        spread = 0
        correct = 1
        for i in range(self.towers):
            if len(self.board[i])<=0:
                continue
            spread += 1
        pos1,pos2 = position
        for i in range(len(self.board[pos1])):
            if i<=0:
                continue
            if self.board[pos1][i-1]==self.board[pos1][i]+1:
                correct += 1
            else:
                break    
        cost =  spread - pow(correct,2)  
            
        return cost + dis_From_start    
        
    def valid_board(self):
        """is the input board valid?
        Returns:
            (bool) 
        """
        for i in range(len(self.board)):
            ele = self.board[i]
            if len(ele)<=1:
                continue
            for j in range(1,len(ele)):
                    if ele[j-1] <= ele[j]:
                        return False
        return True            
                        
                
    def isgoal(self):
        # wether the state is the goal 
        index = -1 # Index of the rings in tower
        # all must be in the same tower 
        for i in range(len(self.board)):
            if len(self.board[i])>0:
                if index==-1:
                    index = i
                else:
                    return False
        if index==-1:
            raise Exception ("invalide board no ring found")
        
        for i in range(1,len(self.board[index])):
            if self.board[index][i-1] <= self.board[index][i]: # Must be in decreasing order
                return False   
        
        return True                          
                        
    def availalblemoves(self,parentcost):   # find available moves and heuristic value as well                        
        """used for solver

        Returns {move:(state produced,cost)} => dict
        """
        moves = {}
        for i in range(len(self.board)):
            
            if len(self.board[i]) <= 0:
                # no ring in this tower
                continue
            size = self.board[i][-1]
            # the top ring
            
            for j in range(len(self.board)):
                if j==i:
                    continue
                move_str = f"{i}=>{j}"
                if move_str in moves:
                    continue
                
                if size==self.rings: 
                    new_max_position = (j,len(self.board[j]))
                else:    
                    new_max_position = self.max
                                
                if len(self.board[j])<=0 or self.board[j][-1]>size:
                    newboard = puzzle(self.towers,self.rings,self.board,new_max_position)
                    ele = newboard.board[i].pop()
                    newboard.board[j].append(ele)  
                    cost = newboard.heuristicFunction(parentcost+1,new_max_position)
                    moves[move_str] = (newboard,cost,new_max_position) # cause it the next state so +1 
        return moves        
    def hashable_type(self):
        """
        convert a state to hasable state
        """
        return tuple(tuple(i) for i in self.board)           
    
def taking_input_ints():
    """
    take input the number of towers and rings
    Returns: tup = (towers,rings)
    
    """
    temp = []
    while True:
        try:
            x = int(input("Enter the number of Towers (n): "))
        except ValueError :
            print("only integers allowed")
            continue
        except Exception as e:
            print(e)
            print("something went wrong")
            continue
            
        else:    
            if x<=0:
                print("x must be >= 1")
                continue
            temp.append(x)
            break
        
    while True:
        try:
            x = int(input("Enter the number of rings (m): "))
        except ValueError :
            print("only integers allowed")
            continue
        except Exception as e:
            print(e)
            print("something went wrong")
            continue
            
        else:    
            if x<=0:
                print("x must be >= 1")
                continue
            temp.append(x)
            break 
    
    return temp           
                


def SOLVER(board:puzzle): # uses A*
    
    seen = set() # states seen so far
    frontier = FRONTIER() # to store states
    max_ = board.find_max_ring()
    if not(max_):
        raise Exception ("FAILED TO FIND LARGEST RING")
    start = node(board,None,None,board.heuristicFunction(0,board.max),0,board.hashable_type())
    states_seen_count = 0

    frontier.push(start)
    while not(frontier.isempty()):
        ele:node = frontier.pop()
        state:puzzle = ele.state
        states_seen_count += 1
        if state.isgoal():
            print("FOUND SOLUTION")
            act = []
            
            while (ele.parent is not None):
                act.append(ele.action)
                ele = ele.parent
            act = act[::-1]    
            return (states_seen_count,act)   
            
        # look at child if no solution at this state
        
        seen.add(ele.hashable_state)
        moves:dict = state.availalblemoves(ele.dis_from_start)    
        # creating and adding child 
        for action,produced in moves.items():
            NewPuzzleObj:puzzle = produced[0]
            cost = produced[1]
            pos = produced[2]
            hashed = NewPuzzleObj.hashable_type()

            if hashed not in seen:
                newnode = node(NewPuzzleObj,ele,action,cost,ele.dis_from_start+1,hashed,pos)
                frontier.push(newnode)
                seen.add(hashed)
            
            
    # no solution found        
    print("NO SOLUTION FOUND")    
    return (states_seen_count,act)



def main():
    answer = False
    while not(answer):
        input_taken = taking_input_ints()
        game = puzzle(input_taken[0],input_taken[1])
        game.initialize_board_FromInput()
        answer = (game.valid_board())
        if not(answer):
            print()
            print("invalide board all rings must be in accending order form top")
            print()
    seen,sol = SOLVER(game)
    print(f"state seen = {seen}")
    print("solution")
    print(sol)
    
            
        
    
if __name__=="_main__":
    main()
else: # if you want to test certain parts
    state = board = [[2], [5, 1], [4], [3]] 
    rings = 5
    position = (1,0) # (tower number , height) for the largest ring all is 0 indexed
    game = puzzle(len(state),rings,state,position)  
    print(x:=SOLVER(game),len(x[1])) 
         