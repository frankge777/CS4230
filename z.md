# CS 4470: Artificial Intelligence - HW1 Solutions

## 1. Swarm of Robotic Miners Problem

### (a) Define a minimal state space representation for this problem (3 pts)

The state space representation consists of the positions of each robot miner and whether all Strontium 90 pieces (dots) have been collected. The minimal state space can be represented by:
- **Positions of all k miners**: \((x_1, y_1), (x_2, y_2), ..., (x_k, y_k)\), where \(x_i, y_i\) represents the position of the \(i\)-th miner.
- **Binary flag for each Strontium 90 piece**: A set/list indicating whether each piece of Strontium 90 has been collected or remains.

Thus, a state is represented as:
\[
((x_1, y_1), (x_2, y_2), ..., (x_k, y_k), \{Strontium\ remaining\ positions\})
\]

### (b) How large is the state space? (3 pts)

To calculate the size of the state space:
1. **Miner positions**: Each miner can be in any of the \(M \times N\) cells, so the number of possible miner positions is \((M \times N)^k\).
2. **Strontium 90 positions**: Each Strontium 90 piece can either be collected or not, so for \(P\) pieces, the number of possible configurations is \(2^P\).

Thus, the total size of the state space is:
\[
(M \times N)^k \times 2^P
\]

---

## 2. Search Graph Problem

The following search strategies were applied to a given graph:

### (a) Depth-first graph search (3 pts)
Using DFS and alphabetical tiebreaking:
- **Path**: `S → A → B → D → E → G`

### (b) Breadth-first graph search (3 pts)
Using BFS, exploring nodes level by level:
- **Path**: `S → A → C → G`

### (c) Uniform cost graph search (3 pts)
With equal edge costs, uniform cost behaves like BFS:
- **Path**: `S → A → C → G`

### (d) Greedy graph search (3 pts)
Using a heuristic to select nodes closest to the goal:
- **Path**: `S → A → C → G`

### (e) A* graph search (3 pts)
A* search balances actual cost and heuristic estimates:
- **Path**: `S → A → C → G`

