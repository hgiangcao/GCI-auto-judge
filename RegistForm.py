from tkinter import *
from tkinter import font as tkFont
import random
import numpy as np
#def

def load_current_result():
    data = blank_data

    data_load_from_file = np.load("res.npy", allow_pickle=True)

    data["student_id"] = data_load_from_file.item().get("student_id")
    data["student_name"] = data_load_from_file.item().get("student_name")

    for i in range(4):
        data["task_" + str(i + 1)] = data_load_from_file.item().get("task_" + str(i + 1))

    return data
def refresh():

    global total_score,detail_score,lb_total_score,student_id,name

    data = np.load("res.npy", allow_pickle=True)

    #random data
    name = data.item().get("student_name")
    student_id = data.item().get("student_id")

    lb_student_name.config(text="Student Name:" + name)
    lb_student_id.config(text="Student ID:" + student_id)

    if (name.find("Not")!= -1 or student_id.find("Not")!= -1):
        print("Finish Task 0 to enter your name and your student ID")
        return



    for i in range (n_problem):
        detail_score[i] = data.item().get("task_"+str(i+1))
        lb_detail_score[i].config(text=str(detail_score[i]))

    lb_total_score.config(text=str(int(sum(detail_score)/n_problem)))

    return


#global variable
student_id,name ="Not connected!","Not connected!"

root = Tk(className='GCI Lab - Auto Judge')
#setup font
btn_font = tkFont.Font(family='Helvetica', size=10, weight=tkFont.BOLD)
btn_score = tkFont.Font(family='Helvetica', size=25, weight=tkFont.BOLD)
btn_normal = tkFont.Font(family='Helvetica', size=11)
btn_normal_bold = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD)

# Set window size
root.geometry("400x200")


main_frame  = Frame(root,width=400, height=200)
main_frame.pack(side=TOP)

#label

#input

#button



root.mainloop()