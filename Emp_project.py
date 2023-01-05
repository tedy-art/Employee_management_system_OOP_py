db = []

def dashboard():
    print("\t Welcome to CRUD project using OOp by Batch 459")

    print("""
                ******** Menu *********
                1. Add Employee
                2. Display Employee
                3. Update Employee
                4. Delete Employee
                5. Search Employee
                6. Find salary
    
    """)

class Employee:
    def __init__(self, nm, id, sal, dept):
        self.name = nm
        self.ID = id
        self.salary = sal
        self.dapartment = dept

    def add_employee(self):
        nm = input('Enter employee name : ')
        id = eval(input('Enter employee ID : '))
        sal = eval(input('Enter employee salary : '))
        dept = input('Enter employee dapartment name : ')

        e1 = Employee(nm = nm, id = id, sal = sal, dept = dept)
        db.append(e1)
        print(f'Employess {e1.name} added successfully in the database')

    def diplay_employee(self):

        print('-'*85)
        print("|{i:^20}|{n:^20}|{s:^20}|{d:^20}|".format(i = 'E_id', n = 'Name', s = 'salary', d = 'dapartment'))

        print('-'*85)
        for i in db:
            print("|{i:^20}|{n:^20}|{s:^20}|{d:^20}|".format(i = i.ID, n = i.name, s = i.salary, d = i.dapartment))
            print('-'*85)

    def search_employee(self):
        e_id = eval(input("Enter employee id : "))
        for i in range(len(db)):
            if db[i].ID == e_id:
                # print('Employee found in data base')
                return i
        return -1

    def delete_employee(self):
        i = dummy_obj.search_employee()
        if i >= 0:
            del db[i]
            print("Record deleted successfully from db...")
        else:
            print('Employee ID not found in DB...')

    def update_employee(self):
        i = dummy_obj.search_employee()
        if i >= 0:
            nm = input('Enter Updated employee name : ')
            # id = eval(input('Enter employee ID : '))
            sal = eval(input('Enter updated employee salary : '))
            dept = input('Enter updated employee dapartment name : ')

            db[i].name = nm
            db[i].salary = sal
            db[i].dapartment = dept
            print("Record is updated successfully in db....")
        else:
            print("Employee id is not found in DB....")

    def salary_employee(self):
        find_salary = eval(input("Enter salary :"))
        print('-' * 85)
        print("|{i:^20}|{n:^20}|{s:^20}|{d:^20}|".format(i='E_id', n='Name', s='salary', d='dapartment'))

        print('-' * 85)
        for i in db:
            if find_salary <= i.salary:
                print("|{i:^20}|{n:^20}|{s:^20}|{d:^20}|".format(i=i.ID, n=i.name, s=i.salary, d=i.dapartment))
                print('-' * 85)

    def __str__(self):
        return self.name

dummy_obj = Employee('', 0, 0,'')
e1 = Employee(nm = 'jay', id = 101, sal = 15000, dept = 'IT')
e2 = Employee(nm = 'veru', id = 102, sal = 30000, dept = 'HR')
e3 = Employee(nm = 'Mai', id = 103, sal = 55000, dept = 'Admin')
e4 = Employee(nm = 'John', id = 104, sal = 65000, dept = 'IT')
db.append(e1)
db.append(e2)
db.append(e3)
db.append(e4)


while True:
    dashboard()
    choise = eval(input("Enter your choice[1, 2, 3, 4, 5, 6] : "))

    if choise == 1:
        dummy_obj.add_employee()

    elif choise == 2:
        if len(db) != 0:
            dummy_obj.diplay_employee()
        else:
            print("No record in Data base....")

    elif choise == 3:
        if len(db) != 0:
            dummy_obj.update_employee()
        else:
            print("No record in Data base....")

    elif choise == 4:
        if len(db) != 0:
            dummy_obj.delete_employee()
        else:
            print("No record in Data base....")
    
    elif choise == 5:
        if len(db) != 0:
            i = dummy_obj.search_employee()
            if i >= 0:
                print("Employee found in data base...")
            else:
                print("Employee Id not found in DB...")
        else:
            print("No record in Data base....")

    elif choise == 6:
        if len(db) != 0:
            dummy_obj.salary_employee()
        else:
            print("No record in Data base....")
    else:
        print("Invalid choice...")

    ch = input("Do you want to continue[y/n] : ")
    if ch.lower() != 'y':
        # print(db)
        break