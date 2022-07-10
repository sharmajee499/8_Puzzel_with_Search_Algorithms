# 8 Puzzel Game with Graph Search 

The 8-puzzel is a classic game developed by Noyes Palmer Chapman in the 1870s . 
The puzzle consists of a 3x3 grid, that consists of number from 1 to 8 on each 
tile. One of the tiles is blank or 0, that can be slid within the grid. The tile only can be moved in the blank space/square. The start of the puzzle can be any configurations as shown in the Figure 1. Since we are playing the 8-puzzel in 
order to gauge the algorithms performance, the goal state also can be any configurations. However, in general, the goal state looks like as in the 
below Figure 2. The objective is to find the needed steps to get from initial state 
to the goal state. The blank tile can be moved in the up, down, left, and right direction. It couldn’t be moved diagonally, and we can only take one step 
at a time

![Initial and Goal State](https://github.com/sharmajee499/8_Puzzel_with_Search_Algorithms/blob/master/img/initial_goal_state.png)

### Algorithms Implemented:
1. [Breadth First Search](https://en.wikipedia.org/wiki/Breadth-first_search)
2. [Best-First Search](https://en.wikipedia.org/wiki/Best-first_search#:~:text=Best%2Dfirst%20search%20is%20a,according%20to%20a%20specified%20rule.)
3. [A* Search](https://en.wikipedia.org/wiki/A*_search_algorithm)

### Emperical Results from the Respective Algorithms

The below picture shows the performance and efficiency of the respective
algorithm. A* is the complete as well as optimal algorithm as compared to other
two. 

![emperical result](https://github.com/sharmajee499/8_Puzzel_with_Search_Algorithms/blob/master/img/emperical_result.png)

*Note: The time may vary depending upon the machine/computer*

### How to Run the script in your local computer?

#### Step 1: Create a new conda enviroment on your local machine and activate. 

#### Step 2: Clone this repo

#### Step 3: Install the needed packages from 'requirements.txt' on your conda enviroment
Run the below code in your newly created conda enviroment
```
pip install -r requirements.txt
```
#### Step 4: Run `main.py` file 
- Open the command prompt/terminal/poweshell
- Open `main.py`
  - For Cmd Prompt/Powershell users use: `& C:/Anaconda/envs/YOUR NEW CREATED ENV/python.exe -i c:/Users/Sande/../main.py`
  - *Note: The `-i` in above code runs the python file with the interractive window*
- Follow the prompt and enter the initial and goal state that you desire. 
  - Note: The initial and goal state takes the 3*3 matrix format input. For instance: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
- It will show the result for **breadth first search**

#### Step 5: Running different search methods
Since the file is opened in interractive window, we can use the function that are defined on the scripts file. Use the below function:
- Breadth First Search: `breadth_first_solution(initial, goal)`
- Best First Search: `best_first_solution(initial, goal)`
- A* Search: `astar_solution(initial, goal)`

*Note: `initial` and `goal` are already defined when you input the values after running `main.py'.*

#### Step 6: Running Algos with other `initial` and `goal` value

Since, we are in python terminal, we can again define the `initial` and `goal` variable like this:
```python
initial = np.array([[Your initial value]])
goal = np.array([[your goal value]])
```
Now, again you can call the search functions as in Step 5. 


### Running in [Replit](https://replit.com/~)

You can run the same scripts in the Replit without creating the conda enviroment in your local machine. 

- Open the [link](https://replit.com/join/bqnzpmqjed-sharmajee499)
- Go to the `main.py` file.
- Input ypur value in `initial` and `goal` variable in the script. 
- Click the **Run** button on the top. 
- Follow the procedure of Step 5 in the console on side bar. 


### Additional test sets

You can find the additional test set on the `test_set.txt` file on the repo. 

### Advisory:

Please be aware while inputting value. From the emperical result graph you saw that some of the inputs takes huge amount of time. It might also kill the memory in some instances. So, choose the input carefully. 




