# LP-3 (Laboratory Practice III) - Comprehensive Code, Theory & Viva Repository

A complete, production-grade reference repository for **SPPU Computer Engineering LP-III (Laboratory Practice III)** covering:
1. **Design and Analysis of Algorithms (DAA)**
2. **Machine Learning (ML)**
3. **Blockchain Technology (BT / Solidity Smart Contracts)**

Each program file contains fully functional source code, exhaustive line-by-line comments, architectural theory, complexity analyses, and **15+ high-yield Viva Questions and Answers** directly embedded as comments.

---

## 📚 Repository Index & Quick Reference

### Group A: Design and Analysis of Algorithms (DAA)

| File Name | Topic / Problem | Paradigm | Time Complexity | Space Complexity |
|---|---|---|---|---|
| [`fibo`](./fibo) | Fibonacci Series (Recursive vs Iterative) | Divide & Conquer / DP | Iterative: `O(n)`<br>Recursive: `O(2^n)` | Iterative: `O(1)`<br>Recursive: `O(n)` |
| [`fractionalKnapsack`](./fractionalKnapsack) | Fractional Knapsack Problem | Greedy Algorithm | `O(n log n)` | `O(1)` auxiliary |
| [`knapsack-DP`](./knapsack-DP) | 0/1 Knapsack Problem | Dynamic Programming | `O(n * W)` (Pseudo-polynomial) | `O(n * W)` or `O(W)` |
| [`huffman`](./huffman) | Huffman Coding (Lossless Compression) | Greedy (Min-Heap) | `O(n log n)` | `O(n)` |
| [`n-queen`](./n-queen) | N-Queens Puzzle | Backtracking (DFS + Pruning) | `O(N!)` | `O(N^2)` board, `O(N)` stack |

---

### Group B: Machine Learning (ML)

| File Name | Topic / Problem | Model / Techniques | Key Metrics / Objectives |
|---|---|---|---|
| [`gradientdescent`](./gradientdescent) | Local Minimum Optimization | Gradient Descent (First-order) | Learning rate ($\alpha$), Convergence, Derivative |
| [`uber`](./uber) | Uber Fare Price Prediction | Linear Regression vs Random Forest | $R^2$ Score, RMSE, Outlier Removal |
| [`bankcustomer`](./bankcustomer) | Customer Churn Classification | Artificial Neural Network (MLP) | Accuracy, Confusion Matrix, Classification Report |
| [`emailspam`](./emailspam) | SMS / Email Spam Classification | TF-IDF Vectorizer + KNN & Linear SVM | Accuracy, Precision, Recall, Confusion Matrix |
| [`k-means`](./k-means) | Customer / Sales Segmentation | K-Means & Agglomerative Clustering | Elbow Method (WCSS/Inertia), Dendrogram |

---

### Group C: Blockchain Technology (Solidity Smart Contracts)

| File Name | Smart Contract Title | Key Blockchain Concepts Demonstrated |
|---|---|---|
| [`B-1Studentdata`](./B-1Studentdata) | Student Data Management | Structs, Dynamic Storage Arrays, `memory` vs `storage`, `view`, `fallback()`, `receive()` |
| [`B-2 BANkaccount`](./B-2 BANkaccount) | Bank Account System | `payable`, `msg.sender`, `msg.value`, `require()`, Checks-Effects-Interactions (CEI), Reentrancy prevention |

---

## 🎯 How to Use for Viva & Practical Exams
- Open any file to see:
  1. **Header documentation**: Objective, mathematical formulation, and algorithmic steps.
  2. **Clean, documented source code**: Explanation of every function, variable, and parameter.
  3. **Theory & Architecture section**: Deep dive into working mechanisms, tradeoffs, and edge cases.
  4. **Viva Questions & Answers (15 Q&As per file)**: Direct answers to examiner-favorite questions.

---

## 🚀 Execution Guide

### 1. Java Programs (`fibo`, `fractionalKnapsack`, `knapsack-DP`, `huffman`, `n-queen`)
```bash
# Rename or compile directly with javac
javac Fibonacci.java   # or javac <file>
java Fibonacci
```

### 2. Python ML Scripts (`gradientdescent`, `uber`, `bankcustomer`, `emailspam`, `k-means`)
```bash
# Install dependencies
pip install numpy pandas scikit-learn matplotlib

# Run any script
python uber
python bankcustomer
python emailspam
python k-means
python gradientdescent
```

### 3. Solidity Smart Contracts (`B-1Studentdata`, `B-2 BANkaccount`)
- Open [Remix Ethereum IDE](https://remix.ethereum.org).
- Create a new file with `.sol` extension and paste the contract code.
- Select compiler version `0.8.20` or higher.
- Deploy in Remix VM (Prague / Cancun) or Sepolia testnet using MetaMask.
