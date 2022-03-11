
import re

def validate():
    #print('start coding ,and remember ,delete this line')
    first_name = input('Enter the first name:')
    last_name = input('Enter the last name:')
    ZIP_code = input('Enter the ZIP code:')
    employee_id = input('Enter an employee ID:')
    if len(first_name) == 0:
        print('The first name must be filled in.')
    if (len(first_name) < 2 and len(first_name) > 0):
        print('\"'+first_name+'\" is not a valid first name. It is too short.')
    if len(last_name) == 0:
        print('The last name must be filled in.')
    if (len(last_name) < 2 and len(last_name) > 0):
        print('\"' + last_name + '\" is not a valid last name. It is too short.' )
    if ZIP_code.isnumeric() == False:
        print("The ZIP code must be numeric.")
    if re.match('^[A-Z]{2}\-[0-9]{4}$',employee_id) == None:
        print(employee_id+' is not a valid ID.')

    return
validate()