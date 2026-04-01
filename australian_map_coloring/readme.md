# Australian Map Coloring 

This code is a simple implementation of the **Map Coloring Problem** using Python.

The goal is to color a map of Australia's seven principal states and territories (WA (Western Australia),NT (Northern Territory) ,SA (South Australia),Queensland,NSW (New South Wales) ,Victoria and Tasmania ) such that no two adjacent states can share the same color.

---

## How the algorithm works

The code uses an approach called **recursive backtracking**.

###  1. Selection  
It starts by picking a state, for example *Western Australia*.

###  2. Assignment  
Then it tries assigning a color to that state — either Red, Green, or Blue.

###  3. Validation  
Before moving forward, it checks:  
“Do any neighboring states already have this color?”  
If yes, that color is rejected.

###  4. Recursion  
If the color works, the algorithm moves on to the next state and repeats the same steps.

###  5. Backtracking  
If it reaches a point where no color works for a state, it doesn’t stop.  
Instead, it goes back to the previous state, changes its color, and tries a different path.

---

This process continues until all states are assigned valid colors without conflicts.

 ## Sample Output

When you run `map_coloring_csp.py`, you’ll see a clean and readable table in your terminal like this:
STATE/TERRITORY | COLOR ASSIGNED

WA | Red
NT | Green
SA | Blue
Queensland | Red
NSW | Green
Victoria | Red
