from AutoJudge import check_task

def solve(number):

    while (number>0):
        if(number%20==0):
            return number
        else:
            number-=1

    return number

#===========          IMPORTANT!!!         =============#
#=========== DO NOT MODIFY THE PART BELLOW =============#
#===== The part bellow is used to grade your score. DO NOT MODIFY!!! ==========#
check_task(solve,"task_4")



