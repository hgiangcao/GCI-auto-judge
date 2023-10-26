import os
from lib.AutoJudge import check_task_0

def Enter_Your_Name():
    name = input("Your name:")
    print("My name is:",name)
    return name

def Enter_Student_ID():
    student_ID = input("Student ID:")
    print("My student ID is:",student_ID)
    return student_ID


#===========          IMPORTANT!!!         =============#
#=========== DO NOT MODIFY THE PART BELLOW =============#
#===== The part bellow is used to grade your score. DO NOT MODIFY!!! ==========#
check_task_0(Enter_Your_Name,Enter_Student_ID)
