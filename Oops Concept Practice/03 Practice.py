# Create a function in python showEmployee() in such a way that it should accept employee name, and it's salary and display both and if the salry is missing in function call it should how it as 5000 (default)


class Employee:
    
    def __init__(self, name, salary = 5000):
        self.name = name 
        self.salary = salary 

    def showEmployee(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee salary: {self.salary}")


emp = Employee("Arfaj")
emp2 = Employee("Mohammad", 40000)

emp.showEmployee()
emp2.showEmployee()


