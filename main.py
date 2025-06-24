class puzzle:
    def __init__(self,numOfTower = 3,numOfRings = 3):
        self.towers = numOfTower
        self.rings = numOfRings
        self.board = [""] * self.towers # Will store int as 123 where 3 is  on top and largest ring 
    
    def __valide_input(self,num):
        """take valid index from user for the board
        """
        if num<0 or num >= self.towers:
            return False
        if len(self.board[num])>self.rings:
            print("tower full")
            return False
        return True
    
    def initialize_board(self):
            count = self.rings
            avail = {s for s in range(1,self.rings+1)}
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
                            self.board[x-1] += str(size) 
                            break
        
    def __valid_board(self):
        pass
    
    def availalble_moves(self):                           
        pass
    
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
                
def main():
    input_taken = taking_input_ints()
    game = puzzle(input_taken[0],input_taken[1])
    game.initialize_board()
    
if __name__=="__main__":
    main()        