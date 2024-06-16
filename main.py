import heapq

def astar_search(graph, heuristic, start, goal):
    open_list = [(0, start)]  # (f-value, city)
    visited = set()
    g_values = {city: float('inf') for city in graph}
    g_values[start] = 0
    came_from = {}

    while open_list:
        current_cost, current_city = heapq.heappop(open_list)

        if current_city == goal:
            path = []
            while current_city in came_from:
                path.append(current_city)
                current_city = came_from[current_city]
            path.append(start)
            path.reverse()
            return path, current_cost

        if current_city in visited:
            continue

        visited.add(current_city)

        for neighbor, cost in graph[current_city].items():
            tentative_g = g_values[current_city] + cost
            if tentative_g < g_values[neighbor]:
                g_values[neighbor] = tentative_g
                f_value = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_value, neighbor))
                came_from[neighbor] = current_city

    return None, float('inf')  # No path found

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

path, total_cost = astar_search(graph, heuristic, startCity, goalCity)
if path:
    print("Optimal Path:", path)
    print("Total Cost:", total_cost)
else:
    print(f"No path found from {startCity} to {goalCity}.")