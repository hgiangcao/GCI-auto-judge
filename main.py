from tkinter import *
from tkinter import Entry
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

def set_text(entry,text):
    entry.configure(state='normal')
    entry.delete(0,END)
    entry.insert(0,text)
    entry.configure(state='disabled')
    return

def load_current_result():
    data = blank_data

    data_load_from_file = np.load("res.npy", allow_pickle=True)


    data["student_id"] = data_load_from_file.item().get("student_id")
    data["student_name"] = data_load_from_file.item().get("student_name")

    for i in range(4):
        data["task_" + str(i + 1)] = data_load_from_file.item().get("task_" + str(i + 1))

    return data
def refresh():

    global total_score,detail_score,lb_total_score,student_id,name,txt_student_id,txt_student_name,lb_detail_score

    data =load_current_result()

    #random data
    name = data["student_name"]
    student_id = data["student_id"]

    if (name is None or student_id is None):
        name = "Not connected!"
        student_id = "Not connected!"

    set_text(txt_student_id, student_id)
    set_text(txt_student_name, name)

    for i in range (n_problem):
        detail_score[i] = data["task_"+str(i+1)]
        lb_detail_score[i].config(text=str(detail_score[i]+key_encode))

    lb_total_score.config(text=str(round((sum(detail_score)+n_problem*key_encode)/n_problem,1)))

    return

def saveInformation ():
    global txt_student_id, txt_student_name,btn_edit

    get_student_id = txt_student_id.get()
    get_student_name = txt_student_name.get()

    if (get_student_name!="" and get_student_name != ""):
        set_text(txt_student_id,get_student_id)
        set_text(txt_student_name, get_student_name)

        btn_save.place_forget()
        btn_save.config(state="disable")

        data = load_current_result()
        data["student_id"] = get_student_id
        data["student_name"] = get_student_name

        np.save("res.npy", data)
        print("Update information")

        txt_student_id.configure(bg="light gray")
        txt_student_name.configure(bg="light gray")

        btn_edit.place(x=345, y=110)
        btn_edit.config(state="normal")

    else:
        print("Null data")

def editInformation ():
    global txt_student_id, txt_student_name,btn_edit

    txt_student_id.configure(bg="light pink")
    txt_student_name.configure(bg="light pink")

    btn_edit.place_forget()
    btn_edit.config(state="disable")
    btn_save.place(x=345, y=110)
    btn_save.config(state="normal")

    txt_student_id.configure(state='normal')
    txt_student_name.configure(state='normal')
    print ("here")

#global variable
total_score =0
n_problem = 4
detail_score = [-1]*n_problem
student_id,name ="Not connected!","Not connected!"

root = Tk(className='GCI Lab - Auto Judge')

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

btn_edit = Button(main_frame,text="Edit Information",command = editInformation,height= 1, width=15,bg="#3b5998", fg='white',font=btn_font, cursor="hand2")
btn_edit.place(x=345, y=110)

btn_save = Button(main_frame,text="Save!",command = saveInformation,height= 1, width=15,bg="red", fg='white',font=btn_font, cursor="hand2")
btn_save.place(x=345, y=110)
btn_save.place_forget()


#username & student ID
lb_student_id = Label(main_frame, text = "Student ID:",font = btn_normal, fg="black",bg="#ffffff",height= 1, width=15,anchor="w",justify="left")
lb_student_id.place(x =50, y = 85)
txt_student_id = Entry(main_frame,width=25,bg="#f7f7f7",state="normal")
txt_student_id.place(x =130, y = 87)
#set_text(txt_student_id,student_id)

lb_student_name = Label(main_frame, text = "Student Name:",font = btn_normal, fg="black",bg="#ffffff",height= 1, width=30,anchor="w",justify="left")
lb_student_name.place(x =23, y = 110)
txt_student_name = Entry(main_frame,width=25,bg="#f7f7f7",state="normal")
txt_student_name.place(x =130, y = 113)
#set_text(txt_student_name,name)

#total_score
lb_total_score = Label(main_frame, text = "0",font = btn_score, fg="dark green",bg="#ffffff",height= 1, width=4)
lb_total_score.place(x = 515, y = 100)

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