from AutoJudge import check_task

def solve(number):

    ans = 1
    for i in range (2,number+1):
        ans*=i

    return ans

#===========          IMPORTANT!!!         =============#
#=========== DO NOT MODIFY THE PART BELLOW =============#
#===== The part bellow is used to grade your score. DO NOT MODIFY!!! ==========#
check_task(solve,"task_4")



