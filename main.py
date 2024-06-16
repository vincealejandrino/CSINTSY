import heapq
def astar_search(graph, heuristic, start, goal):
    open_list = [(0, start)]  # (f-value, city)
    visited = set()
# Define the graph as an adjacency list
graph = {
    'Dallas': {'Miami': 1200, 'Los Angeles': 1700, 'New York': 1500},
    'Miami': {'Dallas': 1200, 'New York': 1000},
    'Los Angeles': {'Dallas': 1700, 'New York': 3000, 'San Francisco': 500},
    'New York': {'Dallas': 1500, 'Miami': 1000, 'Los Angeles': 3000, 'Boston': 250, 'Chicago': 800},
    'San Francisco': {'Los Angeles': 500, 'Chicago': 2200},
    'Boston': {'New York': 250},
    'Chicago': {'New York': 800, 'San Francisco': 2200}
}

# Define the heuristic values
heuristic = {
    'Miami': 2000,
    'New York': 800,
    'Boston': 900,
    'Dallas': 1200,
    'San Francisco': 2200,
    'Los Angeles': 2400,
    'Chicago': 0  # Goal city heuristic is 0
}

#user will define start and goal city with error handling
while True:
    startCity = input("Enter Start City: ")
    if startCity in graph:
        break
    else:
        print("Start City not found in the graph. Please enter a valid city.")

while True:
    goalCity = input("Enter Goal City: ")
    if goalCity in graph:
        break
    else:
        print("Goal City not found in the graph. Please enter a valid city.")

