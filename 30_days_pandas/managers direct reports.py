import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    employee_grouped = employee.groupby('managerId')['id'].count().reset_index()
    employee_grouped = employee_grouped[employee_grouped['id']>=5]
    manager_list = pd.merge(employee_grouped, employee, left_on='managerId', right_on='id', how='inner')
    # manager_list.drop(columns=['managerId_x'  ,'id_x' , 'id_y' ,'department'  ,'managerId_y'], inplace=True)
    return manager_list[['name']]



employee = pd.DataFrame([[101, 'John', 'A', None],
[102, 'Dan', 'A', 101],
[105, 'Anne', 'A', 101],
[103, 'James', 'A', 101],
[104, 'Amy', 'A', 101],
[106, 'Ron', 'B', 101]], columns=['id', 'name', 'department', 'managerId'])

print(find_managers(employee))