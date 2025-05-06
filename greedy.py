import heapq

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Sorted array:", arr)


def prims_algorithm_adj_list(adj_list, n):
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, vertex)
    total_weight = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight
        for v, w in adj_list[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                if weight != 0:
                    mst_edges.append((u, v, w))

    print("Edges in MST (Prim's):", mst_edges)
    print("Total MST cost (Prim's):", total_weight)


# --- Main Menu ---
while True:
    print("\n--- Greedy Algorithm Applications ---")
    print("1. Selection Sort")
    print("2. Prim's MST Algorithm")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        arr = list(map(int, input("Enter array elements (space-separated): ").split()))
        selection_sort(arr)

    elif choice == 2:
        n = int(input("Enter number of vertices: "))
        e = int(input("Enter number of edges: "))
        adj_list = {i: [] for i in range(n)}
        for _ in range(e):
            u, v, w = map(int, input("Enter edge (u v weight): ").split())
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))
        prims_algorithm_adj_list(adj_list, n)

    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")


# ### 🧠 **General Questions**

# **1. What are greedy algorithms? Give two examples.**
# **Answer:**
# Greedy algorithms make a series of choices by picking the best option at each step with the hope of finding the global optimum. They do not reconsider previous choices.
# **Examples:**

# * Prim's Algorithm for Minimum Spanning Tree
# * Kruskal’s Algorithm
# * Activity Selection
# * Selection Sort (though it's usually considered more of a basic sorting algorithm, it uses a greedy-like selection of the minimum at each step).

# ---

# ### 🔄 **Selection Sort**

# **6. Explain how selection sort works.**
# **Answer:**
# Selection sort works by dividing the array into a sorted and unsorted part. It repeatedly selects the smallest (or largest) element from the unsorted part and swaps it with the first element of that part. This process continues until the entire array is sorted.

# **7. What is the time complexity of selection sort and why?**
# **Answer:**
# The time complexity is **O(n²)** because for each element, we find the minimum in the remaining part of the array, which takes O(n), and this is done n times.

# **8. Is selection sort a stable sorting algorithm?**
# **Answer:**
# No, it is **not stable** by default because equal elements can be swapped, changing their original order.

# ---

# ### 🌲 **Prim’s Algorithm**

# **12. What is Prim's algorithm used for?**
# **Answer:**
# Prim's algorithm is used to find the **Minimum Spanning Tree (MST)** of a connected, weighted, undirected graph. It ensures the total edge weight of the spanning tree is minimized.

# **14. Why is a min-heap used in Prim's algorithm?**
# **Answer:**
# A min-heap allows us to efficiently extract the vertex with the minimum edge weight, which helps select the next optimal edge in O(log n) time.

# **15. What is the significance of the `visited[]` array?**
# **Answer:**
# The `visited[]` array ensures that once a vertex is included in the MST, it is not processed again. This prevents cycles and redundant calculations.

# **18. What is the time complexity of Prim's algorithm using a min-heap and adjacency list?**
# **Answer:**
# The time complexity is **O((V + E) log V)**, where V is the number of vertices and E is the number of edges. The log V comes from the heap operations.

# ---

# ### 🧩 **Code Logic / Implementation**

# **20. Why do you check `if weight != 0:` before appending to `mst_edges`?**
# **Answer:**
# This check avoids adding the initial dummy edge `(0, 0, 0)` from the min-heap when starting the algorithm. It ensures only actual MST edges are stored.

# **22. Explain the structure of the `adj_list`.**
# **Answer:**
# `adj_list` is a dictionary where each key is a vertex, and the value is a list of tuples. Each tuple represents an adjacent vertex and the weight of the connecting edge.

# ```python
# # Example:
# adj_list = {
#   0: [(1, 2), (3, 6)],
#   1: [(0, 2), (2, 3)],
#   ...
# }
# ```

# ---

# ### 💻 **Input / Output**

# **26. What will happen if the graph is disconnected?**
# **Answer:**
# Prim’s algorithm assumes a connected graph. If the graph is disconnected, the algorithm will not visit all vertices, and the MST will be incomplete.

# **27. Can this code handle negative edge weights? Why or why not?**
# **Answer:**
# Yes, Prim’s algorithm can handle **negative edge weights** as long as the graph has no negative weight cycles (which isn’t an issue in MST problems). The min-heap still correctly selects the minimum available weight.

# 25. What inputs does your code require for Prim’s algorithm?
# Answer:

# Number of vertices n

# Number of edges e

# Then e lines of edges in the form: u v w where u and v are vertices and w is the edge weight.

# 28. What will be the output for a graph with only one vertex?
# Answer:
# The MST will have no edges, and the total cost will be 0.

# 29. How does your code behave if duplicate edges are provided?
# Answer:
# Both duplicates will be added to the adjacency list. The min-heap will still pick the edge with the least weight due to its priority behavior, but redundant edges can slightly increase the number of operations.

