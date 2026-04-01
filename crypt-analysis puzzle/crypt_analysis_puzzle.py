import itertools

def solve_csp():
    letters = ['T', 'W', 'O', 'F', 'U', 'R']
    digits = list(range(10))

    def is_consistent(var, digit, assignment):
        if digit in assignment.values():
            return False

        if var in ['T', 'F'] and digit == 0:
            return False

        temp = assignment.copy()
        temp[var] = digit

        if all(k in temp for k in ['O', 'R']):
            if (temp['O'] + temp['O']) % 10 != temp['R']:
                return False

        if all(k in temp for k in ['O', 'W', 'U']):
            c1 = (temp['O'] + temp['O']) // 10
            if (c1 + temp['W'] + temp['W']) % 10 != temp['U']:
                return False

        if all(k in temp for k in ['O', 'W', 'T']):
            c1 = (temp['O'] + temp['O']) // 10
            c2 = (c1 + temp['W'] + temp['W']) // 10
            if (c2 + temp['T'] + temp['T']) % 10 != temp['O']:
                return False

        if all(k in temp for k in ['O', 'W', 'T', 'F']):
            c1 = (temp['O'] + temp['O']) // 10
            c2 = (c1 + temp['W'] + temp['W']) // 10
            c3 = (c2 + temp['T'] + temp['T']) // 10
            if c3 != temp['F']:
                return False

        return True

    def backtrack(assignment):
        if len(assignment) == len(letters):
            return assignment

        unassigned = [v for v in letters if v not in assignment]
        var = unassigned[0]

        for digit in digits:
            if is_consistent(var, digit, assignment):
                assignment[var] = digit
                result = backtrack(assignment)
                if result:
                    return result
                del assignment[var]
        return None

    return backtrack({})

sol = solve_csp()

if sol:
    two = sol['T']*100 + sol['W']*10 + sol['O']
    four = sol['F']*1000 + sol['O']*100 + sol['U']*10 + sol['R']
    
    print(f"Solution for TWO + TWO = FOUR:")
    print(f"  {two}")
    print(f"+ {two}")
    print("------")
    print(f" {four}")
    print("")
    for k in sorted(sol):
        print(f"{k}: {sol[k]}")