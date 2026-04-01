#  Cryptarithmetic Solver (TWO + TWO = FOUR)

This Python code is about solving the  **cryptarithmetic puzzle** :
In a cryptarithmetic puzzle, letters are replaced by digits (0-9). Each letter must represent a unique digit, and the leading letters of words cannot be zero. This specific implementation uses Backtracking and Column-wise N-ary Constraints (Carries) to find a valid solution.

---

## How the Code Works

### 1. Variables and Domains

* **Variables (letters):**

  
  ['O', 'R', 'W', 'U', 'T', 'F']
  

* **Domain (possible values):**

  digits = [0–9]
 
 * Each letter must map to a **unique digit**.


### 2. Constraints

####  General Constraints

* No two letters can have the same digit.
* Leading digits (T and F) **cannot be 0**.

####  Arithmetic Constraints 

The addition is checked digit by digit:

**Column 1 (Units place):**

```
O + O = R (with carry C10)
```

---

**Column 2 (Tens place):**

```
C10 + W + W = U (with carry C100)
```

---

**Column 3 (Hundreds place):**

```
C100 + T + T = O (with carry C1000)
```

---

**Column 4 (Thousands place):**

```
C1000 = F
```


### 3. Backtracking Algorithm


1. Pick an unassigned letter.
2. Try assigning a digit.
3. Check if the assignment is **valid**.
4. If valid then continue recursively.
5. If invalid then backtrack and try another digit.


### 4. Final Calculation

Once a valid mapping is found:

* Convert letters into numbers:

  ```
  TWO  = T×100 + W×10 + O
  FOUR = F×1000 + O×100 + U×10 + R
  ```

* Print:

  * The vertical addition
  * The letter and corresponding digit mapping

---

## Example Output

```
Solution for TWO + TWO = FOUR:
  734
+ 734
------
 1468

F: 1
O: 4
R: 8
T: 7
U: 6
W: 3
```

---





