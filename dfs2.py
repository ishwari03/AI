graph = {}
n = int(input("Enter the number of nodes in the graph: "))
print("Enter the edges (e.g., '0 1' for an edge between 0 and 1). Type 'done' to finish:")

while True:
    edge = input()
    if edge.lower() == 'done':
        break
    u, v = edge.split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)  # Undirected graph

# DFS function (recursive)
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# BFS function (iterative)
def bfs(graph, start_node):
    visited = set()
    queue = [start_node]
    visited.add(start_node)

    while queue:
        node = queue.pop(0)
        print(node, end=' ')

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Start traversal
start_node = input("Enter the starting node: ")
print("\nDepth-First Search (DFS):")
dfs(set(), graph, start_node)

print("\n\nBreadth-First Search (BFS):")
bfs(graph, start_node)

# Enter the number of nodes in the graph: 5
# Enter the edges (e.g., '0 1' for an edge between 0 and 1). Type 'done' to finish:
# 0 1
# 0 2
# 1 3
# 1 4
# done
# Enter the starting node: 0

# Depth-First Search (DFS):
# 0 1 3 4 2

# Breadth-First Search (BFS):
# 0 1 2 3 4

# ## 🧠 **Basic Viva Questions**
# ### 1. **What is Depth First Search (DFS)?**
# DFS is a graph traversal algorithm that explores as far as possible along one branch before backtracking.

# ### 2. **What is Breadth First Search (BFS)?**
# BFS is a graph traversal algorithm that explores all the neighbors of a node before moving to the next level.

# ### 3. **What data structure is used in DFS?**
# DFS uses a **stack** (implicitly via recursion).

# ### 4. **What data structure is used in BFS?**
# BFS uses a **queue** to keep track of nodes to visit.

# ### 5. **Which traversal is better for finding the shortest path?**
# **BFS** is better for finding the shortest path in an **unweighted graph**.

# ### 6. **Is your graph directed or undirected?**
# It is an **undirected** graph (both directions are added in adjacency list).

# ### 7. **What is the time complexity of DFS and BFS?**
# Both DFS and BFS have a time complexity of **O(V + E)**, where:
# * V = number of vertices
# * E = number of edges

# ### 8. **How do you handle visited nodes?**
# We use a **set called `visited`** to track nodes that have already been visited.

# ### 9. **What will happen if we don’t mark nodes as visited?**
# It can lead to an **infinite loop** or revisiting nodes unnecessarily.

# ### 10. **What are some real-life applications of DFS and BFS?**

# * **DFS:** Solving mazes, puzzles, cycle detection.
# * **BFS:** Shortest path in navigation, social network friend suggestions.

# ### 11. **What is the base case for DFS recursion?**
# The base case is when a node is already in the visited set.

# ### 12. **Why do we use adjacency lists instead of adjacency matrices?**
# Adjacency lists are **more memory-efficient** for sparse graphs (less edges).

# ### 13. **Can DFS and BFS be used on trees?**
# Yes, trees are a special type of graph. Both algorithms work on trees as well.

# ### 14. **What is the difference between a tree and a graph?**
# * A **tree** is a connected graph with no cycles.
# * A **graph** may have cycles and need not be connected.

# ### 15. **Why is BFS implemented iteratively and DFS recursively?**
# * BFS needs a **queue** to maintain order — best done iteratively.
# * DFS naturally fits **recursion** due to its depth-oriented behavior.


