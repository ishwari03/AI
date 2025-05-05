def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def print_board(board, n):
    for i in range(n):
        row = ['Q' if j == board[i] else '.' for j in range(n)]
        print(' '.join(row))
    print("\n")

def solve_backtracking(board, row, n, count):
    if row == n:
        count[0] += 1
        print(f"Solution {count[0]} (Backtracking):")
        print_board(board, n)
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_backtracking(board, row + 1, n, count)
            board[row] = -1

def solve_branch_bound(n, count):
    board, columns, diag1, diag2 = [-1] * n, set(), set(), set()

    def backtrack(row):
        if row == n:
            count[0] += 1
            print(f"Solution {count[0]} (Branch and Bound):")
            print_board(board, n)
            return
        for col in range(n):
            if col in columns or (row - col) in diag1 or (row + col) in diag2:
                continue
            # Add the current column and diagonals
            board[row] = col
            columns.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            backtrack(row + 1)

            # Backtrack: Remove the current column and diagonals
            board[row] = -1
            columns.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)

def n_queens(n):
    count_backtrack, count_branch_bound = [0], [0]
    print("Solutions using Backtracking:")
    solve_backtracking([-1] * n, 0, n, count_backtrack)
    print(f"Total Backtracking solutions: {count_backtrack[0]}")

    print("\nSolutions using Branch and Bound:")
    solve_branch_bound(n, count_branch_bound)
    print(f"Total Branch and Bound solutions: {count_branch_bound[0]}")

n = int(input("Enter the number of queens: "))
n_queens(n)



# ### 🔹 **Basic Understanding**

# 1. **What is the N-Queens problem?**
#    ➤ It is a problem of placing `n` queens on an `n x n` chessboard so that no two queens attack each other — i.e., no two in the same row, column, or diagonal.

# 2. **What is Backtracking?**
#    ➤ Backtracking is a method of solving problems by trying partial solutions and then undoing ("backtracking") when we hit a dead end.

# 3. **What is Branch and Bound?**
#    ➤ Branch and Bound is an optimization of backtracking that prunes branches (choices) early if they are guaranteed not to lead to a solution.

# ### 🔹 **Algorithm-Specific**

# 4. **How does Backtracking solve N-Queens?**
#    ➤ It places a queen row by row, checking if it is safe. If placing a queen causes conflict later, it backtracks and tries a different position.

# 5. **What’s the difference between Backtracking and Branch and Bound in this problem?**
#    ➤ Both use recursive methods. Branch and Bound uses sets to quickly check if a column or diagonal is already under attack, which makes it faster.

# 6. **What data structures are used in Branch and Bound?**
#    ➤ Sets to store `columns`, `diag1 (row - col)`, and `diag2 (row + col)`.

# 7. **What is the time complexity of the N-Queens problem?**
#    ➤ Worst-case: **O(N!)** for Backtracking. Branch and Bound can improve performance in practice but has the same worst-case complexity.

# ---

# ### 🔹 **Coding and Logic**

# 8. **What does `abs(board[i] - col) == abs(i - row)` mean?**
#    ➤ It checks if two queens are on the same diagonal.

# 9. **Why do we reset `board[row] = -1` after recursive call?**
#    ➤ This is part of the backtracking process — to undo a move before trying the next column.

# 10. **What happens if no safe column is found in a row?**
#     ➤ The function backtracks to the previous row and tries a different column.

# ---

# ### 🔹 **Advanced / Tricky**

# 11. **Can we use the same algorithm for N-Rooks?**
#     ➤ Yes, but N-Rooks only need to avoid rows and columns, not diagonals — making it simpler.

# 12. **What happens if `n=2` or `n=3`?**
#     ➤ No solutions exist for 2 or 3 queens.

# 13. **Why do we use `row - col` and `row + col` in Branch and Bound?**
#     ➤ They uniquely represent the two diagonals on a chessboard.

# 14. **Is this problem NP-complete?**
#     ➤ No, N-Queens is not NP-complete. It can be solved in polynomial time for many practical values of `n` using smart algorithms.

# 15. **How many solutions are there for 4 queens?**
#     ➤ There are **2 unique solutions** for 4 queens.

# ---

# Would you like flashcards or a printable PDF for last-minute revision?
