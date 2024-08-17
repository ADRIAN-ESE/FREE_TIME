
name = input("Enter your name: ")
request = input("Enter your request: ")
print("Hello " + name + "! You're request for the " + request + " is pending ")

height= float(input("enter height: "))
age = int(input("enter age: "))

if height < 200 or age < 37:
    print("eligible")
else:
    print("ineligible")

educationlevel = input("Enter level of education")
secondeducationlevel = input('Enter second level of education')


job = input("Enter desired job: ")
level = input("Enter your starting level: ")
salary = input("Enter your salary: ")
print("Approved for the role " + job + " in the company,Your " + level + " level is agreed upon and you have been "
                                                                        "approved for the salary of " + salary)