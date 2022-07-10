from breadth_first_search import breadth_first_solution
from greedy_search_best_first import best_first_solution
from A_Star_Search import astar_solution
import numpy as np
import json



x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
y = np.array([[1,2,3],[0,5,6],[4,7,8]])



if __name__ == '__main__':
    x = input("Enter the intial state of the game in flat row-wise manner-No Space--> Initial")
    initial = np.array(json.loads(x))
    y = input("Enter the goal state in a similar way --> Goal")
    goal = np.array(json.loads(y))
    breadth_first_solution(initial, goal)