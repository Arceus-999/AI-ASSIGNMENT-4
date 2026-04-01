## Sudoku Puzzle Solver 

This code is about **Sudoku puzzle** solved using  **backtracking** .

The program takes an incomplete Sudoku grid and fills in the missing numbers while following all Sudoku rules.

---

## How the Code Works

- Takes a 9×9 Sudoku puzzle as input  
- Empty cells are represented using `0`  
- Fills the grid so that:
  - Each row has numbers from 1–9 (no repeats)
  - Each column has numbers from 1–9 (no repeats)
  - Each 3×3 box has numbers from 1–9 (no repeats)  

### 1. Class Initialization

* The puzzle is stored in `self.board`
* `self.size = 9` because Sudoku is a 9×9 grid


### 2. Checking Valid Moves

 Checks whether placing a number in a cell is allowed.

It ensures:

* The number is not already in the same row
* The number is not already in the same column
* The number is not already in the 3×3 subgrid

If all checks pass then it is a valid move
Else it is, invalid move


### 3. Finding Empty Cells

* Scans the board for a cell with value 0
* Returns its position (row,col)
* If no empty cells are found then the puzzle is complete


### 4. Solving the Puzzle 

This is the main logic using **backtracking**:

1. Find an empty cell
2. Try numbers from 1 to 9
3. For each number:

   * Check if it's valid
   * If valid:

     * Place it in the cell
     * Recursively try solving the rest of the board
4. If it leads to a dead end:

   * Remove the number (set back to 0)
   * Try the next number

This process continues until:

* A solution is found
* Or all possibilities are exhausted


### 5. Printing the Board 

* Displays the Sudoku grid after solving it.

---

##  Output

* Prints the original puzzle
* Then prints the solved puzzle (if a solution exists)


