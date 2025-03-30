import random
import os
def start():
    global x, s, index_grid
    print("TicTacToe\n")
    x = [
        "      |      |       ",
        "---------------------",
        "      |      |       ",
        "---------------------",
        "      |      |       "
    ]
   
    s= -1
    index_grid={1: [0, 3], 2: [0, 10], 3: [0, 17], 4: [2, 3], 5: [2, 10], 6: [2, 17], 7: [4, 3], 8: [4, 10], 9: [4, 17]}
    print_grid()
    char_choice()
   
def print_grid():
        global x, s
        for row in x:
            print(row)
        s+=1
        #print(s)
        if s !=0 :
            check_win()         
   
def char_choice():
    global start_1, start_2, inp_choice
    #import random
    choice=["X", "O"]
    while True:
        inp_choice=input("\nPlayer 1: Choose X or O: ").upper()
        if inp_choice not in choice:
            print("Invalid character! Choose again.")
        else:
            break    
    print("Player 2 takes: ", choice[1-choice.index(inp_choice)])    
    random_beginner=random.choice(choice)
    if random_beginner !=inp_choice:
            print("\nPlayer 2 will go first.")
            start_2=random_beginner
            start_1 = choice[1 - choice.index(random_beginner)]
            while True:
                human_choice(start_2, x:=2)
                human_choice(start_1, x:=1)
    else:
            start_1 = random_beginner
            start_2 = choice[1 - choice.index(random_beginner)]
            print("\nPlayer 1 will go first.")
            while True:
                human_choice(start_1, x:=1)
                human_choice(start_2, x:=2)                   
                         
def human_choice(start, x):
    while True:
        y=input(f"Player {x}: Choose a number ranging from 1-9: ")
        if not (y.isdigit()) or int(y) not in range(1, 10):
            print("Invalid Input! Choose again.")
            continue
        y=int(y)    
        if pos_free(y):
            break
        print("Invalid Input! Choose again.")            
    grid_update(start, y)
    print_grid()
    
def grid_update(start, y):
        global x, s, index_grid, index_grid  
        value_indexh=index_grid[y]
        a, b = value_indexh
        x[a] = x[a][:b] + start + x[a][b + 1:]    

def pos_free(pos):
    global index_grid, x
    z=index_grid[pos]
    test=x[z[0]][z[1]]
    if test != "X" and test !="O":
        return True
    else:
        return False    
            
def check_win():
    #print("moin")
    global x, s, index_grid, win_options, start_1, start_2
    win_options=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    p2_list=[]
    p1_list=[]
    for pos, [row, col] in index_grid.items():
        if x[row][col] == start_1:
            p1_list.append(pos)
        if x[row][col] == start_2:
            p2_list.append(pos)                                      
    for sublist in win_options:
        if all(element in p1_list for element in sublist):
            print("Player 1 won!")        
            play_again()                                 
        elif all(element in p2_list for element in sublist):
            print("Player 2 won!")        
            play_again()                                 
    if s == 9:
        print("It's a tie!")       
        play_again()
        
def play_again():
            r=input("Play again? (y/n): ").lower()
            if r == "y":
                os.system("clear")
                start()
            else:
                exit()
start()          