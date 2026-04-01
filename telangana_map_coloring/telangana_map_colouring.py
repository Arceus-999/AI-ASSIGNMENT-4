def solve_telangana_coloring():
    districts = [
        "Adilabad", "Bhadradri Kothagudem", "Hanumakonda", "Hyderabad", 
        "Jagtial", "Jangaon", "Jayashankar Bhupalpally", "Jogulamba Gadwal", 
        "Kamareddy", "Karimnagar", "Khammam", "Kumuram Bheem", "Mahabubabad", 
        "Mahabubnagar", "Mancherial", "Medak", "Medchal-Malkajgiri", "Mulugu", 
        "Nagarkurnool", "Nalgonda", "Narayanpet", "Nirmal", "Nizamabad", 
        "Peddapalli", "Rajanna Sircilla", "Rangareddy", "Sangareddy", "Siddipet", 
        "Suryapet", "Vikarabad", "Wanaparthy", "Warangal", "Yadadri Bhuvanagiri"
    ]

    colors = ["Red", "Green", "Blue", "Yellow"]

    constraints = {
        "Adilabad": ["Nirmal", "Kumuram Bheem"],
        "Kumuram Bheem": ["Adilabad", "Nirmal", "Mancherial"],
        "Nirmal": ["Adilabad", "Kumuram Bheem", "Mancherial", "Jagtial", "Nizamabad"],
        "Mancherial": ["Kumuram Bheem", "Nirmal", "Jagtial", "Peddapalli", "Jayashankar Bhupalpally"],
        "Nizamabad": ["Nirmal", "Jagtial", "Rajanna Sircilla", "Kamareddy"],
        "Jagtial": ["Nirmal", "Nizamabad", "Rajanna Sircilla", "Karimnagar", "Peddapalli", "Mancherial"],
        "Peddapalli": ["Mancherial", "Jagtial", "Karimnagar", "Jayashankar Bhupalpally"],
        "Jayashankar Bhupalpally": ["Mancherial", "Peddapalli", "Karimnagar", "Warangal", "Hanumakonda", "Mulugu"],
        "Mulugu": ["Jayashankar Bhupalpally", "Warangal", "Mahabubabad", "Bhadradri Kothagudem"],
        "Bhadradri Kothagudem": ["Mulugu", "Mahabubabad", "Khammam"],
        "Khammam": ["Bhadradri Kothagudem", "Mahabubabad", "Suryapet"],
        "Suryapet": ["Khammam", "Mahabubabad", "Jangaon", "Yadadri Bhuvanagiri", "Nalgonda"],
        "Nalgonda": ["Suryapet", "Yadadri Bhuvanagiri", "Rangareddy", "Nagarkurnool"],
        "Nagarkurnool": ["Nalgonda", "Rangareddy", "Mahabubnagar", "Wanaparthy"],
        "Wanaparthy": ["Nagarkurnool", "Mahabubnagar", "Jogulamba Gadwal"],
        "Jogulamba Gadwal": ["Wanaparthy", "Mahabubnagar"],
        "Mahabubnagar": ["Jogulamba Gadwal", "Wanaparthy", "Nagarkurnool", "Rangareddy", "Vikarabad", "Narayanpet"],
        "Narayanpet": ["Mahabubnagar", "Vikarabad"],
        "Vikarabad": ["Narayanpet", "Mahabubnagar", "Rangareddy", "Sangareddy"],
        "Sangareddy": ["Vikarabad", "Rangareddy", "Medak", "Kamareddy"],
        "Kamareddy": ["Sangareddy", "Medak", "Siddipet", "Rajanna Sircilla", "Nizamabad"],
        "Rajanna Sircilla": ["Kamareddy", "Siddipet", "Karimnagar", "Jagtial", "Nizamabad"],
        "Karimnagar": ["Rajanna Sircilla", "Siddipet", "Hanumakonda", "Jayashankar Bhupalpally", "Peddapalli", "Jagtial"],
        "Siddipet": ["Kamareddy", "Medak", "Yadadri Bhuvanagiri", "Jangaon", "Hanumakonda", "Karimnagar", "Rajanna Sircilla"],
        "Medak": ["Kamareddy", "Sangareddy", "Medchal-Malkajgiri", "Siddipet"],
        "Medchal-Malkajgiri": ["Medak", "Sangareddy", "Rangareddy", "Hyderabad", "Yadadri Bhuvanagiri"],
        "Hyderabad": ["Medchal-Malkajgiri", "Rangareddy"],
        "Rangareddy": ["Hyderabad", "Medchal-Malkajgiri", "Yadadri Bhuvanagiri", "Nalgonda", "Nagarkurnool", "Mahabubnagar", "Vikarabad", "Sangareddy"],
        "Yadadri Bhuvanagiri": ["Medchal-Malkajgiri", "Siddipet", "Jangaon", "Suryapet", "Nalgonda", "Rangareddy"],
        "Jangaon": ["Yadadri Bhuvanagiri", "Siddipet", "Hanumakonda", "Warangal", "Mahabubabad", "Suryapet"],
        "Hanumakonda": ["Jangaon", "Siddipet", "Karimnagar", "Jayashankar Bhupalpally", "Warangal"],
        "Warangal": ["Hanumakonda", "Jayashankar Bhupalpally", "Mulugu", "Mahabubabad", "Jangaon"],
        "Mahabubabad": ["Warangal", "Mulugu", "Bhadradri Kothagudem", "Khammam", "Suryapet", "Jangaon"]
    }

    assignment = {}

    def is_valid(district, color, assignment):
        for neighbor in constraints.get(district, []):
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def backtrack(at_index):
        if at_index == len(districts):
            return True

        current_district = districts[at_index]
        for color in colors:
            if is_valid(current_district, color, assignment):
                assignment[current_district] = color
                if backtrack(at_index + 1):
                    return True
                del assignment[current_district]
        return False

    if backtrack(0):
        print(f"{'TELANGANA DISTRICT':<25} | {'COLOR ASSIGNED':<15}")
        print("-" * 45)
        for district in sorted(assignment.keys()):
            print(f"{district:<25} | {assignment[district]:<15}")
    else:
        print("No valid solution found with the given constraints.")

if __name__ == "__main__":
    solve_telangana_coloring()