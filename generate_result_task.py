import numpy as np
import random


def generate_task_1_results():
    dict={}
    nTest = 200
    tests=[]
    answers=[]

    for i in range (nTest):
        nNumber = random.randint(5,20)
        arr =[]
        for j in range (nNumber):
            arr.append(random.randint(-999,999))

        ans = max(arr)

        tests.append(arr)
        answers.append(ans)

    dict["test"] = tests
    dict["answer"] = answers

    np.save("task_1_res.npy", dict)

def generate_task_2_results():
    dict={}
    nTest = 200
    tests=[]
    answers=[]

    for i in range (nTest):
        number = random.randint(-99999,99999)

        ans = (number%5==0)
        tests.append(number)
        answers.append(ans)

    dict["test"] = tests
    dict["answer"] = answers

    np.save("task_2_res.npy", dict)

def generate_task_3_results():
    dict={}
    nTest = 200
    tests=[]
    answers=[]

    for i in range (nTest):
        number = random.randint(0,9999999)

        ans = False

        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    ans = True
                    break


        tests.append(number)
        answers.append(ans)

    dict["test"] = tests
    dict["answer"] = answers

    np.save("task_3_res.npy", dict)


def generate_task_4_results():
    dict={}
    nTest = 200
    tests=[]
    answers=[]

    for i in range (nTest):
        number = random.randint(41,9999999)

        ans = number

        while (ans > 0):
            if(ans%41==0):
                break
            else:
                ans-=1


        tests.append(number)
        answers.append(ans)

    dict["test"] = tests
    dict["answer"] = answers

    np.save("task_4_res.npy", dict)

def generate_task_5_results():
    dict={}
    nTest = 200
    tests=[]
    answers=[]

    for i in range (nTest):
        number = random.randint(0,11)

        ans = 1

        for i in range (2,number+1):
            ans *=i

        tests.append(number)
        answers.append(ans)

    dict["test"] = tests
    dict["answer"] = answers

    np.save("task_4_res.npy", dict)

generate_task_1_results()
generate_task_2_results()
generate_task_3_results()
generate_task_4_results()
generate_task_5_results()
