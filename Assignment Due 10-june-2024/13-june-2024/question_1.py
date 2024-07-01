# # given a list of employee dictionaries with keys 'id', 'name', 'salary', and 
# # 'department', write a function that normalizes the data into two dictionaries: 
# # one mapping 'department' to a list of employee ids and another mapping 'id' to the
# # corresponding employee details.


# def normailize_data(List1):
#     dep_ids={}
#     id_to_details={}
#     for employee in Employes:
#         emp_id = employee['id']
#         emp_dept = employee['department']
#         id_to_details[emp_id]=employee
#         if emp_dept not in dep_ids:
#             dep_ids[emp_dept]=[]
#         dep_ids[emp_dept].append(emp_id)
#     return dep_ids,id_to_details

# Employes=[{'id':1,'name':'Adil','salary':52000,'department':'Engineering'},
#        {'id':2,'name':'Ali','salary':53000,'department':'Finance'}]

# dep_ids, id_to_details = normailize_data(Employes)
# print(dep_ids)
# print(id_to_details)


# def normalize_employee_data(employee_list):
#     # Step 1: Initialize the dictionaries
#     department_to_ids = {}  # This will store department names as keys and lists of employee IDs as values
#     id_to_details = {}  # This will store employee IDs as keys and employee details as values

#     # Step 2: Iterate through the employee list
#     for employee in employee_list:
#         emp_id = employee['id']  # Extract the employee's ID
#         emp_dept = employee['department']  # Extract the employee's department

#         # Add employee details to the id_to_details dictionary
#         id_to_details[emp_id] = employee

#         # Check if the department is already in the department_to_ids dictionary
#         if emp_dept not in department_to_ids:
#             # If not, add the department with an empty list
#             department_to_ids[emp_dept] = []

#         # Add the employee ID to the list of the corresponding department
#         department_to_ids[emp_dept].append(emp_id)

#     # Step 3: Return the dictionaries
#     return department_to_ids, id_to_details

# # Example usage:
# employees = [
#     {'id': 1, 'name': 'Alice', 'salary': 70000, 'department': 'HR'},
#     {'id': 2, 'name': 'Bob', 'salary': 80000, 'department': 'Engineering'},
#     {'id': 3, 'name': 'Charlie', 'salary': 90000, 'department': 'Engineering'},
#     {'id': 4, 'name': 'David', 'salary': 75000, 'department': 'HR'}
# ]

# # Call the function with the example list of employees
# dept_to_ids, id_to_details = normalize_employee_data(employees)

# # Print the results
# print("Department to IDs:", dept_to_ids)
# print("ID to Details:", id_to_details)

def employee_data(emp_list):
    dept_to_id={}
    id_to_detalis={}
    for employee in emp_list:
        emp_id=emp_list['id']
        emp_dep=emp_list['department']
        id_to_detalis[emp_id]=employee
        #this means we store the entire employee dictionary 
