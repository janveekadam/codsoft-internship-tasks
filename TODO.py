from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql
from tkinter.messagebox import *


def add_task():
	task_string = ent_task.get()
	if len(task_string) == 0:
		messagebox.showerror("Invalid Input", "Field is empty.")
	else:
		tasks.append(task_string)
		the_cursor.execute('insert into tasks values (?)', (task_string ,))
		list_update()
		ent_task.delete(0, 'end')
	

def list_update():
	clear_list()
	for task in tasks:
		task_listbox.insert('end', task)

def delete_task():
	try:
		the_value = task_listbox.get(task_listbox.curselection())
		if the_value in tasks:
			tasks.remove(the_value)
			list_update()	
			the_cursor.execute('delete from tasks where title = ?', (the_value,))
	except:
		messagebox.showinfo("Issue", "No Task Selected, Cannot Delete.")

def delete_all_tasks():
	message_box = messagebox.askyesno("Delete All", "Are u sure to delete all tasks?")
	if message_box == True:
		while(len(tasks) != 0):
			tasks.pop()
		the_cursor.execute("Delete from tasks")
		list_update()

def clear_list():
	task_listbox.delete(0, 'end')



def retrieve_database():
	while(len(tasks) != 0):
		tasks.pop()
	for row in the_cursor.execute('select title from tasks'):
		tasks.append(row[0])
	retrieve_database()
	list_update()

root = Tk()
root.geometry("550x450+300+100")
root.config(bg="turquoise")
root.resizable(0, 0)
root.title("TO-DO LIST APP")
f = ("Arial", 18, "bold")

the_connection = sql.connect('task.db')
the_cursor = the_connection.cursor()
the_cursor.execute('create table if not exists tasks (title text)')


tasks = []

lab_wlc = Label(root, text = "Welcome to To-Do List", font=f, bg="rosybrown")
lab_wlc.pack(pady=10)

lab_task = Label(root, text= "Enter Tasks", font=f, bg="rosybrown")
lab_task.place(x=80, y=70)

ent_task = Entry(root, font=f)
ent_task.place(x=20, y=120)

btn_add = Button(root, text="Add Task", font=f, width=15, command=add_task, bg="rosybrown")
btn_add.place(x=30, y=170)

btn_del = Button(root, text="Delete Task", font=f, width=15, command=delete_task, bg="rosybrown")
btn_del.place(x=30, y=240)

btn_del_all = Button(root, text="Delete All Tasks", font=f, width=15, command=delete_all_tasks, bg="rosybrown")
btn_del_all.place(x=30, y=310)


task_listbox = Listbox(root, width=15, height=13, font=f)
task_listbox.place(x=340, y=50)


def on_closing():
	print(tasks)
	if askyesno("Quit", "Do u want to close app?"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

btn_exit = Button(root, text="Exit", font=f, width=15, bg="rosybrown", command=on_closing)
btn_exit.place(x=30, y=380)

root.mainloop()

the_connection.commit()
the_cursor.close()






