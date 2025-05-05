def get_graph_input():
    graph = {}
    nodes = input("Enter all node names (space-separated): ").strip().upper().split()

    for node in nodes:
        graph[node] = []

    num_edges = int(input("Enter number of edges: "))
    print("Enter each edge in the format: from to weight")
    for _ in range(num_edges):
        u, v, w = input().strip().upper().split()
        w = float(w)
        graph[u].append((v, w))
    
    return graph, nodes

def get_heuristic_input(nodes):
    heuristic = {}
    print("Enter heuristic values for each node (example: A 3.5):")
    for node in nodes:
        h = float(input(f"Heuristic for {node}: "))
        heuristic[node] = h
    return heuristic

def a_star(start, goal, graph, heuristic):
    open_set = {start}
    closed_set = set()
    g_cost = {start: 0}
    parent = {start: None}

    while open_set:
        current = min(open_set, key=lambda node: g_cost[node] + heuristic.get(node, float('inf')))
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            print("Path found:", " -> ".join(path[::-1]))
            return

        open_set.remove(current)
        closed_set.add(current)

        for neighbor, weight in graph.get(current, []):
            if neighbor in closed_set:
                continue

            tentative_g = g_cost[current] + weight
            if neighbor not in open_set or tentative_g < g_cost.get(neighbor, float('inf')):
                g_cost[neighbor] = tentative_g
                parent[neighbor] = current
                open_set.add(neighbor)

    print("Path does not exist!")

# ---- Main Program ----
graph, nodes = get_graph_input()
heuristic = get_heuristic_input(nodes)

start = input("Enter START node: ").strip().upper()
goal = input("Enter GOAL node: ").strip().upper()

if start not in graph or goal not in graph:
    print("Invalid start or goal node.")
else:
    a_star(start, goal, graph, heuristic)
