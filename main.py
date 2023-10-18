from tkinter import *
from tkinter import font as tkFont
from tkinter import simpledialog
import random
import numpy as np
#def
key_encode = 1234
blank_data = {
            "student_id": "Not connected!",
            "student_name": "Not connected",
            "task_1": -key_encode,
            "task_2": -key_encode,
            "task_3": -key_encode,
            "task_4": -key_encode,
        }
def load_current_result():
    data = blank_data

    data_load_from_file = np.load("res.npy", allow_pickle=True)


    data["student_id"] = data_load_from_file.item().get("student_id")
    data["student_name"] = data_load_from_file.item().get("student_name")

    for i in range(4):
        data["task_" + str(i + 1)] = data_load_from_file.item().get("task_" + str(i + 1)) + key_encode

    return data
def refresh():

    global total_score,detail_score,lb_total_score,student_id,name

    data =load_current_result()

    #random data
    name = data["student_name"]
    student_id = data["student_id"]

    lb_student_name.config(text="Student Name:" + name)
    lb_student_id.config(text="Student ID:" + student_id)

    for i in range (n_problem):
        detail_score[i] = data["task_"+str(i+1)]
        lb_detail_score[i].config(text=str(detail_score[i]))

    lb_total_score.config(text=str(int(sum(detail_score)/n_problem)))

    return

def updateInformation(edit=True):
    data = load_current_result()

    name = data["student_name"]
    student_id = data["student_id"]
    print (name,student_id,edit)

    if ((name.find("Not")!= -1 or student_id.find("Not")!= -1) or edit):
        new_student_id, new_name = "",""

        while (new_student_id == "" or new_name == ""):
            input_student_id = simpledialog.askstring(title="Student ID", prompt="Student ID")
            input_student_name = simpledialog.askstring(title="Your English Name", prompt="Your Name")

            new_student_id, new_name = input_student_id, input_student_name
            print (new_student_id, new_name)

        student_id, name = input_student_id, input_student_name
        data["student_id"] = input_student_id
        data["student_name"] = input_student_name

        np.save("res.npy", data)
        print ("Update information")

    if edit:
        refresh()


    return student_id, name

#global variable
total_score =0
n_problem = 4
detail_score = [-1]*n_problem
student_id,name ="Not connected!","Not connected!"



root = Tk(className='GCI Lab - Auto Judge')
root.withdraw()
student_id,name = updateInformation(edit=False)
root.deiconify()

#setup font
btn_font = tkFont.Font(family='Helvetica', size=10, weight=tkFont.BOLD)
btn_score = tkFont.Font(family='Helvetica', size=25, weight=tkFont.BOLD)
btn_normal = tkFont.Font(family='Helvetica', size=11)
btn_normal_bold = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD)

# Set window size
root.geometry("620x460")
#bg
# Add image file
bg = PhotoImage(file="bg_sm_new.png")
# Create Canvas

main_frame  = Frame(root,width=620, height=460)
main_frame.pack(side=TOP)

canvas1 = Canvas(main_frame, width=620,   height=460)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")

#create button REFRESH
btn_refresh = Button(main_frame,text="Refresh!",command = refresh,height= 2, width=22,bg="#3b5998", fg='white',font=btn_font, cursor="hand2")
btn_refresh.place(x=230, y=366)

btn_edit = Button(main_frame,text="Edit Information",command = updateInformation,height= 1, width=15,bg="#3b5998", fg='white',font=btn_font, cursor="hand2")
btn_edit.place(x=345, y=110)


#username & student ID
lb_student_id = Label(main_frame, text = "Student ID:" + student_id,font = btn_normal, fg="black",bg="#ffffff",height= 1, width=30,anchor="w",justify="left")
lb_student_id.place(x =23, y = 85)

lb_student_name = Label(main_frame, text = "Student Name:" +name,font = btn_normal, fg="black",bg="#ffffff",height= 1, width=30,anchor="w",justify="left")
lb_student_name.place(x =23, y = 110)

#total_score
lb_total_score = Label(main_frame, text = "0",font = btn_score, fg="dark green",bg="#ffffff",height= 1, width=3)
lb_total_score.place(x = 525, y = 100)

#detail score
lb_detail_score =[0]*n_problem
lb_detail_task_name =[0]*n_problem
startX,stepX = 55,140
for i in range (n_problem):
    detail_task_name = "Task " +str(i+1)
    lb_detail_task_name[i] = Label(main_frame, text=detail_task_name, font=btn_normal_bold, fg="black", bg="white", height=2, width=8, bd=1)
    lb_detail_task_name[i].place(y=190, x=startX + stepX * i)

    lb_detail_score[i] = Label(main_frame, text = str(detail_score[i]),font = btn_normal_bold, fg="dark green",bg="light green",height= 4, width=8,bd=1)
    lb_detail_score[i].place(y = 235, x = startX + stepX*i)


refresh()
root.mainloop()