import pandas as pd

def check_planning_permission(df):
    """
    Check if planning permission is required for each site code based on various criteria. 

    Parameters:
    df (pd.DataFrame): DataFrame containing planning restriction data with the following columns:
                       - 'Restrictions': Categories of restrictions (e.g., 'Location', 'Height', 'Constraints', 'Other').
                       - 'Details': Specific details related to each restriction category.
                       - Site codes: Columns representing individual sites (e.g., '2U1', '2U2', etc.), which indicate the 
                         presence (1.0) or absence (0.0) of restrictions.

    Returns:
    dict: A dictionary with site codes as keys and a string indicating whether planning permission is required.

    Criteria for Planning Permission:
    1. Universal Requirement:
       - If the site code contains 'U' (e.g., '2U1', '2U2'), planning permission is automatically required.
    
    2. Constraints and Other (which seems to be falling into Universal Requirments):
       - If any entry under the 'Constraints' category has a value of 1.0, planning permission is required.
       - If any entry under the 'Other' category has a value of 1.0, planning permission is also required.

    3. Location-Specific Requirements:
        - If the site is **adjacent to a highway**:
        - Planning permission is required if the height of the structure is **above 1 meter**.
        - If the site is **near a listed building**:
        - Planning permission is required if the height of the structure is **above 2 meters**.
    """
    results = {}

    # Iterate over each column (site code) in the DataFrame, starting from the third column
    for column in df.columns[2:]:  # Skipping 'Restrictions' and 'Details' columns
        # Initialize permission requirement
        requires_permission = False
        
        # Check if the site code contains 'U'
        if 'U' in column:
            requires_permission = True
        else:
            # Check if any row for 'Constraints' or 'Other' has a value of 1.0
            constraints_values = df[df['Restrictions'] == 'Constraints'][column]
            other_values = df[df['Restrictions'] == 'Other'][column]
            
            # Check if 1.0 is present in Constraints or Other
            if any(constraints_values == 1.0) or any(other_values == 1.0):
                requires_permission = True
            
            # Check for location-specific requirements
            adjacent_highway = (df['Restrictions'] == 'Location') & (df['Details'].str.contains('adjacent', na=False))
            height_above_1m = (df['Restrictions'] == 'Height') & (df['Details'] == 'above 1m')
            height_above_2m = (df['Restrictions'] == 'Height') & (df['Details'] == 'above 2m')

            # Check if the site is adjacent to a highway and height is above 1m
            if adjacent_highway.any() and any(df[height_above_1m][column] == 1.0):
                requires_permission = True
            
            # Check if height is above 2m
            if any(df[height_above_2m][column] == 1.0):
                requires_permission = True
        
        # Record results
        results[column] = (
            f"{column}: Planning permission required" if requires_permission 
            else f"{column}: No planning permission required"
        )

    return results