#IMPORTING NEEDED LIBRARIES
import numpy as np
import time
import sys
import json


x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
y = np.array([[1,2,3],[0,5,6],[4,7,8]])

#test sets
x1 = np.array([[1, 3, 4], [8, 0, 5], [7, 2, 6]])
y1 = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

x2 = np.array([[1, 3, 4], [8, 6, 2], [0, 7, 5]])
y2 = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

x3 = np.array([[3, 6, 4], [0, 1, 2], [8, 7, 5]])
y3 = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

x4 = np.array([[4, 6, 0], [3, 5, 2], [1, 7, 8]])
y4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x5 = np.array([[4, 8, 3], [2, 7, 5], [1, 6, 0]])
y5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x6 = np.array([[0, 3, 6], [5, 7, 1], [2, 4, 8]])
y6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x7 = np.array([[7, 8, 0], [3, 2, 1], [6, 5, 4]])
y7 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x8 = np.array([[0, 5, 3], [4, 1, 6], [7, 2, 8]])
y8 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x9 = np.array([[4, 5, 2], [1, 0, 3], [8, 7, 6]])
y9 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x14 = np.array([[3,6,4],[0,1,2],[8,7,5]])
y14 = np.array([[1,2,3],[8,0,4],[7,6,5]])

x15 = np.array([[3, 5, 6], [1, 4, 8], [0, 7, 2]])
y15 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x16 = np.array([[8,7,6],[5,4,3],[2,1,0]])
y16 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])



#solvability check
s1 = np.array([[1,2,3],[4,5,6],[8,7,0]])
s2 = np.array([[1,2,3],[4,5,6],[0,8,7]])
s3 = np.array([[5,2,8],[4,1,7],[0,3,6]])
s4 = np.array([[7,1,2],[5,0,9],[8,3,6]])

#*******************************************************************************
#Node Class
#*******************************************************************************
"""
This is the main node as a base class/data-structure we will be implementing. 
It constist of the node_no --> depth of node
                   data ---> board state
                   parent --> parent of the node
                   heuristic_cost --> for informed search
"""

class Node:
    def __init__(self, node_no, data, parent, heuristic_cost):
        self.data = data
        self.parent = parent
        self.node_no = node_no
        self.heuristic_cost = heuristic_cost

#*******************************************************************************
#Index-Finding Function
#*******************************************************************************
"""
The fucntion finds the index/position of the 'zero' in the board.
The input is: puzzel or 3*3 matrix
The output is : i = row & j = column - the coordinate of 0.
"""        
def find_index(puzzle):
    i, j = np.where(puzzle == 0)
    i = int(i)
    j = int(j)
    return i, j #return the index of the 3x3 matrix


#*******************************************************************************
#Left Move
#*******************************************************************************
"""
As the 0 can move in the four possible direction or less depending upon the
where it is located. The left move is only possible when the zero is in third(3) 
second column(2), it couldn't move left if it is in first(1) column

The function inputs : 3*3 matrix
             outputs: 3*3 matrix with repective move if available
"""

def left_move(data):
    i, j = find_index(data) #findind the index of the zero
    if j == 0: #if column is zero(meaning first column)
        return None #there is no movement
    else:
        temp_puz = np.copy(data) #create a temporary space
        mov_num = temp_puz[i, j-1] #the column decreses when the number moves 
                                   #left but row doesn't change so j(column) -1
        temp_puz[i, j] = mov_num #replacing the 0 with the moved value
        temp_puz[i, j-1] = 0 #making the moved value 0
        return temp_puz 

#*******************************************************************************
#Right Move
#*******************************************************************************
"""
For the right move, only for first(1) and second column(2) is possible NOT for 
the third column(3)

The function inputs : 3*3 matrix
             outputs: 3*3 matrix with repective move if available
"""

def right_move(data):
    i, j = find_index(data) #findind the index of the zero
    if j == 2: #if column is 2 (meaning third column)
        return None #No movement
    else:
        temp_puz = np.copy(data) 
        mov_num = temp_puz[i, j+1] 
        temp_puz[i, j] = mov_num 
        temp_puz[i, j+1] = 0 
        return temp_puz


#*******************************************************************************
#Up Move
#*******************************************************************************
"""
For the up move, only for second(2) and third(3) row is possible NOT for the 
first(1) row. 

The function inputs: 3*# matrix
             outputs: 3*3 matrix with respective move if available
"""
def up_move(data):
    i, j = find_index(data) #findind the index of the zero
    if i == 0: #if i(row) is 0 (meaning first row)
        return None #No movement 
    else:
        temp_puz = np.copy(data) 
        mov_num = temp_puz[i-1, j] 
        temp_puz[i, j] = mov_num 
        temp_puz[i-1, j] = 0 
        return temp_puz


#******************************************************************************
#Down Move
#******************************************************************************
"""
For the down move, only for second(2) and first(1) row is possible NOT for the 
third(3) row. 

The function inputs: 3*3 matrix
             outputs: 3*3 matrix with respective move if available
"""

def down_move(data):
    i, j = find_index(data) #findind the index of the zero
    if i == 2: #if i(row) is 2 (meaning third row)
        return None
    else:
        temp_puz = np.copy(data) 
        mov_num = temp_puz[i+1, j] 
        temp_puz[i, j] = mov_num 
        temp_puz[i+1, j] = 0 
        return temp_puz

#******************************************************************************
#All Possible Movement
#******************************************************************************
"""
This function combines all the movement and outputs the all possible movement
of the state.

The function inputs: 3*3 matrix 
             outputs: list of 3*3 matrix with all possible movement
"""
def move(data):
    
    mov_combination = list() #initialize empty list
    
    mov_combination.append(up_move(data)) 
    mov_combination.append(down_move(data))
    mov_combination.append(left_move(data))
    mov_combination.append(right_move(data))
    
    #filtering out the None
    output = list(filter(None.__ne__, mov_combination)) 

    return output


#******************************************************************************
#Solvable OR NOT
#******************************************************************************
"""
This function finds out if the initial state that is passed is solvable or not.
The solvability of puzzel can be found by counting the number of inversion pre-
sented in the initial state. 

INVERSION:
Given a board, an inversion is any pair of blocks i and j where i < j but i 
appears after j when considering the board in row-major order.

If a board has an odd number of inversions, then it cannot lead to the goal 
board by a sequence of legal moves because the goal board has an even number 
of inversions

More Info: https://tinyurl.com/PuzzelInversion


The function inputs: 3*3 matrix of initial state
             outputs: boolean value
"""
def solveable(check_data):
    """
    The check_data should be entered as 3*3 matrix
    """
    counter = 0 #initialize the empty counter to count inversion
    
    #flatten the 3*3 matrix
    flat_initial_state = np.array(check_data.flatten().tolist()) 
    
    #we will remove the zero from the list as it is not accounted for inversion
    notZero = flat_initial_state[flat_initial_state != 0]

    for i in range(len(flat_initial_state)): #for the every item 
        
        for j in range(i+1,8): #compare with number that comes after i
            
            #if the number in 'i' is greater than number that comes after it
            #and is not zero, then we count inversion.
            if notZero[j] < notZero[i]:
                counter += 1
                
            else:
                continue
    
    #if the number of inversion is even, it is solvable
    if counter % 2 == 0:
        return True
    else:
        return False

#******************************************************************************
#Breadth-First Search Algorithm Implementation
#******************************************************************************

"""
This is the main algo for the Breadth-First Search.
It inputs the initial state and goal state as 3*3 matrix and 
outputs : The solution node, all manipulated nodes, time
"""

def breadth_first_search(initial_state, goal_state):
    """
    Both initial_state and goal_state will be 3*3 matrix NOT 1*9 flat list.
    
    """
    start_time = time.time()
    
    
    #this is the root/parent node which is input. Since it is parent, the node-
    #number is zero. The huristic value and parent assignment is None. 
    root_parent = Node(0, initial_state, None, None)
    
    
    #this list stores all the nodes that are created in solving problem. Meaning
    #all the possible moves in each and every stage. 
    list_node = [root_parent]
    
    
    #this stores all the nodes that are checked 
    checked_nodes = []
    
    
    #this stores all the nodes that are created to stop checking the all the 
    #states that are already checked and no solution was found. This is no 
    #different than 'checked_node'. Just for programming purpose
    all_states = []
    
    
    #initializing the node counter that tracks the node depth
    node_counter = 0
    
    
    #looping over the infinite until the solution is found. 
    while list_node:
        
        #make the seperate variable that is first manipulated
        #The algo work on Queue data structure so we will manipualte the first-
        #node and remove it and go on another node
        current_node = list_node.pop(0)
        
        #if the item on the first Queue matches the goal then that's solution
        if current_node.data.tolist() == goal_state.tolist():
            
            #calculating the time taken
            end_time = time.time()
            total_time = end_time - start_time
            #*********************************
            
            return current_node, checked_nodes, total_time, all_states
        
        #if there is no match, we will move the current state to possible direction. 
        moved_spaces = move(current_node.data)
        
        #increses the node counter
        node_counter += 1
        
        
        for items in moved_spaces: #all the moves from current node
            
            #we will make all the moves as child nodes
            """
            For every child node:
                data = items/one of the possible moves
                parent = current node from which the moves are formed
                node no = node counter
                heuristic_cost = None
            """
            child_node = Node(node_counter, items, current_node, None)
            
            
            #we won't check state that is already checked before
            if child_node.data.tolist() not in all_states:
                
                #append the child node to our initial Queue
                list_node.append(child_node)
                
                #append the data to our 'all_state' list
                all_states.append(child_node.data.tolist())
                
                #also append in our checked_node 
                checked_nodes.append(child_node)
                
                #if the any child node match with goal that's solution
                if child_node.data.tolist() == goal_state.tolist():
                    
                    #calculating the time taken
                    end_time = time.time()
                    total_time = end_time - start_time
                    #*********************************
                    
                    return child_node, checked_nodes, total_time, all_states
                
    return None, None, None, None

#******************************************************************************
#Solution Path
#******************************************************************************
"""
The 'breadth_first_search' outputs the solution as Node data. So, this 
fucntion extracts all the ancestor node that led to the solution list

The function inputs node data which is child node and
outputs list of the states that led to solution. 

The function back-tracks the parent node from the end node.

In other words, it means it will output the moves needed to get the solution. 
"""

def solution_path(solution_node):
    #initialize empty list to store states
    path = []
    
    #first state would be solution
    path.append(solution_node.data.tolist())
    
    #the parent node is the parent value stored in 'solution_node' object
    parent_node = solution_node.parent
    
    #loop unitl parent node is available
    while parent_node:
        #append the state of the current parent node
        path.append(parent_node.data.tolist())
        
        #update the parent node to be the parent node of current node
        parent_node = parent_node.parent
        
    #final_path is the reversed of the path as we went from bottom to up
    final_path = list(reversed(path))
       
    return final_path


#******************************************************************************
#Input Check
#******************************************************************************
"""
This function checks the input status of the states. 

* If the states contains 0-8 range or not
* IF there are unique 0-8 range or not

"""

def input_check(initial_state, goal_state):
        
    #number list that should be in puzzel
    numb = [0,1,2,3,4,5,6,7,8] 
        
    #number list that are not in numb
    range_initial_state = [num for num in initial_state.flatten().tolist() if num not in numb]
    range_goal_state = [num for num in goal_state.flatten().tolist() if num not in numb]
        
        
    #checks if there are 9 unique digits are present or not
    if (len(np.unique(initial_state)) & len(np.unique(goal_state))) != 9:
        print("Do not repeat the number")
        return False
        
    #if the number list isn't zero meaning the state contains number except-
    #0-8 range
    if (len(range_initial_state) != 0) or (len(range_goal_state) != 0):
        print("Please enter the number ranging from 0-8")
        return False
        
    else:
        return True
            

#******************************************************************************
#Breadth-First Search Solution
#******************************************************************************
"""
This final function combine above function to give a user interactive solution.
"""

def breadth_first_solution(initial_state, goal_state):
    """
    The initial and goal state both are 3*3 matrix. 
    """
    #check function to validate input
    if input_check(initial_state, goal_state):
        
        soln_node, checkd_node, time, visited_state = breadth_first_search(initial_state, goal_state)
        
        #Finds the path to the solution as a list
        solution_states = solution_path(soln_node)
    
        for val, items in enumerate(solution_states):
            print(30*"*", "\n")
            print("Step No: ", val, "\n")
            print(np.reshape(items,(3,3)))
            print("\n")
            print(30*"*")
        
        print("\n\n")
        print("Solution Statistics: ")
        print("Total Time taken (In seconds): ", round(time,10))
        print("Total Number of State Searched: ", len(visited_state))
        print("Total Number of Steps: ", len(solution_states)-1)
        
    else:
        pass

# if __name__ == '__main__':
#     x = input("Enter the intial state of the game in flat row-wise manner-No Space")
#     x_arr = np.array(json.loads(x))
#     y = input("Enter the goal state in a similar way")
#     y_arr = np.array(json.loads(y))
#     breadth_first_solution(x_arr, y_arr)














