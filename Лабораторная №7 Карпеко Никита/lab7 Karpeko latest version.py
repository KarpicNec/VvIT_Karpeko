class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def get_info(self):
        return f"{self.name}(id:{self.id})"
    
class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department
        
    def manage_project(self):
        print(f"I'm, {self.get_info()}, manager, I manage {self.department}")
        
class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization
        
    def perform_maintenance(self):
        print(f"I'm, {self.get_info()}, techic, I perform {self.specialization}")
        
class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.lst_of_emp = []
        
    def manage_project(self):
        print(f"I'm, {self.get_info()}, TechManager, I can manage {self.department}")
        
    def perform_maintenance(self):
        print(f"I'm, {self.get_info()}, TechManager, I can perform {self.specialization}")
        
    def add_employee(self, emp):
        self.lst_of_emp.append(emp)
        
    def get_team_info(self):
        print(f"In work with {self.get_info()}")
        for i in self.lst_of_emp:
            print(i.get_info())


emp1 = Employee("Astrid", "10001")
emp2 = Employee("Benjamin", "10002") 
emp3 = Employee("Charlie", "10003")

manager = Manager("David", "10004", "sellings")
manager.manage_project()

technic = Technician("Edwin", "10005", "big_data")
technic.perform_maintenance()

print()

tech_manager = TechManager("Franklin", "10006", "production", 'science')

tech_manager.add_employee(emp1)
tech_manager.add_employee(emp2)
tech_manager.add_employee(emp3)
tech_manager.add_employee(manager)
tech_manager.add_employee(technic)

tech_manager.get_team_info()
print()
tech_manager.manage_project()
tech_manager.perform_maintenance()
