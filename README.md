# Planning Permission Checker

This project is designed to evaluate whether planning permission is required for erecting a face, gate, or wall based on a provided dataset. It processes the data and applies various criteria to determine the necessity of planning permission for different sites.

## Project Structure

The project consists of three Python files:

1. **data_preparation.py**: 
   - This file contains functions for preparing the DataFrame from the dataset. 
   - It loads the dataset from an Excel file, processes it by replacing certain values, and handles missing data.

2. **planning_permission.py**: 
   - This file includes functions that implement the logic to check if planning permission is required based on defined criteria.
   - It analyzes the DataFrame created by `data_preparation.py` and evaluates site-specific conditions.

3. **main.py**: 
   - This is the entry point of the application. 
   - It orchestrates the execution of the data preparation and planning permission checking functions, providing a cohesive user experience.

## Dataset Structure

The dataset is sourced from an Excel file with two sheets. The relevant sheet "Diagram" for this project contains the following information:

1. **Universal Category**: 
   - If the site falls into this category, planning permission is required.

2. **Location of gate, fence, wall, or other means of enclosure**:
   - If the structure is adjacent to a highway used by vehicular traffic.

3. **Height of gate, fence, wall, or other means of enclosure**:
   - Up to 1m: Planning permission may be required if other conditions are met.
   - Above 1m: Planning permission is generally required.
   - Up to 2m: Check other conditions to determine permission requirement.
   - Above 2m: Planning permission is required.

4. **Planning Constraints**:
   - Listed building status.
   - Article 2(3) for land removing permitted development rights.
   - Article 2(4) for land.
   - Article 4 Directive removing permitted development rights.
   - Areas of Outstanding Natural Beauty (AONB).
   - Works affecting Tree Preservation Orders (TPO).

5. **Other Categories**:
   - Permitted development rights removed by previous planning.
   - New build property with restrictions applied.

6. **Final Planning Permission Assessment**: 
   - Based on the above conditions, the final output will indicate if planning permission is required for each site.

## How to Use

1. **Install Dependencies**: Ensure you have the required libraries installed. You can install them using:
   ```bash
   pip install pandas
2. **Prepare the Dataset**: Update the file path in `data_preparation.py` to point to your Excel file containing the planning data.

3. **Run the Application**: Execute `main.py` to prepare the dataset and check for planning permissions. The output will indicate whether planning permission is required for each site.

4. **View Results**: The results will be printed to the console, showing which sites require planning permission based on the defined criteria.
