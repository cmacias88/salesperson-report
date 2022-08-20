# """Generate sales report showing total melons each salesperson sold."""

# salespeople = []
# melons_sold = []

# f = open('sales-report.txt')

# # Possible Improvements: 
#     # 1) Use "with open(filename) as file" to close file after executing.
#     # 2) Better naming conventions for the lists and open file variable.
#     # 3) Create a function to begin file intake.
#     # 4) Use a dictionary rather than a list for salespeople and their sales.
# #      
# # ex: def salesreport(filename):
# #         with open(filename) as opened_file:

# for line in f:
#     line = line.rstrip()
#     entries = line.split('|')
#     salesperson = entries[0]
#     melons = int(entries[2])

# # Improvements: 
#     # 1) Condense line formatting as one line and list unpacking as another.

# # ex: for line in opened_file:
# #         employee_data = line.rstrip.split("|")
# #         salesperson, total_order_amount, melons_sold = employee_data

#     if salesperson in salespeople:
#         position = salespeople.index(salesperson)
#         melons_sold[position] += melons
        
#     else:
#         salespeople.append(salesperson)
#         melons_sold.append(melons)

# Possible Improvements: 
    # 1) Use a dictionary to create a unique key and more easily find employee's data.
    # 2) Use enumerate() to access the index and then data of employee
    # 3) Ask for user input for a new entry if not found.

# for i in range(len(salespeople)):
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')

# Possible Improvements: 
    # 1) List unpacking from earlier will make the final printed statement easier to format.
    # 2) Use a for loop to iterate through all the employees instead.

# Final Improved Code:

import sys

employee_data_list = []

sales_profiles = {}

def salesreport_data_slicing(filename):
    """Opens file and organizes the data given."""
    
    with open(filename) as opened_file:
        for line in opened_file:
            employee_data = line.rstrip().split('|')
            employee_data_list.append(employee_data)
    return employee_data_list

employee_data_list = salesreport_data_slicing('sales-report.txt')

def dictionary_sales_report(employee_data_list):
    """Return a dictionary containing all employee records."""

    for employee_info in employee_data_list: 
        full_name, total_order_amount, melons_sold = employee_info
        employee_profile = {
            full_name: {
                'Total Order Amount': total_order_amount,
                'Melons Sold': melons_sold
            }
        }
        sales_profiles.update(employee_profile)
    
    return sales_profiles

def sales_records_directory(sales_profiles):
    """Finds an employee's records through input and if not found, 
    prompts user to add entry."""

    user_fullname_input = input("Enter the full name of the employee whose record you would like to view: ").title()
    
    if user_fullname_input in sales_profiles.keys():
        print("Employee found!")
        print(sales_profiles[user_fullname_input])
    else:
        print("Employee not found.")
        user_new_entry_prompt = input("Would you like to create a data entry for them? (Enter Y or N.) ").upper()
        if user_new_entry_prompt == "Y":
            user_new_entry = input("Print employee's full name, total order amount and melons sold separated by commas: ")
            user_new_entry = user_new_entry.rstrip().split(",")
            full_name, total_order_amount, melons_sold = user_new_entry
            employee_profile = {
            full_name: {
                'Total Order Amount': total_order_amount,
                'Melons Sold': melons_sold
            }
        }
            print(f" {full_name} is now in the system: {employee_profile}")
            sales_profiles.update(employee_profile)
        elif user_new_entry_prompt == "N":
            show_all_data_prompt = input("Would you like to view all employee records? (Enter Y to view all or N/Q to quit.): ").upper()
            if show_all_data_prompt == "Y":
                print(sales_profiles)
            elif show_all_data_prompt == "N" or show_all_data_prompt == "Q":
                print("Goodbye!")
                exit()

filename = sys.argv[1]
employee_data = salesreport_data_slicing(filename)      
sales_profiles = dictionary_sales_report(employee_data)
print(sales_records_directory(sales_profiles))
