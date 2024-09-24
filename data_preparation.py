import pandas as pd

def prepare_dataframe(file_path):
    """
    Load and prepare the Excel DataFrame for planning permission checks. To make the analysis simpler, the 'Restrictions'
    column was edited to shorter strings. The Foward fill method has been used to further simplify the analysis in the next
    step. In fact, the conditional loops are bonded initially just to the type of Restriction (way easier then computing over
    the Details strings).

    Parameters:
    - file_path (str): The path to the Excel file.

    Returns:
    - pd.DataFrame: The prepared DataFrame.
    """
    # Load the Excel file into a DataFrame
    df = pd.read_excel(file_path, sheet_name='Diagram', skiprows=4)
    
    # Rename columns
    df.columns = ['Restrictions', 'Details'] + df.columns[2:].tolist()
    
    # Replace 'y' and 'n' with 1 and 0
    df = df.replace(to_replace=['y', 'n'], value=[1, 0])
    
    # Map specific restriction names to standardised names
    df['Restrictions'] = df['Restrictions'].replace({
        "Location of gate, fence, wall or other means of enclosure ": "Location",
        "Height of gate, fence, wall or other means of enclosure": "Height",
        "Planning constraints": "Constraints",
        "Other": "Other"
    })
    
    # Forward fill the 'Restrictions' column
    df['Restrictions'] = df['Restrictions'].ffill()
    
    # Fill NaN values with 0
    df.fillna(0, inplace=True)
    
    return df