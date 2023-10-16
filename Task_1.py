from AutoJudge import check_task

def solve(arr):
    l = len(arr)
    max_value = arr[0]
    for i in range (l):
            if ( arr[i] > max_value):
                max_value = arr[i]

    return max_value

#===========          IMPORTANT!!!         =============#
#=========== DO NOT MODIFY THE PART BELLOW =============#
#===== The part bellow is used to grade your score. DO NOT MODIFY!!! ==========#
check_task(solve,"task_1")



