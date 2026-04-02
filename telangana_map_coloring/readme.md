# Telangana Map Coloring

This code is about **Map Coloring Problem** for the 33 districts of Telangana using **(CSP)** approach. The objective is to assign colors to each district such that no two neighboring districts have the same color.

The code automatically:

* Reads district boundaries from a .kml file
* Identifies neighboring districts using spatial relationships
* Applies a the CSP algorithm
* displays the colored map using Matplotlib


#### How it works:

### 1. Data Loading 

The program begins by loading the telangana.kml file into a Geodataframe using Geopandas. 


### 2. Adjacency List

Using geometric operations, the code determines which districts share boundaries. For each district, it identifies neighboring districts by checking if their geometries touch.This information is stored as an adjacency list.


### 3. CSP Logic

The logic is applying backtracking CSP algorithm to assign colors to districts. The algorithm ensures that no two adjacent districts are assigned the same color. It also uses a heuristic to improve efficiency and reduce the search space.



### 4. Final Step

Once a valid coloring is found, the assigned colors are mapped back to the GeoDataFrame. The program then visualizes the colored districts using Matplotlib, adding labels at the centroid of each district and displaying the final map.

---

## Output

* A colored map of Telangana districts
* No two adjacent districts share the same color
* Labels displayed clearly on the map
