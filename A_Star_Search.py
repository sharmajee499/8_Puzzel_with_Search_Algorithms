#******************************************************************************
#Importing Needed Libraries
#******************************************************************************
import numpy as np
import time
from scipy.spatial import distance #for manhattan distance
import json

from greedy_search_best_first import manhattan_distance
from breadth_first_search import Node
from greedy_search_best_first import misplaced_tiles
from breadth_first_search import move
from breadth_first_search import input_check
from breadth_first_search import solution_path

# Test set
x1 = np.array([[1, 3, 4], [8, 0, 5], [7, 2, 6]])
y1 = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

x7 = np.array([[7, 8, 0], [3, 2, 1], [6, 5, 4]])
y7 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x8 = np.array([[0, 5, 3], [4, 1, 6], [7, 2, 8]])
y8 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x9 = np.array([[4, 5, 2], [1, 0, 3], [8, 7, 6]])
y9 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x11 = np.array([[8, 7, 6], [5, 4, 3], [2, 1, 0]])
y11 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x12 = np.array([[3,5,6],[1,4,8],[0,7,2]])
y12 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

x13 = np.array([[3,0,2],[6,5,1],[4,7,8]])
y13 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
#******************************************************************************
# A* Search Algorithm (heuristic search)
#******************************************************************************      

def astar_search(initial_state, goal_state):
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
    
    
    node_counter = 0
    
    while list_node:
        
        #make the seperate variable that is first manipulated
        #The algo work on Queue data structure so we will manipualte the first-
        #node and remove it and go on another node
        current_node = list_node.pop(0)
        
        """
        Check if the current node is equal to goal state
        """
        
        if current_node.data.tolist() == goal_state.tolist():
            
            #calculating the time taken
            end_time = time.time()
            total_time = end_time - start_time
            #*********************************
            
            #print(current_node.heuristic_cost)
            
            checked_nodes.append(current_node)
            all_states.append(current_node.data.tolist())

            
            return current_node, checked_nodes, total_time, all_states
        
        #if there is no match, we will move the current state
        moved_spaces = move(current_node.data)
        
        """
        The variables: 'compare_nodes' & 'misplaced_tile' will help to decide
        which state to choose when there is same heuristic value. On those
        situation, we grow the node of state which has same minimun heuristic
        value and again check the heuristic of the grown tree and will follow 
        that node. 
        """
        
        compare_nodes = []
        heuristic_list = []
        
        #incrementing the node count
        node_counter += 1
        
        for items in moved_spaces:
            
            #calculating the heuristic fucntion
            heuristic_func = manhattan_distance(items, goal_state) + node_counter
            #heuristic_func = misplaced_tiles(items, goal_state) + node_counter
            
            #Making all the moves as child node with their respective value
            child_node = Node(node_counter, np.array(items), current_node, heuristic_func)
            
            # checking if an of those child have goal state
            if child_node.data.tolist() == goal_state.tolist():
                
                #calculating the time taken
                end_time = time.time()
                total_time = end_time - start_time
                #*********************************
                
                checked_nodes.append(child_node)
                all_states.append(child_node.data.tolist())
                
                return child_node, checked_nodes, total_time, all_states
            
            
            #Adding the child nodes 'compare_nodes' to check heuristic val of 
            #all child nodes along with their heuristic value on 'misplaced_list'
            
                
            if child_node.data.tolist() not in all_states:
                
                compare_nodes.append(child_node)
                heuristic_list.append(child_node.heuristic_cost)
                
                all_states.append(child_node.data.tolist())
                checked_nodes.append(child_node)           
                

            # compare_nodes.append(child_node)
            # heuristic_list.append(child_node.heuristic_cost)
        

        for i in range(len(heuristic_list)):
    
            if heuristic_list[i] == min(heuristic_list):

                list_node.append(compare_nodes[i])


    return None, None, None, None



def astar_solution(initial_state, goal_state):
    """
    The initial and goal state both are 3*3 matrix. 
    """
    #check function to validate input
    if input_check(initial_state, goal_state):
        
        soln_node, checkd_node, time, visited_state = astar_search(initial_state, goal_state)
        
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
#     astar_search(x_arr, y_arr)
    
    
