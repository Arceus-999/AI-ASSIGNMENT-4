import matplotlib
matplotlib.use('TkAgg')

import geopandas as gpd
import matplotlib.pyplot as plt
import fiona
import random
import os

fiona.drvsupport.supported_drivers['KML'] = 'rw'

file_path = "telangana.kml"

if not os.path.exists(file_path):
    print(f"Error: {file_path} not found in {os.getcwd()}")
else:
    gdf = gpd.read_file(file_path, driver='KML')
    
    name_col = "Name"
    if "District" in gdf.columns:
        name_col = "District"
    
    gdf[name_col] = gdf[name_col].astype(str).str.strip()

    adjacencies = {}
    for index, row in gdf.iterrows():
        neighbors = gdf[gdf.geometry.touches(row.geometry)][name_col].tolist()
        adjacencies[row[name_col]] = neighbors

    districts = list(adjacencies.keys())
    colors = ["#ff9999", "#99ff99", "#9999ff", "#ffff99"]

    def is_valid(district, color, assignments, neighbors_dict):
        for neighbor in neighbors_dict.get(district, []):
            if neighbor in assignments and assignments[neighbor] == color:
                return False
        return True

    def solve_csp(assignments, districts_list, color_list, neighbors_dict):
        if len(assignments) == len(districts_list):
            return assignments
        
        unassigned = [d for d in districts_list if d not in assignments]
        current = max(unassigned, key=lambda d: len(neighbors_dict[d]))
        
        shuffled_colors = random.sample(color_list, len(color_list))
        
        for color in shuffled_colors:
            if is_valid(current, color, assignments, neighbors_dict):
                assignments[current] = color
                
                result = solve_csp(assignments, districts_list, color_list, neighbors_dict)
                if result is not None:
                    return result
                
                assignments.pop(current)
        return None

    print("Solving Map Coloring CSP...")
    csp_solution = solve_csp({}, districts, colors, adjacencies)

    if csp_solution:
        gdf["color"] = gdf[name_col].map(csp_solution)

        fig, ax = plt.subplots(figsize=(12, 10))
        gdf.plot(ax=ax, color=gdf["color"], edgecolor="black", linewidth=0.8)

        for idx, row in gdf.iterrows():
            if row.geometry and not row.geometry.is_empty:
                centroid = row.geometry.centroid
                ax.text(centroid.x, centroid.y, str(row[name_col]), 
                        fontsize=7, ha='center', weight='bold',
                        bbox=dict(facecolor='white', alpha=0.5, edgecolor='none', pad=0.5))

        plt.title("Telangana 33 Districts - CSP Coloring", fontsize=15)
        plt.axis('off')
        
        print("Displaying Map...")
        plt.show()
    else:
        print("Error: Could not find a valid coloring solution.")