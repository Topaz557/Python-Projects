class User: ## Here I am creating the user class and assinging it attributes
    name = 'No Name Provided'
    email = ' '
    password = '1234abcd'
    account_number = 0

class Employee(User): ## here I am creating the user class employee, this will become a child class with the attributes assinged from above
    base_pay = 11.00
    department = 'General'
# above are the attributes that will only be added to the child class employee
class Customer(User): # child class customer will inherit all attributes from user
    mailing_address = ' '
    billing_address = ' '
    mailing_list = True
# above are the attributes that will only be added to the child class Customer, 
