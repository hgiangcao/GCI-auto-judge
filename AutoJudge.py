import numpy as np

key_encode = 1234

blank_data = {
            "student_id": "Not connected!",
            "student_name": "Not connected",
            "task_1": -key_encode-1,
            "task_2": -key_encode-1,
            "task_3": -key_encode-1,
            "task_4": -key_encode-1,
        }

blank_user_answer = {
            "task_1_user_answer": None,
            "task_2_user_answer": None,
            "task_3_user_answer": None,
            "task_4_user_answer": None,
        }

#load test

def load_test(test_name):
    load_data = np.load("lib/lib.npy", allow_pickle=True)

    answer = load_data.item().get(test_name+"_answer")

    tests = answer ["test"] #load_data.item().get("test")
    answers =  answer ["answer"] #load_data.item().get("answer")

    return tests,answers

def update_answer(name_task,ans):
    #print (ans)
    user_answer = blank_user_answer
    data_load_from_file = np.load("lib/user_answer.npy", allow_pickle=True)

    for i in range (1,4+1):
        user_answer["task_"+str(i)+"_user_answer"] = data_load_from_file.item().get("task_"+str(i)+"_user_answer")


    user_answer[name_task + "_user_answer"] = ans
    np.save("lib/user_answer.npy", user_answer)


def check_task(fn,name_task):

    tests,answers = load_test(name_task)
    nTest = len(answers)
    score = 0
    ans = []

    for i in range (nTest):
        test = tests[i]
        user_answer = None
        try:
            user_answer = fn(test)

        except Exception as e:
            print (e)
            # = None

        ans.append(user_answer)

    #nomalize to 100
    print("\n=========================================")
    print ("Your code for",name_task,"is successfully executed. Click 'Refresh' on the GCI_Auto_Judge to update the result.")
    print("=========================================\n")

    update_answer(name_task,ans)

    return score # to reduce the -1 code
