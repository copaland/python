from tkinter import *
import csv
from tkinter import messagebox

phonelist = []
def ReadCSVFile():
	global header
	with open('phoneBook.csv') as csvfile:
		csv_reader = csv.reader(csvfile,delimiter=',')
		header = next(csv_reader)
		for row in csv_reader:
			phonelist.append(row)
	set_select()		
	print(phonelist)

def WriteInCSVFile(phonelist):
	with open('phoneBook.csv','w',newline='') as csv_file:
		writeobj = csv.writer(csv_file,delimiter=',')
		writeobj.writerow(header)
		for row in phonelist:
			writeobj.writerow(row)


def WhichSelected():
	print("hello",len(select.curselection()))
	if len(select.curselection())==0:
		messagebox.showerror("Error", "이름을 선택해 주세요")
	else:
		return int(select.curselection()[0])
		


def AddDetail():
	if (" ".join(E_name.get().split())).strip()!="" and E_contact.get()!="":
		phonelist.append([(" ".join(E_name.get().split())).strip(),E_contact.get()])
		print(phonelist)
		WriteInCSVFile(phonelist)
		set_select()
		EntryReset()
		messagebox.showinfo("Confermation", "새로운 정보가 저장됨")
		
	else:
		messagebox.showerror("Error", "정보를 채워주세요")

def UpdateDetail():
	if (" ".join(E_name.get().split())).strip() and E_contact.get():
		phonelist[WhichSelected()] = [ (" ".join(E_name.get().split())).strip(), E_contact.get()]
		WriteInCSVFile(phonelist)
		messagebox.showinfo("Confirmation", "연락처가 갱신됨")
		EntryReset()
		set_select()

	elif not((" ".join(E_name.get().split())).strip()) and not(E_contact.get()) and not(len(select.curselection())==0):
		messagebox.showerror("Error", "정보를 채워 주세요")

	else:
		if len(select.curselection())==0:
			messagebox.showerror("Error", "Please Select the Name and \n press Load button")
		else:
			message1 = """To Load the all information of \n 
						  selected row press Load button\n.
						  """
			messagebox.showerror("Error", message1)

def EntryReset():
	E_name_var.set('')
	E_contact_var.set('')


def DeleteEntry():
	if len(select.curselection())!=0:
		result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
		if result==True:
			del phonelist[WhichSelected()]
			WriteInCSVFile(phonelist)
			set_select()
	else:
		messagebox.showerror("Error", 'Please select the Contact')

def LoadEntry():
    name, phone = phonelist[WhichSelected()]
    # print(name.split(' '))
    E_name_var.set(name)
    E_contact_var.set(phone)


def set_select():
    phonelist.sort(key=lambda record: record[1])
    select.delete(0, END)
    i=0
    for name, phone in phonelist:
    	i+=1
    	select.insert(END, f"{i}  |    {name}   |   {phone}")


window = Tk()

Frame1 = LabelFrame(window,text="폰북 입력창")
Frame1.grid(padx=15,pady=15)


Inside_Frame1 = Frame(Frame1)
Inside_Frame1.grid(row=0,column=0,padx=15,pady=15)
#---------------------------------------------
l_name = Label(Inside_Frame1,text="이름",font=("Arial Bold",12),)
l_name.grid(row=0,column=0,padx=5,pady=5)
E_name_var = StringVar()
E_name_var = E_name_var.replace(" " , "") #공백제거

E_name = Entry(Inside_Frame1,width=30, textvariable=E_name_var)
E_name.grid(row=0,column=1,padx=5,pady=5)
#---------------------------------------------------
l_contact= Label(Inside_Frame1,text="연락처",font=("Arial Bold",12),)
l_contact.grid(row=2,column=0,padx=5,pady=5)
E_contact_var = StringVar()
E_contact = Entry(Inside_Frame1,width=30,textvariable=E_contact_var)
E_contact.grid(row=2,column=1,padx=5,pady=5)
#---------------------------------------------------
Frame2 = Frame(window)
Frame2.grid(row=0,column=1,padx=15,pady=15,sticky=E)
#<><><><><><><><><><><><><><<><<<><><<<><><><><><><><><><>
Add_button = Button(Frame2,text="추가",width=15,font=("Arial Bold",12), bg="#6B69D6",fg="#FFFFFF",command=AddDetail)
Add_button.grid(row=0,column=0,padx=8,pady=8)

Update_button = Button(Frame2,text="수정",width=15,font=("Arial Bold",12),bg="#6B69D6",fg="#FFFFFF",command=UpdateDetail)
Update_button.grid(row=1,column=0,padx=8,pady=8)


Reset_button = Button(Frame2,text="지움",width=15,font=("Arial Bold",12),bg="#6B69D6",fg="#FFFFFF",command=EntryReset)
Reset_button.grid(row=2,column=0,padx=8,pady=8)
#----------------------------------------------------------------------------

DisplayFrame = Frame(window)
DisplayFrame.grid(row=1,column=0,padx=15,pady=15)

scroll = Scrollbar(DisplayFrame, orient=VERTICAL)
select = Listbox(DisplayFrame, yscrollcommand=scroll.set,font=("Arial Bold",12),bg="#282923",fg="#E7C855",width=40,height=10,borderwidth=3,relief="groove")
scroll.config(command=select.yview)
select.grid(row=0,column=0,sticky=W)
scroll.grid(row=0,column=1,sticky=N+S)



#-----------------------------------------------------------------------------------
ActionFrame = Frame(window)
ActionFrame.grid(row=1,column=1,padx=15,pady=15,sticky=E)

Delete_button = Button(ActionFrame,text="삭제",width=15,font=("Arial Bold",12),bg="#D20000",fg="#FFFFFF",command=DeleteEntry)
Delete_button.grid(row=0,column=0,padx=5,pady=5,sticky=S)

Loadbutton = Button(ActionFrame,text="불러오기",width=15,font=("Arial Bold",12),bg="#6B69D6",fg="#FFFFFF",command=LoadEntry)
Loadbutton.grid(row=1,column=0,padx=5,pady=5)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

ReadCSVFile()

window.mainloop()