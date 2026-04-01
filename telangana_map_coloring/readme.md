## Telangana District Map Coloring Solver (CSP)

This code applies the **Map Coloring Problem** to all 33 districts of Telangana using a backtracking approach.

 The main objective is to assign a color to each district such that **no two neighboring districts share the same color**.

---

##  How the Code Works

###  1. Understanding the problem

- **Variables** → These are the 33 districts of Telangana  
- **Domains** → The colors we can use:  
  `["Red", "Green", "Blue", "Yellow"]`  
- **Constraints** → A list that tells which districts are neighbors  

This constraints list basically represents the map.  
For example, the code knows that **Hyderabad** is surrounded by **Rangareddy** and **Medchal-Malkajgiri**, so they shouldn’t have the same color.


###  2. Checking if a color is allowed

Before giving a color to any district, the code checks if it’s valid.

- It looks at all the neighboring districts  and if any neighbor already has the same color, it rejects that choice  

So, a district only gets a color if it doesn’t clash with its neighbors.


###  3. Trying all possibilities (Backtracking)

This is the main part of the logic.

- The code picks a district  
- Tries giving it a color  
- If it works, it moves to the next district  

But sometimes, no color works for a district.

When that happens:
- It goes back to the previous district  
- Changes the color it chose earlier  
- Then tries again with a different option  

This process is called **backtracking**.

This process continues until all states are assigned valid colors without conflicts.

------

###  Final output

Once a solution is found:
- The districts are sorted alphabetically  
- Each district is displayed with its assigned color .


