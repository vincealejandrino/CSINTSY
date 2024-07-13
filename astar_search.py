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

def show_guidelines():
    guidelines = """
    Guidelines:
    1. Enter the start city when prompted. Ensure the city is available in the graph.
    2. Enter the goal city when prompted. Ensure the city is available in the graph.
    3. Enter the heuristic values for each city except the goal city. Heuristic values should be numeric.
    4. The program will compute and display the optimal path and total cost from the start city to the goal city.
    5. If no path is found, the program will inform you accordingly.
    """
    print(guidelines)

def menu():
    print("\n--Navigate Beyond!--\nPrecision Guidance for Boundless Adventures..\n")
    print("1. Let's explore!")
    print("2. Guidelines")
    print("3. Exit\n")

graph = {
    'Dallas': {'Miami': 1200, 'Los Angeles': 1700, 'New York': 1500},
    'Miami': {'Dallas': 1200, 'New York': 1000},
    'Los Angeles': {'Dallas': 1700, 'New York': 3000, 'San Francisco': 500},
    'New York': {'Dallas': 1500, 'Miami': 1000, 'Los Angeles': 3000, 'Boston': 250, 'Chicago': 800},
    'San Francisco': {'Los Angeles': 500, 'Chicago': 2200},
    'Boston': {'New York': 250},
    'Chicago': {'New York': 800, 'San Francisco': 2200}
}


def compute_total_cost():
    print("\n\n--Where do you want to go?--\n")
    while True:
        startCity = input("\nEnter Start City: ")
        if startCity in graph:
            break
        else:
            print("\n[Start City not found in the graph. Please enter a valid city.]")

    while True:
        goalCity = input("Enter Goal City: ")
        if goalCity in graph:
            break
        else:
            print("\n[Goal City not found in the graph. Please enter a valid city.]")

    print("\n")
     # Define the heuristic values
    heuristic = {}
    for city in graph:
        if city != goalCity:
            while True:
                try:
                    heuristic[city] = float(input(f"Enter heuristic value for {city}: "))
                    break
                except ValueError:
                    print("Please enter a valid numeric value.")

    heuristic[goalCity] = 0  # Goal city heuristic is 0

    path, total_cost = astar_search(graph, heuristic, startCity, goalCity)
    if path:
        print("\nOptimal Path:", path)
        print("\nTotal Cost:", total_cost,("\n"))
    else:
        print(f"No path found from {startCity} to {goalCity}.")

def exit_program():
    print("\nExiting the program...")
    print("\nEnjoy and Stay Safe!\n\n")
    exit()

switch_dict = {
    '1': compute_total_cost,
    '2': show_guidelines,
    '3': exit_program
}

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice: ")
        action = switch_dict.get(choice)
        if action:
            action()
        else:
            print("\nInvalid choice. Please select a valid option.")
