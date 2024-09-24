# PlanningHub_CodeChallenge
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

The dataset is sourced from an Excel file with two sheets. The relevant sheet for this project contains the following structure:

| Restrictions | Details                                           | 2U1 | 2U2 | 2U3 | 2U4 | 2U5 | 2U6 | 2U7 | 2U8 | 2U9 | 2A1 | 2A2 | 2A3 | 2A4 | 2A5 | 2A6 |
|--------------|--------------------------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Location of gate, fence, wall or other means of enclosure | "adjacent to a highway used by vehicular traffic" | y   | y   | y   |     |     |     |     |     |     |     |     |     |     |     |     |
|                                                        | gate, fence, wall or other means of enclosure face onto a property with a listed building | y |     |     | y   | y   | y   |
| Height of gate, fence, wall or other means of enclosure | up to 1m                                      | y   | y   |     |     |     |     |     |     |     |     |     |     |     |     |
|                                                        | above 1m                                      |     |     | y   |     |     |     |     |     |     |     |     |     |     |     |
|                                                        | up to 2m                                      |     |     |     | y   | y   |     |
|                                                        | above 2m                                      |     |     |     |     | y   |
| Planning constraints                                   | Listed building                                | y   |     |     |     |     |     |     |     |     |     |     |     |     |     |
|                                                        | Article 2(3) Land removing permitted development rights for the project | y |     |     |     |     |     |     |     |     |     |     |     |     |     |
|                                                        | Article 2(4) Land                             |     | y   |     |     |     |     |     |     |     |     |     |     |     |     |
|                                                        | Article 4 Directive removing the PD rights for the project |     |     | y |     |     |     |     |     |     |     |     |     |     |     |
|                                                        | AONB                                          |     |     |     | y   |     |     |     |     |     |     |     |     |     |     |
|                                                        | works affecting TPO                           |     |     |     |     |     | y   |     |     |     |     |     |     |     |     |
| Other                                                 | Permitted development rights removed with previous planning | y   |     |     |     |     |     |     |     |     |     |     |     |     |     |
|                                                        | New build property - restrictions applied     |     |     |     |     | y   |     |     |     |     |     |     |     |     |     |
| Planning permission                                    | Planning Permission required                   | y   | y   | y   | y   | y   | y   | y   | y   | y   | n   | n   | y   | n   | n   | y   |

## How to Use

1. **Install Dependencies**: Ensure you have the required libraries installed. You can install them using:
   ```bash
   pip install pandas
2. **Prepare the Dataset**: Update the file path in `data_preparation.py` to point to your Excel file containing the planning data.

3. **Run the Application**: Execute `main.py` to prepare the dataset and check for planning permissions. The output will indicate whether planning permission is required for each site.

4. **View Results**: The results will be printed to the console, showing which sites require planning permission based on the defined criteria.
