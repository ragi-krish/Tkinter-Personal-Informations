import tkinter as tk
my_w = tk.Tk()
my_w.geometry("400x300") 

f_done=('Times',22,'overstrike','italic') # font values to use
f_normal=('Times',22,'normal')   # font values to use 
def my_upd(k): 
    if(my_ref[k][1].get()==True):
        my_ref[k][0].config(font=f_done,fg='green')
    else:
        my_ref[k][0].config(font=f_normal,fg='blue')

my_dict={'a':'My Task 1','b':'My Task 2','c':'My Task 3'}
my_ref={}
label1=tk.Label(my_w,text="MY TASKS",fg='green',font=('arial',22))
label1.grid(row=0,column=0,padx=10,pady=10)
i=1

for k in my_dict.keys():
    var=tk.BooleanVar() # variable 
    ck = tk.Checkbutton(my_w, text=my_dict[k],variable=var,onvalue=True,offvalue=False,font=f_normal,fg='blue',
                        command=lambda k=k:my_upd(k))
    ck.grid(row=i,column=0,padx=10,pady=25) 
    my_ref[k]=[ck,var]
    i+=1
    print(my_ref)
 
my_w.mainloop()