import pandas as pd
from data_preparation import prepare_dataframe
from planning_permission import check_planning_permission

file_path = '/Users/sebastiano/Documents/PytonScripts/PlanningHub_CodeChallenge/PlanningHub_CodeChallenge_Sebastiano/PlanningHub Software engineer code challange- 202404.xlsx'
df = prepare_dataframe(file_path)
results = check_planning_permission(df)
for result in results.values():
    print(result)