def solve_map_coloring():
    states = ["WA", "NT", "SA", "Queensland", "NSW", "Victoria", "Tasmania"]
    colors = ["Red", "Green", "Blue"]
    constraints = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "Queensland", "SA"],
        "SA": ["WA", "NT", "Queensland", "NSW", "Victoria"],
        "Queensland": ["NT", "SA", "NSW"],
        "NSW": ["Queensland", "SA", "Victoria"],
        "Victoria": ["SA", "NSW"],
        "Tasmania": []
    }

    assignment = {}

    def is_valid(state, color, assignment):
        for neighbor in constraints.get(state, []):
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def backtrack(at_index):
        if at_index == len(states):
            return True

        current_state = states[at_index]

        for color in colors:
            if is_valid(current_state, color, assignment):
                assignment[current_state] = color
                if backtrack(at_index + 1):
                    return True
                del assignment[current_state]
        return False

    if backtrack(0):
        print(f"{'STATE/TERRITORY':<20} | {'COLOR ASSIGNED':<15}")
        print("-" * 40)
        for state, color in assignment.items():
            print(f"{state:<20} | {color:<15}")
    else:
        print("No solution exists.")

if __name__ == "__main__":
    solve_map_coloring()