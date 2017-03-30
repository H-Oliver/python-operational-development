name = str(input('Name:'))
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

info = '''
-------------info of %s ----------
Name:%s
Age:%d
Job:%s
Salary:%s
''' % (name,name,age,job,salary)

info2= '''
-------------info of {_name} ----------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=name,
            _age=age,
            _job=job,
            _salary=salary)
print(info2)