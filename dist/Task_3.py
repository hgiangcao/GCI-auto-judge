from AutoJudge import check_task

def solve(number):

    flag = True
    for i in range (2,number//2):
           if (number%i==0):
                flag = False
                break

    return flag

#===========          IMPORTANT!!!         =============#
#=========== DO NOT MODIFY THE PART BELLOW =============#
#===== The part bellow is used to grade your score. DO NOT MODIFY!!! ==========#
check_task(solve,"task_3")



