#Contact book in python 

from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import requests
f=("Arial", 18, "bold","italic")

def f1():
	add_window.deiconify()
	root.withdraw()

def f2():
	root.deiconify()
	add_window.withdraw()

def f3():
	view_window.deiconify()
	root.withdraw()
	view_scrtxt.delete(1.0, END)
	info = ""
	con = None
	try:
		con = connect("contact.db")

		cursor = con.cursor()
		sql = "select * from contact"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			info = info + "name:" + str(d[0]) + ", num: " + str(d[1])  + "\n"
		view_scrtxt.insert(INSERT, info)
	except Exception as e:
		showerror("Issue", e)
	finally:
		if con is None:
			con.close()
def f4():
	root.deiconify()
	view_window.withdraw()

def f5():
	update_window.deiconify()
	root.withdraw()

def f6():
	root.deiconify()
	update_window.withdraw()

def f7():
	delete_window.deiconify()
	root.withdraw()

def f8():
	root.deiconify()
	delete_window.withdraw()
		

def valid_name(name):
	if name == "" or name.strip() == "":
		showerror("Issue", "Name cannot be empty.")
		return False
	elif not name.isalpha():
		showerror("Issue", "Name should be only alphabets.")
		return False
	elif len(name) < 2:
		showerror("Issue", "Name length should be min 2.")
		return False
	return True

def valid_num(num):
	if not num:
		showerror("Issue","Phone no cannot be empty.")
		return False
	elif not num.isdigit():
		showerror("Issue","Phone no cannot be text.")
		return False
	elif len(num) < 10 or len(num) > 10:
		showerror("Issue","Phone no length should be 10.")
		return False

	try:
		int(num)
	except ValueError:
		showerror("Invalid Input", "Please enter numbers only.")
		return False
	return True

def valid_n_name(n_name):
	if (n_name) == "" or (n_name).strip() == "":
		showerror("Issue", "Name cannot be empty.")
		return False
	elif not (n_name).isalpha():
		showerror("Issue", "Name should be only alphabets.")
		return False
	elif len(n_name) < 2:
		showerror("Issue", "Name length should be min 2.")
		return False
	return True

def valid_new_num(new_num):
	if not new_num:
		showerror("Issue","Phone no cannot be empty.")
		return False
	elif not new_num.isdigit():
		showerror("Issue","Phone no cannot be text.")
		return False
	elif len(new_num) < 10 or len(new_num) > 10:
		showerror("Issue","Phone no length should be 10.")
		return False

	try:
		int(new_num)
	except ValueError:
		showerror("Invalid Input", "Please enter numbers only.")
		return False
	return True

def f9():
	con = None
	try:
		con = connect("contact.db")
		cursor = con.cursor()
		sql = "insert into contact values('%s','%s')"
		name = aw_ent_name.get()
		num = aw_ent_num.get()
		
		if not valid_name(name):
			aw_ent_name.delete(0,END)
			aw_ent_name.focus()
			return
		
		elif not valid_num(num):
			aw_ent_num.delete(0,END)
			return

		cursor.execute(sql % (name, int(num)))
		con.commit()
		showinfo("Success", "New contact created.")
	except Exception as e:
		showerror("Issue", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

	aw_ent_name.delete(0,END)
	aw_ent_num.delete(0,END)
	aw_ent_name.focus()	


def f10():
	con = None
	n_name = uw_ent_name.get()
	new_num = uw_ent_num.get()
	try:
		con = connect("contact.db")
		cursor = con.cursor()
		sql = "update contact SET num='%d' where name='%s'" % (int(new_num), str(n_name)) 
		
		if not valid_n_name(n_name):
			uw_ent_name.delete(0,END)
			uw_ent_name.focus()
			return
		
		elif not valid_new_num(new_num):
			uw_ent_num.delete(0,END)
			return

		cursor.execute(sql)
		con.commit()

		if cursor.rowcount == 1:
			showinfo("Success", "Contact updated.")
		else:
			showerror("Invalid Input", f"Contact with name {n_name} does not exist.")
	except Exception as e:
		showerror("Issue", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
	
	uw_ent_name.delete(0,END)
	uw_ent_num.delete(0,END)
	uw_ent_name.focus()

def f11():
	con = None
	try:
		con = connect("contact.db")
		cursor = con.cursor()
		sql = "delete from contact where name = '%s'"
		name = dw_ent_name.get()

		if not valid_name(name):
			dw_ent_name.delete(0, END)
			dw_ent_name.focus()
			return

		cursor.execute(sql % name)
		if cursor.rowcount == 1:
			showinfo("Success", "Contact Deleted.")
			con.commit()
		else:
			showerror("Invalid Input", f"Contact with name {name} does not exist.")
	except Exception as e:
		showerror("Issue", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
	dw_ent_name.delete(0, END)
	dw_ent_name.focus()



root = Tk()
root.title("Contact book System")
root.geometry("450x400+350+100")
root.resizable(False,False)
root.config(bg="plum")

lab_wel = Label(root, text="Welcome to Contact Book", font=f, bg="plum")
lab_wel.pack(pady=20)

btn_add = Button(root, text="Add Contact",width=15, font=f, command=f1, bg="lightblue")
btn_add.pack()
btn_view = Button(root, text="View Contact",width=15, font=f, command=f3, bg="lightblue")
btn_view.pack(pady=8)
btn_update = Button(root, text="Update Contact",width=15, font=f, command=f5, bg="lightblue")
btn_update.pack(pady=8)
btn_delete = Button(root, text="Delete Contact",width=15, font=f, command=f7, bg="lightblue")
btn_delete.pack(pady=8)


add_window = Tk()
add_window.title("ADD CONTACTS")
add_window.geometry("550x500+350+100")
add_window.resizable(False,False)
add_window.config(bg="skyblue")

lab_wlc = Label(add_window, text="Welcome to Add Contact", font=f, bg="lightblue")
lab_wlc.pack(pady=10)

aw_lab_name = Label(add_window, text="Enter Name", font=f, bg="lightblue")
aw_lab_name.pack(pady=10)
aw_ent_name = Entry(add_window, font=f)
aw_ent_name.pack()

aw_lab_num = Label(add_window, text="Enter Phone Number", font=f, bg="lightblue")
aw_lab_num.pack(pady=10)
aw_ent_num = Entry(add_window, font=f)
aw_ent_num.pack()

btn_save = Button(add_window, text="Save", font=f, bg="lightblue",command=f9)
btn_save.pack(pady=10)
btn_back = Button(add_window,text="Back", font=f, bg="lightblue", command=f2)
btn_back.pack()
add_window.withdraw()



view_window = Tk()
view_window.title("VIEW CONTACTS")
view_window.geometry("550x500+350+100")
view_window.resizable(False,False)
view_window.config(bg="skyblue")

lab_wlc = Label(view_window, text="Welcome to View Contacts", font=f, bg="lightblue")
lab_wlc.pack(pady=10)
view_scrtxt = ScrolledText(view_window, font=f, height=12, width=40)
view_scrtxt.pack(pady=10)
btn_back = Button(view_window,text="Back", font=f, bg="lightblue", command=f4)
btn_back.pack(pady=10)
view_window.withdraw()



update_window = Tk()
update_window.title("UPDATE CONTACTS")
update_window.geometry("550x500+350+100")
update_window.resizable(False,False)
update_window.config(bg="skyblue")

lab_wlc = Label(update_window, text="Welcome to Update Contact", font=f, bg="lightblue")
lab_wlc.pack(pady=10)

uw_lab_name = Label(update_window, text="Enter Name", font=f, bg="lightblue")
uw_lab_name.pack(pady=10)
uw_ent_name = Entry(update_window, font=f)
uw_ent_name.pack()

uw_lab_num = Label(update_window, text="Enter Phone Number", font=f, bg="lightblue")
uw_lab_num.pack(pady=10)
uw_ent_num = Entry(update_window, font=f)
uw_ent_num.pack()

btn_save = Button(update_window, text="Update", font=f, bg="lightblue", command=f10,width=10)
btn_save.pack(pady=10)
btn_back = Button(update_window,text="Back", font=f, bg="lightblue", command=f6,width=10)
btn_back.pack()
update_window.withdraw()



delete_window = Tk()
delete_window.title("DELETE CONTACTS")
delete_window.geometry("550x500+350+100")
delete_window.resizable(False,False)
delete_window.config(bg="skyblue")

lab_wlc = Label(delete_window, text="Welcome to Delete Contact", font=f, bg="lightblue")
lab_wlc.pack(pady=10)

dw_lab_name = Label(delete_window, text="Enter Name", font=f, bg="lightblue")
dw_lab_name.pack(pady=10)
dw_ent_name = Entry(delete_window, font=f)
dw_ent_name.pack()

btn_save = Button(delete_window, text="Delete", font=f, bg="lightblue", command=f11, width=10)
btn_save.pack(pady=10)
btn_back = Button(delete_window,text="Back", font=f, bg="lightblue", command=f8, width=10)
btn_back.pack()
delete_window.withdraw()


def on_closing():
	if askyesno("Quit", "Do u want to quit?"):
		root.destroy()
		add_window.destroy()
		view_window.destroy()
		update_window.destroy()
		delete_window.destroy()
	
root.protocol("WM_DELETE_WINDOW", on_closing)
add_window.protocol("WM_DELETE_WINDOW", on_closing)
view_window.protocol("WM_DELETE_WINDOW", on_closing)
update_window.protocol("WM_DELETE_WINDOW", on_closing)
delete_window.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()