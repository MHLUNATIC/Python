name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

if salary.isdigit():
    salary = int(salary)
# else:
#     exit("must input digit")    #推出程序

#需要下面这种固定格式的输出
msg = """
-   -----info of %s------
Name: = %s
Age: = %d
Job: = %s
Salary: = %f
you will be retired in %s years
----------end---------
"""%(name,name,age,job,salary,65-age)

print(msg)