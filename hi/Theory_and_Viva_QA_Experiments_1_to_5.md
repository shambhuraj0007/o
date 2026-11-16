# LP III – Theory, Algorithms and Viva Questions (Experiments 1–5)

Answers are written in simple English for practical examination preparation.

---

# Experiment 1: Fibonacci Series Using Recursive and Non-Recursive Methods

## Aim
Write a Python program to calculate Fibonacci numbers using recursive and non-recursive methods and analyze their time and space complexity.

## Theory
The Fibonacci series is a sequence in which each number is the sum of the previous two numbers.
Example: 0, 1, 1, 2, 3, 5, 8, 13.
F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2).

Recursion means a function calls itself. Iteration means repeating statements using a loop.

## Algorithm
1. Read the number of terms.
2. For the iterative method, initialize a=0 and b=1.
3. Print a and update a,b to b,a+b for each term.
4. For the recursive method, return n when n<=1.
5. Otherwise return Fibonacci(n-1) + Fibonacci(n-2).
6. Print the required terms and compare complexity.

## Complexity
- Iterative time: O(n); auxiliary space: O(1).
- Simple recursive time: O(2^n) upper bound; recursion stack: O(n).

## Conclusion
The Fibonacci series is generated using both iterative and recursive methods. The iterative method is more efficient for this implementation.

## Viva Questions and Answers
1. **What is an algorithm?** A step-by-step procedure to solve a problem.
2. **What is the Fibonacci series?** A series where each term is the sum of the previous two terms.
3. **What is recursion?** A function calling itself.
4. **What is iteration?** Repeating instructions using loops.
5. **What is a base condition?** The condition that stops recursive calls.
6. **What is the base condition in this program?** `n <= 1`.
7. **What is time complexity?** A measure of how running time grows with input size.
8. **What is space complexity?** A measure of memory used by an algorithm.
9. **What is iterative Fibonacci time complexity?** O(n).
10. **What is simple recursive Fibonacci time complexity?** O(2^n) upper bound.
11. **Which method uses less auxiliary memory?** The iterative method, O(1).
12. **Which Python function accepts keyboard input?** `input()`.

---

# Experiment 2: Huffman Encoding Using Greedy Strategy

## Aim
Implement Huffman Encoding using a Greedy Strategy to generate binary codes based on character frequencies.

## Theory
Huffman Encoding is a lossless data compression technique. Characters with higher frequencies generally receive shorter codes, while less frequent characters receive longer codes. The algorithm repeatedly combines the two nodes with the smallest frequencies to build a binary tree.

A min-heap helps retrieve the two smallest-frequency nodes efficiently. In the generated tree, moving left adds 0 and moving right adds 1.

## Algorithm
1. Read a non-empty string.
2. Count the frequency of each character.
3. Insert one leaf node per character into a min-heap.
4. Remove the two nodes with the smallest frequencies.
5. Create a parent node with their combined frequency.
6. Attach the removed nodes as left and right children.
7. Insert the parent node back into the heap.
8. Repeat until one root node remains.
9. Traverse the tree: left adds 0, right adds 1.
10. Display each character and its code.

## Complexity
Let n be the input length and k be the number of distinct characters.
- Frequency counting: O(n).
- Heap construction and merging: O(k log k).
- Overall: O(n + k log k).
- Tree and code storage: O(k).

## Conclusion
Huffman Encoding generates prefix-free binary codes based on character frequencies and can reduce the number of bits needed to represent data.

## Viva Questions and Answers
1. **What is Huffman Encoding?** A lossless compression method that assigns variable-length binary codes to characters.
2. **What is data compression?** Reducing the amount of data needed to store or transmit information.
3. **Which strategy does Huffman use?** Greedy strategy.
4. **Why is it greedy?** It repeatedly combines the two lowest-frequency nodes.
5. **What is frequency?** The number of times a character occurs.
6. **What is a min-heap?** A heap where the smallest-priority value is at the top.
7. **Why use a min-heap?** To efficiently retrieve the two lowest-frequency nodes.
8. **What is a Huffman tree?** A binary tree used to generate Huffman codes.
9. **What is a leaf node?** A node with no children.
10. **What is a root node?** The top node of a tree.
11. **What is lossless compression?** Compression from which the original data can be recovered exactly.
12. **What do 0 and 1 mean in the tree?** 0 represents a left move and 1 represents a right move.
13. **Which Python module provides a heap?** `heapq`.
14. **Which class counts character frequencies?** `collections.Counter`.
15. **Are Huffman codes always identical?** No. Different valid codes can result when frequencies are tied or when left/right choices differ.

---

# Experiment 3: Fractional Knapsack Using Greedy Method

## Aim
Solve the Fractional Knapsack Problem using a Greedy Method to maximize profit within a given capacity.

## Theory
Each item has a weight and a profit. The knapsack has a fixed capacity. In Fractional Knapsack, an item can be taken completely or partially.

Calculate each item's profit-to-weight ratio:
Ratio = Profit / Weight.

Sort items by decreasing ratio. Take the highest-ratio items first. If the next item does not fit completely, take the fraction that fills the remaining capacity.

## Algorithm
1. Read the number of items.
2. Read each item's weight and profit.
3. Read the knapsack capacity.
4. Calculate profit/weight for every item.
5. Sort items by decreasing ratio.
6. Take a complete item if it fits.
7. Otherwise take the fraction that fits.
8. Add the selected profit and display the maximum profit.

## Complexity
- Ratio calculation: O(n).
- Sorting: O(n log n).
- Selection: O(n).
- Overall time: O(n log n).
- Auxiliary space: O(n).

## Conclusion
The Fractional Knapsack problem is solved using a Greedy strategy by selecting items in decreasing order of profit-to-weight ratio.

## Viva Questions and Answers
1. **What is the Knapsack Problem?** An optimization problem to maximize profit within a limited capacity.
2. **What is Fractional Knapsack?** A knapsack problem where items can be taken fully or partially.
3. **Which algorithm is used?** Greedy Algorithm.
4. **What is the objective?** Maximize profit without exceeding capacity.
5. **What is the profit-to-weight ratio?** Profit divided by weight.
6. **Why sort in descending order?** To select the highest profit per unit weight first.
7. **Can an item be divided?** Yes, fractions are allowed.
8. **What if an item does not fit completely?** Take the fraction that fits in the remaining capacity.
9. **What is an optimization problem?** A problem that seeks the best solution, such as maximum profit or minimum cost.
10. **What is the time complexity?** O(n log n), mainly due to sorting.
11. **Which Python function sorts items?** `sorted()`.
12. **Is Greedy optimal for Fractional Knapsack?** Yes, for the standard Fractional Knapsack problem.
13. **How is it different from 0-1 Knapsack?** Fractional allows partial items; 0-1 requires taking or rejecting each whole item.

---

# Experiment 4: 0-1 Knapsack Using Dynamic Programming

## Aim
Solve the 0-1 Knapsack Problem using Dynamic Programming to maximize profit without exceeding capacity.

## Theory
Each item has a weight and profit. Each item must either be selected completely (1) or rejected (0). Items cannot be divided.

Dynamic Programming stores the best result for smaller item sets and capacities in a table. For each item, compare:
- Excluding the item: previous best profit at the same capacity.
- Including the item: its profit plus the previous best profit at the remaining capacity.

If the item does not fit, copy the previous result.

## Recurrence
If item i fits:
DP[i][w] = max(DP[i-1][w], profit[i] + DP[i-1][w-weight[i]])
Otherwise:
DP[i][w] = DP[i-1][w].
The first row and first column are initialized to zero.

## Algorithm
1. Read the number of items.
2. Read weights and profits.
3. Read the knapsack capacity.
4. Create a table with n+1 rows and W+1 columns.
5. Initialize the table with zeros.
6. For each item and each capacity, compare include and exclude choices.
7. Store the maximum value.
8. Display the value in the final table cell.

## Complexity
- Time: O(nW).
- Space: O(nW).
Here n is the number of items and W is the integer capacity.

## Conclusion
The 0-1 Knapsack problem is solved using Dynamic Programming by comparing inclusion and exclusion of each complete item.

## Viva Questions and Answers
1. **What is 0-1 Knapsack?** An optimization problem where each item is either selected completely or rejected.
2. **Why is it called 0-1?** Each item has a decision value of 0 or 1.
3. **Which method is used?** Dynamic Programming.
4. **What is Dynamic Programming?** Solving overlapping subproblems and storing their results.
5. **What is a DP table?** A table that stores solutions to smaller subproblems.
6. **Can an item be divided?** No.
7. **What are the two choices?** Include or exclude the item.
8. **What is the objective?** Maximize profit within capacity.
9. **What does the recurrence compare?** The profit from including the item and excluding it.
10. **What is the time complexity?** O(nW).
11. **What is the space complexity of this table implementation?** O(nW).
12. **Why initialize the first row and column to zero?** With zero items or zero capacity, maximum profit is zero.
13. **How does it differ from Greedy?** DP compares subproblem results; Greedy makes a locally best choice.

---

# Experiment 5: N-Queens Using Backtracking

## Aim
Place N queens on an N x N chessboard so that no two queens attack each other, using Backtracking. The program fixes the first queen in the first column at a user-selected row.

## Theory
A queen can attack horizontally, vertically and diagonally. Therefore, no two queens may share a row, column or diagonal.

Backtracking tries a possible position. If it is safe, it places a queen and moves to the next column. If later placement fails, it removes the queen and tries another row.

## Algorithm
1. Read N and create an N x N board of zeros.
2. Read the row for the first queen and place it in column 0.
3. Start solving from column 1.
4. Try each row in the current column.
5. Check the same row and the upper-left and lower-left diagonals.
6. If safe, place the queen and recursively process the next column.
7. If the recursive call fails, remove the queen.
8. If all columns are filled, display the board.
9. If no placement works, display that no solution exists for the fixed first queen.

## Complexity
- Common upper-bound search estimate: O(N!).
- Board storage: O(N^2).
- Recursion stack: O(N).
- Overall auxiliary storage including the board: O(N^2).

## Conclusion
The N-Queens problem is solved using Backtracking by placing queens safely and undoing placements when they lead to failure.

## Viva Questions and Answers
1. **What is the N-Queens Problem?** Place N queens on an N x N board so no two queens attack each other.
2. **Which algorithm is used?** Backtracking.
3. **What is Backtracking?** Trying a choice and undoing it if it cannot lead to a solution.
4. **How does a queen move?** Horizontally, vertically and diagonally.
5. **What is a safe position?** A position not attacked by any previously placed queen.
6. **Why use recursion?** To place queens one column at a time.
7. **What is the base condition?** When the column index reaches N, all queens have been placed.
8. **Why use backtracking?** To undo a placement that leads to a dead end and try another.
9. **What does `board[row][col] = 1` mean?** Place a queen in that cell.
10. **What does `board[row][col] = 0` mean?** Remove a queen from that cell.
11. **What is a matrix?** A two-dimensional arrangement of values in rows and columns.
12. **What is the common time-complexity estimate?** O(N!) upper-bound search estimate.
13. **What is the board's space complexity?** O(N^2).
14. **Does the first queen's row matter in this lab version?** Yes. The program fixes the first queen in column 0 at the row entered by the user; some choices may not lead to a solution.

---

# Quick Comparison of Experiments 1–5

| Experiment | Main technique | Main idea |
|---|---|---|
| 1. Fibonacci | Iteration and recursion | Generate a number sequence |
| 2. Huffman | Greedy | Combine two lowest frequencies |
| 3. Fractional Knapsack | Greedy | Take highest profit/weight ratio first |
| 4. 0-1 Knapsack | Dynamic Programming | Compare include and exclude |
| 5. N-Queens | Backtracking | Place, test and undo queens |

## Important complexity summary

| Experiment | Time complexity |
|---|---|
| Fibonacci iterative | O(n) |
| Fibonacci simple recursive | O(2^n) upper bound |
| Huffman | O(n + k log k) |
| Fractional Knapsack | O(n log n) |
| 0-1 Knapsack DP | O(nW) |
| N-Queens | O(N!) upper-bound search estimate |
