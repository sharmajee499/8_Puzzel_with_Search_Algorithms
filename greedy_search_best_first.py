#******************************************************************************
#Importing Needed Libraries
#******************************************************************************
import numpy as np
import time
from scipy.spatial import distance #for manhattan distance
import json

from breadth_first_search import Node
from breadth_first_search import move
from breadth_first_search import solution_path
from breadth_first_search import input_check

#test sets

#works
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
y = np.array([[1, 2, 3], [0, 5, 6], [4, 7, 8]])

# x = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
# y = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

#works
x1 = np.array([[1, 3, 4], [8, 0, 5], [7, 2, 6]])
y1 = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

#works
x2 = np.array([[1, 3, 4], [8, 6, 2], [0, 7, 5]])
y2 = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

#don't work
x3 = np.array([[3, 6, 4], [0, 1, 2], [8, 7, 5]])
y3 = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

#don't work
x4 = np.array([[4, 6, 0], [3, 5, 2], [1, 7, 8]])
y4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x5 = np.array([[4,8,3],[2,7,5],[1,6,0]])
y5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x6 = np.array([[0, 3, 6], [5, 7, 1], [2, 4, 8]])
y6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x7 = np.array([[7, 8, 0], [3, 2, 1], [6, 5, 4]])
y7 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x8 = np.array([[0, 5, 3], [4, 1, 6], [7, 2, 8]])
y8 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x9 = np.array([[4, 5, 2], [1, 0, 3], [8, 7, 6]])
y9 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x10 = np.array([[1, 2, 3], [4, 0, 5], [7, 8, 6]])
y10 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

#take longer time
x11 = np.array([[8, 7, 6], [5, 4, 3], [2, 1, 0]])
y11 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x12 = np.array([[3,5,6],[1,4,8],[0,7,2]])
y12 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

#works
x13 = np.array([[1,2,3],[0,4,6],[7,5,8]])
y13 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

#works
x14 = np.array([[3,6,4],[0,1,2],[8,7,5]])
y14 = np.array([[1,2,3],[8,0,4],[7,6,5]])

#******************************************************************************
#Manhattan Distance Calculation
#******************************************************************************
"""
It calculate the manhattan distance between the starting state and 
upcoming state. 

The input is : initial_state and goal_state(upcoming state)
The output is : distance (integer)
"""
def manhattan_distance(initial_state, goal_state):
    """
    The initial and goal state are 3*3 matrix NOT a flat list. 
    """
    #possible integer in the game board
    possible_val = [1,2,3,4,5,6,7,8,0]
    
    #initializing the distance(output) with 0.
    dist = 0
    
    #looping over all the possible value to find distance between intial and
    #goal state
    for i in range(len(possible_val)):
        #if 0 skip
        if possible_val[i] == 0:
            continue
        else:
            #finding the co-ordinates of the given value in initial state
            i1, j1 = np.where(initial_state == possible_val[i])
            #finding the co-ordinates of the given value in final state
            i2, j2 = np.where(goal_state == possible_val[i])
            
            #converting the point to integer format for calculation
            point1 = [int(i1), int(j1)]
            point2 = [int(i2), int(j2)]
            
            #calculating distance and adding to the dist function to get total
            #distance
            dist += distance.cityblock(point1, point2)
            
    return dist

#******************************************************************************
# Misplaced Tiles Calculation
#******************************************************************************
"""
This function calculates the number of misplace tiles in the current state and 
the goal state.

The input is : 3*3 matrix of the current state and the goal state
The output is : number of misplaced tiles/incorrect tiles
"""  

def misplaced_tiles(state, goal_state):
    
    #initialize the counter
    incorrect_tile = 0
    
    #looping through all the tiles except zero
    for i in range(8):
        
        #coordinates of number in starting state, i+1 means starting from 1
        j1, k1 = np.where(state == (i+1))
        
        #coordinate of number/tile in goal state
        j2, k2 = np.where(goal_state == (i+1))
        
        #comparing the co-ordinates
        if (j1 == j2) & (k1 == k2):
            continue
        else:
            incorrect_tile += 1
            
    return incorrect_tile

    
#******************************************************************************
# Best-First Search Algorithm Implementation (Greedy)
#******************************************************************************

"""
This is the main algo for the Best-First Search.
It inputs the initial state and goal state as 3*3 matrix and 
outputs : The solution node, all manipulated nodes, time
"""

def best_first_search(initial_state, goal_state):
    """
    Both initial state and goal state will be 3*3 matrix NOT 1*9 flat list
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
    
    #Depth Counter for Nodes
    node_counter = 0
    
    while list_node:
        
        #make the seperate variable that is first manipulated
        #The algo work on Queue data structure so we will manipualte the first-
        #node and remove it and go on another node
        current_node = list_node.pop(0)

        """
        In below statement, the manhattan distance are counted and if they equal
        zero we have our goal state. 
        """
        if misplaced_tiles(current_node.data, goal_state) == 0:
            
            #calculating the time taken
            end_time = time.time()
            total_time = end_time - start_time
            #*********************************
            
            #add the node to checked node
            checked_nodes.append(current_node)
            
            #add the value of the node to 'all_states'
            all_states.append(current_node.data.tolist())

            
            return current_node, checked_nodes, total_time, all_states
        
        #if there is no match, we will move the current state in possible direction
        moved_spaces = move(current_node.data)
        
        """
        The variables: 'compare_nodes' & 'misplaced_tile' will help to decide
        which state to choose when there is same heuristic value. On those
        situation, we grow the node of state which has same minimun heuristic
        value and again check the heuristic of the grown tree and will follow 
        that node. 
        """
        compare_nodes = []
        man_dist_list = []
        
        #increase the node counter
        node_counter += 1
        
        
        #make the posssible move for all needed 
        for items in moved_spaces:
            
            #calculating number of misplaced tiles
            no_of_misplaced = misplaced_tiles(items, goal_state)
            
            #manhattan distance
            # man_dist = manhattan_distance(items, goal_state)
            
            #Making all the moves as child node with their respective value
            child_node = Node(node_counter, np.array(items), current_node, no_of_misplaced)
            
            #checking if an of those child have goal state
            if child_node.heuristic_cost == 0:
                
                #calculating the time taken
                end_time = time.time()
                total_time = end_time - start_time
                #*********************************
                
                checked_nodes.append(child_node)
                all_states.append(child_node.data.tolist())

                return child_node, checked_nodes, total_time, all_states
            
            #We will only add the nodes that aren't explored before.
            if child_node.data.tolist() not in all_states:
                
                #append to list to compare minimum heuristic value
                compare_nodes.append(child_node)
                man_dist_list.append(child_node.heuristic_cost)
                
                #added to the checked state
                all_states.append(child_node.data.tolist())
                
                #added to checked node
                checked_nodes.append(child_node)
         
            
        #this loop find the minimum heuristic values on child nodes    
        for i in range(len(man_dist_list)):
            
            if man_dist_list[i] == min(man_dist_list):
                
                #adding the nodes that have minimum value in the children to queue.
                list_node.append(compare_nodes[i])
        
                # all_states.append(compare_nodes[i].data.tolist())
                # checked_nodes.append(compare_nodes[i])
                    
    return None, None, None, None


#******************************************************************************
#Best-First Search Solution (Greedy)
#******************************************************************************
"""
This final function combine above function to give a user interactive solution.
Majority of the functions are imported from 'breadth_first_search.py'
"""

def best_first_solution(initial_state, goal_state):
    """
    The initial and goal state both are 3*3 matrix. 
    """
    #check function to validate input
    if input_check(initial_state, goal_state):
        
        soln_node, checkd_node, time, visited_state = best_first_search(initial_state, goal_state)
        
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
#     best_first_solution(x_arr, y_arr)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    