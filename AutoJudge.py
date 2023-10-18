import numpy as np

key_encode = 1234

blank_data = {
            "student_id": "Not connected!",
            "student_name": "Not connected",
            "task_1": -key_encode,
            "task_2": -key_encode,
            "task_3": -key_encode,
            "task_4": -key_encode,
        }
def check_task_0 (fn_name,fn_student_id):
    name ="Not connected!"
    student_id = "Not connected!"
    try:
        name = fn_name()
        student_id = fn_student_id()

        if (name is None or student_id is None):
            print ("Please enter your name and your student ID")
            raise Exception("Please enter your name and your student ID")

        #init data
        data =blank_data

        data_load_from_file = np.load("res.npy", allow_pickle=True)

        data["student_id"] = data_load_from_file.item().get("student_id")
        data["student_name"] = data_load_from_file.item().get("student_name")

        for i in range (4):
            data["task_"+str(i+1)] =  data_load_from_file.item().get("task_"+str(i+1))


        #update new data
        data["student_id"] = student_id
        data["student_name"] = name

        np.save("res.npy", data)

        # print ("Task 0 is completed!. Congratulation. Keep solving other task! Good Luck!")
        print ("Hello,",name,"(",student_id,").\nWelcome to the Advance Python Programming course.\nNow, time to solve the problems.\nGood Luck to you!")

    except:
        print("Task 0 is NOT CORRECT. CORRECT YOUR SOLUTION!")


#load test

def load_current_result():
    data = blank_data

    data_load_from_file = np.load("res.npy", allow_pickle=True)

    data["student_id"] = data_load_from_file.item().get("student_id")
    data["student_name"] = data_load_from_file.item().get("student_name")

    for i in range(4):
        data["task_" + str(i + 1)] = data_load_from_file.item().get("task_" + str(i + 1))

    return data
def save_data(data):
    np.save("res.npy", data)
def update_score(task,score):
    data = load_current_result()

    data[task]= score-key_encode

    save_data(data)

def load_test(test_name):
    load_data = np.load("answer.npy", allow_pickle=True)

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
            print("Input:",test ,".")
            print ("Expected answer:",correct_answer,".Your answer:",user_answer)
            print("")
    #nomalize to 100
    score = int (score/nTest*100)
    print ("Your score for",name_task,"is:", score,"/100")

    #update task 1
    update_score(name_task,score)

    return score
