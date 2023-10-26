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

#load test

def load_current_result():
    data = blank_data

    data_load_from_file = np.load("lib/res.npy", allow_pickle=True)

    data["student_id"] = data_load_from_file.item().get("student_id")
    data["student_name"] = data_load_from_file.item().get("student_name")

    for i in range(4):
        data["task_" + str(i + 1)] = data_load_from_file.item().get("task_" + str(i + 1))

    return data
def save_data(data):
    np.save("lib/res.npy", data)
def update_score(task,score):
    data = load_current_result()

    data[task]= score-key_encode

    save_data(data)

def load_test(test_name):
    load_data = np.load("lib/lib.npy", allow_pickle=True)

    answer = load_data.item().get(test_name+"_answer")

    tests = answer ["test"] #load_data.item().get("test")
    answers =  answer ["answer"] #load_data.item().get("answer")

    return tests,answers
def check_task(fn,name_task):

    tests,answers = load_test(name_task)
    nTest = len(answers)
    score = 0

    for i in range (nTest):
        test = tests[i]
        correct_answer = answers[i]

        try:
            user_answer = fn(test)
        except Exception as e:
            print (e)
            user_answer = None

        if (correct_answer == user_answer):
            score+=1
        else:
            continue
            print("Input:",test ,".")
            print ("Expected answer:",correct_answer,".Your answer:",user_answer)
            print("")
    #nomalize to 100
    score = int (score/nTest*100)
    print("\n=========================================")
    print ("Your score for",name_task,"is:", score,"/100")
    print("=========================================\n")

    score = score

    #update task 1
    update_score(name_task,score)

    return score # to reduce the -1 code

def update_answer(name_task,ans):
    #user_answer.py
    #read current user_answer.npy
    #update answer of task_name
    #save to file again
    #
def check_task_1(fn,name_task):

    tests,answers = load_test(name_task)
    nTest = len(answers)
    score = 0
    ans = []

    for i in range (nTest):
        test = tests[i]

        try:
            user_answer = fn(test)
            ans.append(user_answer)
        except Exception as e:
            print (e)
            user_answer = None

    #nomalize to 100
    print("\n=========================================")
    print ("Your code for",name_task,"is successfully executed. Click 'Refresh' on the GCI_Auto_Judge to update the result.")
    print("=========================================\n")

    update_answer(name_task,ans)

    return score # to reduce the -1 code
