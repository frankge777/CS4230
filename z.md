### 1. Swarm of Robotic Miners Problem

#### (a) Define a minimal state space representation for this problem. (3 pts)

**State space representation** refers to how we define the current "state" of the system. In this case, each robot miner’s position in the maze and whether they have collected all the Strontium 90 (dots) will define the state. The following elements are needed:

- **Positions of all k miners**: The position of each miner is crucial to track since they move independently but cannot share a space.
- **Positions of Strontium 90 pieces**: Since the miners must collect them, we need to know which pieces of Strontium 90 have been collected and which remain.

A minimal state space would be represented by:
- The **location of each miner**: \((x_1, y_1), (x_2, y_2), ..., (x_k, y_k)\) where \(x_i, y_i\) is the position of the \(i\)-th miner.
- A **binary flag for each Strontium 90 piece**: Whether it is collected or not, represented as a set or list of uncollected positions.

Thus, a state could be represented as:
\[
((x_1, y_1), (x_2, y_2), ..., (x_k, y_k), \{Strontium\ remaining\ positions\})
\]

#### (b) How large is the state space? (3 pts)

To compute the size of the state space:
1. **Miner positions**: Each miner can be in any of the \(M \times N\) cells. Since there are \(k\) miners, the number of possible miner positions is:
   \[
   (M \times N)^k
   \]
   
2. **Strontium 90 positions**: Each Strontium 90 piece can either be present or absent. If there are \(P\) pieces, the number of possible configurations is:
   \[
   2^P
   \]

Therefore, the total size of the state space is:
\[
(M \times N)^k \times 2^P
\]

---

### 2. Search Graph Problem

#### (a) Depth-first graph search (3 pts)
In Depth-first search (DFS), you explore as far down one path as possible before backtracking. Following alphabetical tiebreaking:

- Path: `S → A → B → D → E → G`

#### (b) Breadth-first graph search (3 pts)
In Breadth-first search (BFS), you explore all nodes at the current depth before moving to the next level.

- Path: `S → A → C → G`

#### (c) Uniform cost graph search (3 pts)
Uniform-cost search expands the node with the lowest path cost. Assuming all edges have equal costs, uniform-cost search behaves like BFS in this case.

- Path: `S → A → C → G`

#### (d) Greedy graph search (3 pts)
Greedy search selects the node closest to the goal, typically based on a heuristic like straight-line distance. Assuming `C` is closest to the goal:

- Path: `S → A → C → G`

#### (e) A* graph search (3 pts)
A* search uses both the actual cost to reach the node (g) and the estimated cost to the goal (h). Assuming a consistent heuristic, A* will behave similarly to greedy or uniform-cost search, depending on the heuristic.

- Path: `S → A → C → G`

