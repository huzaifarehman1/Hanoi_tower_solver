class node:
    # used to store the state of board
    def __init__(self,state,parent = None,action = None,cost = 0,distance = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost # heuristic cost of state
        self.dis_from_start = distance # step moves distance from start state


class FRONTIER:
    def __init__(self):
        pass
    
    def pop(self):
        pass
    
    def push(self):
        pass

class puzzle:
    def __init__(self,numOfTower = 3,numOfRings = 3,board = None):
        self.towers = numOfTower
        self.rings = numOfRings
        if board is None:
            self.board = [[] for i in range(self.towers)] # Will store int as 1 2 3 where 3 is  on top and largest ring 
        else:
            self.board = [i[::] for i in board]
            
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
    
    def heuristicFunction(self,dis_From_start):
        cost = 0
        for i in range(self.towers):
            if len(self.board[i])<=0:
                continue
            
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
                    if int(ele[j]-1) <= int(ele[j]):
                        return False
        return True            
                        
                
    def isgoal(self):
        # wether the state is the goal 
        index = -1 # Index of the rings in tower
        # all must be in the same tower 
        for i in range(len(self.board)):
            if len(self.board[i]>0):
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
                        
    def availalblemoves_AND_costValueOfState(self):                           
        """used for solver

        Returns {move:(state produced} => dict
        """
        moves = {}
        for i in range(len(self.board)):
            if len(self.board[i]) <= 0:
                # no ring in this tower
                continue
            size = self.board[i][-1]
            # the top ring
            for j in range(i+1,len(self.board)):
                move_str = f"{i}=>{j}"
                if move_str in moves:
                    continue
                if len(self.board[j])<=0:
                    ele = self.board[i].pop()
                    self.board[j].append(ele)
                    # copy and push
                    newboard = puzzle(self.towers,self.rings,self.board)
                    self.board[i].append(ele)
                
                
    
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
    frontier = FRONTIER()




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
    
            
        
    
if __name__=="__main__":
    main()        