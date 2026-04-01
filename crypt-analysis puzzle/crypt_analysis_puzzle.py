import itertools

def solve_cryptarithmetic_csp():
    letters = ['O', 'R', 'W', 'U', 'T', 'F']
    digits = list(range(10))

    def backtrack(assignment):
        if len(assignment) == len(letters):
            return assignment

        var = [l for l in letters if l not in assignment][0]

        for val in digits:
            if val in assignment.values():
                continue
            if var in ['T', 'F'] and val == 0:
                continue

            assignment[var] = val
            
            if is_consistent(assignment):
                result = backtrack(assignment)
                if result: return result
            
            del assignment[var]
        return None

    def is_consistent(a):
        # Column 1: O + O = R + 10 * C10
        if all(k in a for k in ['O', 'R']):
            if (a['O'] + a['O']) % 10 != a['R']:
                return False
            c10 = (a['O'] + a['O']) // 10
            
            # Column 2: C10 + W + W = U + 10 * C100
            if all(k in a for k in ['W', 'U']):
                if (c10 + a['W'] + a['W']) % 10 != a['U']:
                    return False
                c100 = (c10 + a['W'] + a['W']) // 10
                
                # Column 3: C100 + T + T = O + 10 * C1000
                if 'T' in a:
                    if (c100 + a['T'] + a['T']) % 10 != a['O']:
                        return False
                    c1000 = (c100 + a['T'] + a['T']) // 10
                    
                 # Column 4: C1000 = F

                    if 'F' in a:
                        if c1000 != a['F']:
                            return False
        return True

    return backtrack({})

sol = solve_cryptarithmetic_csp()

if sol:
    two = sol['T']*100 + sol['W']*10 + sol['O']
    four = sol['F']*1000 + sol['O']*100 + sol['U']*10 + sol['R']
    print(f"Solution for TWO + TWO = FOUR:")
    print(f"  {two}")
    print(f"+ {two}")
    print("------")
    print(f" {four}\n")
    for k in sorted(sol):
        print(f"{k}: {sol[k]}")