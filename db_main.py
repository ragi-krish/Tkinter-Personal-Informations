import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import pymysql
from tkinter import messagebox
from tkinter import filedialog
import db_config
import os.path
from tkcalendar import DateEntry


root=tk.Tk()
root.title("PERSONAL DETAILS")
root.geometry("400x400")

def image_fit(path_image):
    image=Image.open(path_image)
    image=image.resize((200,200),Image.ANTIALIAS)
    image=ImageTk.PhotoImage(image)
    return image
def connection():
    con=pymysql.connect(host=db_config.DB_SERVER,user=db_config.DB_USER,password=db_config.DB_PASSWORD,database=db_config.DB)
    return con
def select_image():
    global image_name
    global image_selected
    global image
    path_image=filedialog.askopenfilename(initialdir="/",title="open file",
                                      filetypes=(("pngs","*.png"),("jpgs","*.jpg"),("jpegs","*.jpeg"),("All files","*.*")))
    print(path_image)
    try:
        if path_image:
            image=image_fit(path_image)
            imglabelTab1.config(image=image)
            imglabelTab1.image=image
            image_selected=True
            image_name=os.path.basename(path_image)
    except:
        print("error")
def insert_data():
    con=connection()
    try:
        if fnameval.get()=="" and famval.get()==""  and jobval.get()=="" and nationval.get()=="":
            messagebox.showerror("Not Completed","Please fill the entry boxes")
        else:    
            sql="INSERT INTO personal_details(fname,famname,dbdate,jobname,nationality,image) VALUES (%s,%s,%s,%s,%s,%s)"
            dt=DbEntryTab1.get_date()
            dtproper=dt.strftime("%y-%m-%d")
            val=(fnameval.get(),famval.get(),dtproper,jobval.get(),nationval.get(),image_name)
            print(val)
            cursor=con.cursor()
            cursor.execute(sql,val)
            cursor.close()
            con.close()
            messagebox.showinfo("connected","inserted values into db")
    except Exception as e:
        messagebox.showerror("error",e)
    
def load_database_results():
    global rows
    global num_of_rows
    con=connection()
    try:
        sql="SELECT * FROM personal_details"
        cursor=con.cursor()
        cursor.execute(sql)
        rows=cursor.fetchall()
        print(rows)
        num_of_rows=cursor.rowcount
        print(num_of_rows)
        cursor.close()
        con.close()
        messagebox.showinfo("success","fetched all records from db")
    except Exception as e:
        messagebox.showerror("ERROR",e)
    return True


def on_tab_selected(event):
    selected_tab=event.widget.select()
    tab_text=event.widget.tab(selected_tab,"text")
    if tab_text=="Add records":
        print("Add records tab selected")
    if tab_text=="view records":
        print("view records tab selected")
notebook=ttk.Notebook(root)
notebook.pack(fill="both",expand=True)

frame1=tk.Frame(notebook)
frame2=tk.Frame(notebook)

frame1.pack(fill="both",expand=True)
frame1.pack(fill="both",expand=True)

notebook.bind("<<NotebookTabChanged>>",on_tab_selected)
notebook.add(frame1,text="Add records")
notebook.add(frame2,text="view records")


default_img="default.png"
default_img_path=db_config.PHOTO_DIRECTORY+default_img
img=image_fit(default_img_path)
##======widgets for tab1===##

fnameval=tk.StringVar()
famval=tk.StringVar()
#dbval=tk.StringVar()
jobval=tk.StringVar()
nationval=tk.StringVar()



fnamelabelTab1 = tk.Label(frame1, text="First Name:",padx=10)
fnamelabelTab1.grid(row=0,column=0)

famlabelTab1 = tk.Label(frame1, text="Family Name:")
famlabelTab1.grid(row=1,column=0)

DbLabelTab1= tk.Label(frame1, text="Date of Birth:")
DbLabelTab1.grid(row=2,column=0)

joblabelTab1 = tk.Label(frame1, text="Job Title:")
joblabelTab1.grid(row=3,column=0)

NationalityTab1=tk.Label(frame1, text="Nationality:")
NationalityTab1.grid(row=4,column=0)

imglabelTab1=tk.Label(frame1,image=img)
imglabelTab1.grid(row=0,column=2,rowspan=5)

button_insert_data=tk.Button(frame1,text="Insert Data",command=insert_data)
button_insert_data.grid(row=5,column=0)
button_insert_img=tk.Button(frame1,text="Insert Image",command=select_image)
button_insert_img.grid(row=5,column=1)

fnameEntryTab1 = tk.Entry(frame1,textvariable=fnameval)
fnameEntryTab1.grid(row=0,column=1)
famEntryTab1 = tk.Entry(frame1,textvariable=famval)
famEntryTab1.grid(row=1,column=1)
#DbEntryTab1 = tk.Entry(frame1,width=30)
#DbEntryTab1.grid(row=2,column=1)
DbEntryTab1=DateEntry(frame1,selectmode='day')
DbEntryTab1.grid(row=2,column=1,padx=15)
jobEntryTab1 = tk.Entry(frame1,textvariable=jobval)
jobEntryTab1.grid(row=3,column=1)
NationalityEntryTab1=tk.Entry(frame1,textvariable=nationval)
NationalityEntryTab1.grid(row=4,column=1)

##======widgets for tab2===##
fnameval2=tk.StringVar()
famval2=tk.StringVar()
dbval2=tk.StringVar()
jobval2=tk.StringVar()
nationval2=tk.StringVar()


fnamelabelTab2 = tk.Label(frame2, text="First Name:")
fnamelabelTab2.grid(row=0,column=0)
famlabelTab2 = tk.Label(frame2, text="Family Name:")
famlabelTab2.grid(row=1,column=0)
DbLabelTab2= tk.Label(frame2, text="Date of Birth:")
DbLabelTab2.grid(row=2,column=0)
joblabelTab2 = tk.Label(frame2, text="Job Title:")
joblabelTab2.grid(row=3,column=0)
NationalityTab2=tk.Label(frame2, text="Job Title:")
NationalityTab2.grid(row=4,column=0)
imglabelTab2=tk.Label(frame2)
imglabelTab2.grid(row=0,column=2,rowspan=5)


button_forward=tk.Button(frame2,text="Next >>")
button_forward.grid(row=5,column=0)
button_backward=tk.Button(frame2,text="<< Back")
button_backward.grid(row=5,column=1)

fnameEntryTab2 = tk.Entry(frame2,textvariable=fnameval2)
fnameEntryTab2.grid(row=0,column=1)
famEntryTab2 = tk.Entry(frame2,textvariable=famval2)
famEntryTab2.grid(row=1,column=1)
DbEntryTab2 = tk.Entry(frame2,textvariable=dbval2)
DbEntryTab2.grid(row=2,column=1)
jobEntryTab2 = tk.Entry(frame2,textvariable=jobval2)
jobEntryTab2.grid(row=3,column=1)
NationalityEntryTab2=tk.Entry(frame2,textvariable=nationval2)
NationalityEntryTab2.grid(row=4,column=1)

success=load_database_results()
if success:
    fnameval2.set(rows[0][1])
    famval2.set(rows[0][2])
    dbval2.set(rows[0][3])
    jobval2.set(rows[0][4])
    nationval2.set(rows[0][5])
    #image_path=db_config.PHOTO_DIRECTORY+rows[0][6]
else:
    print("error")
root.mainloop()